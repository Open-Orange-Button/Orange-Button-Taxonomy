const { Resolver } = require('@stoplight/json-ref-resolver');
const resolver = new Resolver();
let taxonomy; // copy of taxonomy to store added $ref's pointing to item type group types
let itemTypeGroupTypesMap = {};
export default async (input, options, context) => {
	if (!taxonomy) {
		taxonomy = JSON.parse(JSON.stringify(context.document.data));
		// Add item type groups' type value as $ref for the resolver to resolve
		for (let [groupName, groupDef] of Object.entries(taxonomy['x-ob-item-type-groups'])) {
			itemTypeGroupTypesMap[groupName] = groupDef.type;
			groupDef.$ref = groupDef.type;
		}
	}
	let itemTypeGroupRef = `#/x-ob-item-type-groups/${input}`;
	let resolved = await resolver.resolve(taxonomy, { jsonPointer: itemTypeGroupRef });
	if (resolved.errors.some(err => err.code === 'POINTER_MISSING')) {
		return [{ message: itemTypeGroupTypesMap[input] }];
	}
}
