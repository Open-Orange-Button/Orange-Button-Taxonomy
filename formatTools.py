import json
from collections import OrderedDict


def modify_allOf_obj(taxonomy, func):
    for defn in taxonomy["components"]["schemas"].values():
        if "allOf" in defn:
            func(defn)


def modify_item_type_group_types(taxonomy, func):
    for group in taxonomy[ITEM_TYPE_GROUP].values():
        group["type"] = func(group["type"])


def item_type_group_type_parts(path):
    last_slash = path.rindex('/')
    leading_path, type_name = path[:last_slash], path[last_slash + 1:]
    return leading_path, type_name


def add_source_prefix_to_description(item_type, prefix):
    prefix_record_str = 'source prefixes:'
    desc = item_type['description']
    if prefix_record_str not in desc:
        values = 'unit' if 'units' in item_type else 'enum'
        to_add = f'{cap_first_char(values)} {prefix_record_str}'
        if len(desc) > 0:
            if desc[-1] == ' ':
                desc[-1] = '.'
            elif desc[-1] != '.':
                desc += '.'
            item_type['description'] = f'{desc} {to_add} {prefix}'
        else:
            item_type['description'] = f'{to_add} {prefix}'
    else:
        item_type['description'] += f', {prefix}'


def remove_item_type_colon_prefixes(taxonomy, manual=None):
    key_map = old_new_item_type_map(taxonomy)
    new_item_types = {}
    manual = manual or {}
    for k, v in taxonomy[ITEM_TYPES].items():
        prefix, type_name = key_map[k]['prefix'], key_map[k]['type_name']
        if prefix not in {'', 'solar-types'}:
            add_source_prefix_to_description(v, prefix)
        if type_name in manual:
            if ':' not in k:
                new_item_types[type_name] = manual[type_name]
        else:
            new_item_types[type_name] = v
    for k, v in manual.items():
        if k not in new_item_types:
            new_item_types[k] = v
    taxonomy[ITEM_TYPES] = new_item_types

    def allOf_obj(obj):
        target = obj['allOf'][1]
        if SCHEMA_ITEM_TYPE in target:
            s = target[SCHEMA_ITEM_TYPE]
            r = s
            if s in key_map:
                r = key_map[s]['type_name']
            elif ':' in s: # handle referenced item types that do not exist
                r = cap_first_char(s.split(':')[1])
            target[SCHEMA_ITEM_TYPE] = r

    modify_allOf_obj(taxonomy, allOf_obj)

    def item_type_group_type_path(p):
        leading_path, type_name = item_type_group_type_parts(p)
        sub = key_map[type_name]['type_name'] if ':' in p else type_name
        return f'{leading_path}/{sub}'

    modify_item_type_group_types(taxonomy, item_type_group_type_path)


def capitalize_item_type(taxonomy):

    def allOf_obj(obj):
        target = obj['allOf'][1]
        if SCHEMA_ITEM_TYPE in target:
            target[SCHEMA_ITEM_TYPE] = cap_first_char(target[SCHEMA_ITEM_TYPE])

    modify_allOf_obj(taxonomy, allOf_obj)


def capitalize_item_type_group(taxonomy):
    taxonomy[ITEM_TYPE_GROUP] = {cap_first_char(k): v for k, v in taxonomy[ITEM_TYPE_GROUP].items()}

    def allOf_obj(obj):
        target = obj['allOf'][1]
        if SCHEMA_ITEM_TYPE_GROUP in target and (itg := target[SCHEMA_ITEM_TYPE_GROUP]):
            target[SCHEMA_ITEM_TYPE_GROUP] = cap_first_char(itg)
    
    modify_allOf_obj(taxonomy, allOf_obj)


def change_item_type_group_type_path(taxonomy):
    for group in taxonomy[ITEM_TYPE_GROUP].values():
        _, type_name = item_type_group_type_parts(group["type"])
        group["type"] = f'#/x-ob-item-types/{type_name}'


def sort_dict(od):
    od_keys_sorted = [key for key in od.keys()]
    od_keys_sorted.sort()
    new_od = OrderedDict()
    for key in od_keys_sorted:
        new_od[key] = od[key]
    return new_od


def cap_first_char(mstr):
    if (mstrl := mstr.lower()).startswith('uuid'):
        return f'UUID{mstr[mstrl.index("d") + 1:]}'
    return f'{mstr[0].capitalize()}{mstr[1:]}'


def old_new_item_type_map(taxonomy):
    result = {}
    for key in taxonomy[ITEM_TYPES]:
        prefix, item_type = '', cap_first_char(key)
        if ':' in key:
            key_parts = key.split(':')
            prefix, item_type = key_parts[0], cap_first_char(key_parts[1])
        result[key] = {'prefix': prefix, 'type_name': item_type}
    return result


def duplicate_item_types_after_prefix_removal(taxonomy):
    key_map = old_new_item_type_map(taxonomy)
    lower_case_taxonomy_item_types = {k.lower() for k in taxonomy[ITEM_TYPES]}
    return {old: new['type_name'] for old, new in key_map.items() if new['type_name'].lower() in lower_case_taxonomy_item_types}


def get_recorded_duplicates(taxonomy):
    with open('duplicate_item_types_proposed.json', 'r', encoding='utf-8') as file:
        objs = json.load(file)
        return objs


TAXONOMY_FILENAME = 'Master-OB-OpenAPI_in_repo.json'
ITEM_TYPES = 'x-ob-item-types'
SCHEMA_ITEM_TYPE = 'x-ob-item-type'
SCHEMA_ITEM_TYPE_GROUP = 'x-ob-item-type-group'
ITEM_TYPE_GROUP = 'x-ob-item-type-groups'


def write_json(fname, d):
    with open(fname, 'w', encoding='utf-8') as file:
        json.dump(d, file, indent=2, ensure_ascii=False)


with open(TAXONOMY_FILENAME, 'r', encoding='utf-8') as taxonomyFile:
    taxonomy = json.load(taxonomyFile)
    write_json('duplicate_item_types.json', duplicate_item_types_after_prefix_removal(taxonomy))
    manual_written = get_recorded_duplicates(taxonomy)
    remove_item_type_colon_prefixes(taxonomy, manual=manual_written)
    capitalize_item_type(taxonomy)
    change_item_type_group_type_path(taxonomy)
    capitalize_item_type_group(taxonomy)
    write_json('Master-OB-OpenAPI.json', taxonomy)
