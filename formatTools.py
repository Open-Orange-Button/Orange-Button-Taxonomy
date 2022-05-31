import json
import functools
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


def rename_taxonomy_schemas(taxonomy):
    key_map = {'MCERgroundmotionSS': 'MCERGroundMotionSS',
               'MCERgroundmotionS1': 'MCERGroundMotionS1'}
    new_schemas = {}
    for k, v in taxonomy['components']['schemas'].items():
        if k in key_map:
            new_schemas[key_map[k]] = v
        else:
            new_schemas[k] = v
        if k == 'SeismicLoad':
            new_props = {}
            for r in v['properties']:
                new_props[key_map[r]] = {'$ref': f'#/components/schemas/{key_map[r]}'}
            v['properties'] = new_props
    taxonomy['components']['schemas'] = new_schemas


def duplicate_item_types_after_prefix_removal(taxonomy):
    key_map = old_new_item_type_map(taxonomy)
    lower_case_taxonomy_item_types = {k.lower() for k in taxonomy[ITEM_TYPES]}
    return {old: new['type_name'] for old, new in key_map.items() if new['type_name'].lower() in lower_case_taxonomy_item_types}


def get_recorded_duplicates(taxonomy):
    with open('duplicate_item_types_proposed.json', 'r', encoding='utf-8') as file:
        objs = json.load(file)
        return objs


def update_item_type_entries(item_types, name, old_key, new_key):
    entry_type = 'enums' if 'enums' in item_types[name] else 'units'
    assert old_key in item_types[name][entry_type]
    item_types[name][entry_type] = {(new_key if k == old_key else k): v for k, v in item_types[name][entry_type].items()}
    assert new_key in item_types[name][entry_type]
    # new_entries = {}
    # for k, v in item_types[name][entry_type].items():
    #     if k == old_key:
    #         new_entries[new_key] = v
    #     else:
    #         new_entries[k] = v
    # item_types[name][entry_type] = new_entries


def manual_item_type_entry_updates(taxonomy):
    item_types = taxonomy[ITEM_TYPES]
    update_item_type_entries(item_types, 'StipulationStatusItemType', 'Rescinded ', 'Rescinded')
    update_item_type_entries(item_types, 'WireTypeItemType', 'THWN-2', 'THWN_2')
    update_item_type_entries(item_types, 'CertificationTypeProductItemType', 'CSIP-NRTL', 'CSIP_NRTL')
    update_item_type_entries(item_types, 'CertificationTypeProductItemType', 'UL1973-2-2018', 'UL1973_2_2018')
    update_item_type_entries(item_types, 'CertificationTypeProductItemType', 'IEC62109-1', 'IEC62109_1')
    update_item_type_entries(item_types, 'CertificationTypeProductItemType', 'IEC62109-2', 'IEC62109_2')
    update_item_type_entries(item_types, 'CertificationTypeProductItemType', 'IEC60364-4-41', 'IEC60364_4_41')
    update_item_type_entries(item_types, 'UUIDItemType', '([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\\})', '')
    item_types['UUIDItemType']['enums'] = {
        "UUID": {
            "label": "UUID",
            "description": "An string identifier that matches the regex [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
        }
    }
    update_item_type_entries(item_types, 'CellTechnologyItemType', 'aSi', 'ASi')
    update_item_type_entries(item_types, 'CellTechnologyItemType', 'monoSi', 'MonoSi')
    update_item_type_entries(item_types, 'CellTechnologyItemType', 'polySi', 'PolySi')
    update_item_type_entries(item_types, 'CellTechnologyItemType', 'heterojunction', 'Heterojunction')
    update_item_type_entries(item_types, 'CellTechnologyItemType', 'thinfilm', 'ThinFilm')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Tropicalmegathermalclimates', 'TropicalMegathermalClimates')
    update_item_type_entries(item_types, 'ProjectPhaseItemType', 'Pre_Construction', 'PreConstruction')
    update_item_type_entries(item_types, 'GISFileFormatItemType', 'GEOJson', 'GeoJSON')
    update_item_type_entries(item_types, 'ReserveCollateralItemType', 'LetterofCredit', 'LetterOfCredit')
    update_item_type_entries(item_types, 'RoofItemType', 'ThermoplasticPolyolefin', 'ThermoplasticPolyolefin')
    update_item_type_entries(item_types, 'RoofItemType', 'PolyVinylChloride', 'PolyvinylChloride')
    update_item_type_entries(item_types, 'EnvironmentalConditionsItemType', 'IndustrialEmmissions', 'IndustrialEmissions')
    update_item_type_entries(item_types, 'SecurityInterestItemType', 'DeedofTrust', 'DeedOfTrust')
    update_item_type_entries(item_types, 'ApprovalRequestItemType', 'Notsubmitted', 'NotSubmitted')
    update_item_type_entries(item_types, 'ALTASurveyItemType', 'Notapplicable', 'NotApplicable')
    update_item_type_entries(item_types, 'ProjectInterconnectionItemType', 'InFrontofMeter', 'InFrontOfMeter')
    update_item_type_entries(item_types, 'ProjectInterconnectionItemType', 'BehindtheMeter', 'BehindTheMeter')
    update_item_type_entries(item_types, 'ModuleItemType', 'BiPv', 'BIPV')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Tropicalrainforestclimate', 'TropicalRainForestClimate')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Tropicalmonsoonclimate', 'TropicalMonsoonClimate')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Tropicalwetanddryorsavannaclimates', 'TropicalWetAndDryOrSavannaClimates')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Drydesertandsemi_aridclimates', 'DryDesertAndSemiAridClimates')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Temperatemesothermalclimates', 'TemperateMesothermalClimates')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Mediterraneanclimates', 'MediterraneanClimates')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Humidsubtropicalclimates', 'HumidSubtropicalClimates')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Oceanicclimates', 'OceanicClimates')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Highlandclimates', 'HighlandClimates')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Continentalmicrothermalclimates', 'ContinentalMicrothermalClimates')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Hotsummercontinentalclimates', 'HotSummerContinentalClimates')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Warmsummercontinentalorhemiborealclimates', 'WarmSummerContinentalOrHemiborealClimates')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Subarcticorborealclimates', 'SubarcticOrBorealClimates')
    update_item_type_entries(item_types, 'ClimateClassificationKoppenItemType', 'Polarclimates', 'PolarClimates')
    update_item_type_entries(item_types, 'FinancialTransactionItemType', 'ContributiontoPrincipalCash', 'ContributionToPrincipalCash')
    update_item_type_entries(item_types, 'FinancialTransactionItemType', 'PPAOperationsandMaintenance', 'PPAOperationsAndMaintenance')
    update_item_type_entries(item_types, 'FinancialTransactionItemType', 'LeaseOperationsandMaintenance', 'LeaseOperationsAndMaintenance')
    update_item_type_entries(item_types, 'FinancialTransactionItemType', 'PrincipalCashPaidtoBeneficiary', 'PrincipalCashPaidToBeneficiary')
    update_item_type_entries(item_types, 'EntityRoleItemType', 'InsurerProjectPerfomance', 'InsurerProjectPerformance')
    update_item_type_entries(item_types, 'DocumentSubmissionMethodItemType', 'Epermitting', 'EPermitting')
    update_item_type_entries(item_types, 'PermitIssueMethodItemType', 'Epermitting', 'EPermitting')
    update_item_type_entries(item_types, 'BillOfMaterialsStatusItemType', 'Cancelled', 'Canceled')
    update_item_type_entries(item_types, 'BillOfServicesStatusItemType', 'Cancelled', 'Canceled')
    # update_item_type_entries(item_types, '', '', '')
    taxonomy['components']['schemas']['TariffStructureID']['allOf'][1]['x-ob-item-type'] = 'UUIDItemType'


def isTaxonomyElement(defn):
    return 'allOf' in defn and any('$ref' in d and 'TaxonomyElement' in d['$ref'] for d in defn['allOf'])

def sample_value_label_to_id(taxonomy):
    defns = taxonomy['components']['schemas']
    for k, v in defns.items():
        if not isTaxonomyElement(v):
            continue
        sv = v['allOf'][1][SCHEMA_SAMPLE_VALUE]
        if isinstance(sv, dict) and 'Unit' in sv:
            it = v['allOf'][1][SCHEMA_ITEM_TYPE]
            if k == 'VoltageDCMax':
                print('hi')
            source = taxonomy[ITEM_TYPES][it]
            if not ('enums' in source or 'units' in source):
                continue
            entries = 'enums' if 'enums' in source else 'units'
            item = list(filter(lambda k: source[entries][k]['label'] == sv['Unit'], source[entries]))
            if len(item) > 0:
                sv['Unit'] = item[0]


def sample_value_values_to_value_units_to_unit(taxonomy):
    defns = taxonomy['components']['schemas']
    for k, v in defns.items():
        if not isTaxonomyElement(v):
            continue
        sv = v['allOf'][1][SCHEMA_SAMPLE_VALUE]
        if isinstance(sv, dict):
            new_sv = {}
            for q, r in sv.items():
                if q == 'Units':
                    new_sv['Unit'] = r
                if q == 'Values':
                    new_sv['Value'] = r
                if q not in {'Units', 'Values'}:
                    new_sv[q] = r
            v['allOf'][1][SCHEMA_SAMPLE_VALUE] = new_sv


def sample_value_not_units_defined(taxonomy):
    defns = taxonomy['components']['schemas']
    for k, v in defns.items():
        if not isTaxonomyElement(v):
            continue
        sv = v['allOf'][1][SCHEMA_SAMPLE_VALUE]
        if isinstance(sv, dict) and 'Unit' in sv:
            it = v['allOf'][1][SCHEMA_ITEM_TYPE]
            source = taxonomy[ITEM_TYPES][it]
            if not 'units' in source:
                new_sv = {}
                for q, r in sv.items():
                    if q != 'Unit':
                        new_sv[q] = r
                v['allOf'][1][SCHEMA_SAMPLE_VALUE] = new_sv


def sample_value_remove_empty_fields(taxonomy):
    defns = taxonomy['components']['schemas']
    for k, v in defns.items():
        if not isTaxonomyElement(v):
            continue
        sv = v['allOf'][1][SCHEMA_SAMPLE_VALUE]
        if isinstance(sv, dict):
            new_sv = {}
            for q, r in sv.items():
                if r != '':
                    new_sv[q] = r
            v['allOf'][1][SCHEMA_SAMPLE_VALUE] = new_sv


def sample_value_empty_string_to_empty_dict(taxonomy):
    defns = taxonomy['components']['schemas']
    for k, v in defns.items():
        if not isTaxonomyElement(v):
            continue
        sv = v['allOf'][1][SCHEMA_SAMPLE_VALUE]
        if sv == '':
            v['allOf'][1][SCHEMA_SAMPLE_VALUE] = {}


def sample_value_str_num_to_num(taxonomy):
    defns = taxonomy['components']['schemas']
    for k, v in defns.items():
        if not isTaxonomyElement(v):
            continue
        sv = v['allOf'][1][SCHEMA_SAMPLE_VALUE]
        if isinstance(sv, dict) and 'Value' in sv and isinstance(sv['Value'], str):
            r = sv['Value'].strip()
            if r.isnumeric():
                if float(r) == int(r):
                    res = int(r)
                else:
                    res = float(r)
                v['allOf'][1][SCHEMA_SAMPLE_VALUE]['Value'] = res


def sample_value_stringify(taxonomy):
    defns = taxonomy['components']['schemas']
    for k, v in defns.items():
        if not isTaxonomyElement(v):
            continue
        if not 'TaxonomyElementString' in v['allOf'][0]['$ref']:
            continue
        sv = v['allOf'][1][SCHEMA_SAMPLE_VALUE]
        if isinstance(sv, dict) and 'Value' in sv:
            r = sv['Value']
            v['allOf'][1][SCHEMA_SAMPLE_VALUE]['Value'] = str(r)


def sample_value_nonempty_str_to_value(taxonomy):
    defns = taxonomy['components']['schemas']
    for k, v in defns.items():
        if not isTaxonomyElement(v):
            continue
        sv = v['allOf'][1][SCHEMA_SAMPLE_VALUE]
        if isinstance(sv, str) and sv != '':
            v['allOf'][1][SCHEMA_SAMPLE_VALUE] = {'Value': sv}





TAXONOMY_FILENAME = 'Master-OB-OpenAPI_in_repo.json'
ITEM_TYPES = 'x-ob-item-types'
SCHEMA_ITEM_TYPE = 'x-ob-item-type'
SCHEMA_ITEM_TYPE_GROUP = 'x-ob-item-type-group'
SCHEMA_SAMPLE_VALUE = 'x-ob-sample-value'
ITEM_TYPE_GROUP = 'x-ob-item-type-groups'


def write_json(fname, d):
    with open(fname, 'w', encoding='utf-8') as file:
        json.dump(d, file, indent=2, ensure_ascii=False)


with open(TAXONOMY_FILENAME, 'r', encoding='utf-8') as taxonomyFile:
    taxonomy = json.load(taxonomyFile)
    write_json('duplicate_item_types.json',
               duplicate_item_types_after_prefix_removal(taxonomy))
    manual_written = get_recorded_duplicates(taxonomy)
    remove_item_type_colon_prefixes(taxonomy, manual=manual_written)
    capitalize_item_type(taxonomy)
    change_item_type_group_type_path(taxonomy)
    capitalize_item_type_group(taxonomy)
    rename_taxonomy_schemas(taxonomy)
    manual_item_type_entry_updates(taxonomy)
    sample_value_label_to_id(taxonomy)
    sample_value_values_to_value_units_to_unit(taxonomy)
    sample_value_not_units_defined(taxonomy)
    sample_value_remove_empty_fields(taxonomy)
    sample_value_empty_string_to_empty_dict(taxonomy)
    sample_value_str_num_to_num(taxonomy)
    sample_value_stringify(taxonomy)
    sample_value_nonempty_str_to_value(taxonomy)
    write_json('Master-OB-OpenAPI.json', taxonomy)
