const numericOpenAPITypes = ['number', 'integer'];
let itemTypeUsageHistory = {};
export default (input, options, context) => {
    let taxonomy = context.document.data;
    let defValue = input[0].properties.Value;
    let isArray = defValue.type === 'array';
    let elementType = isArray ? defValue.items.type : defValue.type;
    let itemType = input[1]['x-ob-item-type'];
    let itemTypeDef = taxonomy['x-ob-item-types'][itemType];
    let errorMessageFirstPart = (elementType, isArray) => `This element's Value primitve ${isArray ? 'has items of' : 'is an'} OpenAPI type '${elementType}'`;
    if (numericOpenAPITypes.includes(elementType) && itemTypeDef.enums) {
        return [{ message: `${errorMessageFirstPart(elementType, isArray)}, but the item type '${itemType}' defines 'string' type enumerations.` }];
    } else if (elementType === 'string' && itemTypeDef.units) {
        return [{ message: `${errorMessageFirstPart(elementType, isArray)}, but the item type '${itemType}' defines units.` }];
    } else if (elementType === 'boolean' && itemType !== 'BooleanItemType') {
        return [{ message: `${errorMessageFirstPart(elementType, isArray)}, so its item type must be 'BooleanItemType', not '${itemType}'.`}];
    }
    if (!(itemTypeDef.enums || itemTypeDef.units)) {
        if (itemTypeUsageHistory[itemType]) {
            let matchesHistoricalType = elementType === itemTypeUsageHistory[itemType].OpenAPIType;
            if (!matchesHistoricalType) {
                return [{ message: `${errorMessageFirstPart(elementType, isArray)}, but the item type '${itemType}' is used with other OpenAPI types, for example '${itemTypeUsageHistory[itemType].OpenAPIType}' for '${itemTypeUsageHistory[itemType].firstUse}'.` }];
            }
        } else {
            itemTypeUsageHistory[itemType] = { OpenAPIType: elementType, firstUse: context.path.at(2) };
        }
    }
}
