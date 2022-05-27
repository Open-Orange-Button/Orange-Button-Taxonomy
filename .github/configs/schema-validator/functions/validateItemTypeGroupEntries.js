export default (input, options, context) => {
  let itemTypeGroup = context.document.data['x-ob-item-type-groups'][input];
  let itemTypeGroupType = itemTypeGroup.type.split('/').filter(key => key !== '#')
    .reduce((obj, key) => obj[key] ? obj[key] : false, context.document.data);
  if (!itemTypeGroupType) {
    // ignore if type ref path is not resolved, this is checked separately
    return;
  }
  let groupEntires = itemTypeGroup.group;
  // Entries of an item type definition
  let typeInstances = itemTypeGroupType.enums || itemTypeGroupType.units;
  let typeInstanceNames = Object.keys(typeInstances);
  let missingEntries = groupEntires.filter(entry => !typeInstanceNames.includes(entry));
  if (missingEntries.length > 0) {
    return [{ message: `These entries of item type group '${input}' are not untis or enums of item type '${itemTypeGroup.type.split('/').at(-1)}': ${missingEntries.join(', ')}` }];
  }
}
