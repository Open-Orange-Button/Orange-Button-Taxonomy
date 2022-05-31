const numericOpenAPITypes = ['number', 'integer'];
const nonnumericOpenAPITypes = ['boolean', 'string'];
export default (input, options, context) => {
    let taxonomy = context.document.data;
    let defValue = input[0].properties.Value;
    let isArray = defValue.type === 'array';
    let elementType = isArray ? defValue.items.type : defValue.type;
    let itemType = input[1]['x-ob-item-type'];
    let itemTypeDef = taxonomy['x-ob-item-types'][itemType];
    if (numericOpenAPITypes.includes(elementType) && itemTypeDef.enums) {
        return [{ message: `This element's Value primitive ${isArray ? 'has items of' : 'is an'} OpenAPI type ${elementType}, but the item type '${itemType}' defines string type enumerations.` }];
    } else if (nonnumericOpenAPITypes.includes(elementType) && itemTypeDef.units) {
        return [{ message: `This element's Value primitive ${isArray ? 'has items of' : 'is an'} OpenAPI type ${elementType}, but the item type '${itemType}' defines units.` }];
    }
}
