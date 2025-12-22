const primitiveValidators = { Decimals: validateDecimals,
                              EndTime: validateEndTime,
                              Precision: validatePrecision,
                              StartTime: validateStartTime,
                              Unit: validateUnit,
                              Value: validateValue };
const ValueValidators = new Set([ValuePercentItemType,
                                 ValueUUIDItemType]);
let validatorOptions;
export default (input, options, context) => {
  validatorOptions = options;
  let taxonomy = context.document.data;
  let results = [];
  let addResult = (message, primitive) => results.push({ message, path: [...context.path, '1', 'x-ob-sample-value', primitive] });
  let sampleValue = getSampleValue(input);
  if (!isObject(sampleValue)) {
    addResult('Sample value must be an object.');
  } else if (options.requireAtLeastOneField && (!isObject(sampleValue) || Object.keys(sampleValue).length === 0)) {
    addResult("Sample value's Value primitive must be defined.");
  } else if (!Object.keys(sampleValue).every(k => primitiveValidators[k])) {
    let extraKeys = Object.keys(sampleValue).filter(k => !primitiveValidators[k]);
    addResult(`These fields are not valid primitives: ${extraKeys.join(', ')}`);
  } else {
    for (let [k, v] of Object.entries(primitiveValidators)) {
      v(input, taxonomy, m => addResult(m, k));
    }
  }
  return results;
}

function isObject(variable) {
  return typeof variable === 'object' && !Array.isArray(variable)
    && variable !== null && variable !== undefined;
}

function getSampleValue(input) {
  return input[1]['x-ob-sample-value'];
}

function getItemType(input) {
  return input[1]['x-ob-item-type'];
}

function getItemTypeGroup(input) {
  return input[1]['x-ob-item-type-group'];
}

function getValueOpenAPIType(input) {
  let Value = input[0].properties.Value;
  let isArray = Value.type === 'array'
  let type = isArray ? Value.items.type : Value.type
  return { isArray, type }
}

function OpenAPITypecheck(value, type) {
  if (type.isArray) {
    return Array.isArray(value) && value.length > 0
      && value.every(v => OpenAPITypecheckNotArray(v, type.type));
  }
  return OpenAPITypecheckNotArray(value, type.type);
}

function OpenAPITypecheckNotArray(value, type) {
  if (type === 'number') {
    return !Number.isNaN(value);
  } else if (type === 'string') {
    return typeof value === 'string';
  } else if (type === 'boolean') {
    return typeof value === 'boolean';
  } else if (type === 'integer') {
    return Number.isInteger(value);
  }
}

function validateDecimals(input, taxonomy, addResult) {}

function validateEndTime(input, taxonomy, addResult) {}

function validatePrecision(input, taxonomy, addResult) {}

function validateStartTime(input, taxonomy, addResult) {}

function validateUnit(input, taxonomy, addResult) {
  let primitive = 'Unit';
  let sampleValue = getSampleValue(input);
  let itemType = getItemType(input);
  let sampleValueUnit = sampleValue[primitive];
  if (itemType && primitive in sampleValue) {
    let itemTypeDef = taxonomy['x-ob-item-types'][itemType];
    if (!itemTypeDef) {
      // ignore if item type does not exist, this is checked separately
      return;
    }
    let itemTypeUnits = itemTypeDef['units'];
    if (!itemTypeUnits) {
      addResult(`Cannot define 'Unit' because the item type '${itemType}' does not define units.`);
    } else {
      let itemTypeGroup = getItemTypeGroup(input);
      let itemTypeGroupDef = taxonomy['x-ob-item-type-groups'][itemTypeGroup];
      if (!itemTypeUnits[sampleValueUnit]) {
        addResult(`The item type '${itemType}' does not define the unit '${sampleValueUnit}'.`);
      } else if (itemTypeGroupDef && !itemTypeGroupDef.group.includes(sampleValueUnit)) {
        addResult(`The item type group '${itemTypeGroup}' does not define the unit '${sampleValueUnit}'.`)
      }
    }
  }
}

function validateValue(input, taxonomy, addResult) {
  let primitive = 'Value';
  let sampleValue = getSampleValue(input);
  let itemType = getItemType(input);
  if (itemType && primitive in sampleValue) {
    let itemTypeDef = taxonomy['x-ob-item-types'][itemType];
    if (!itemTypeDef) {
      // ignore if item type does not exist, this is checked separately
      return;
    }
    let itemTypeEnums = itemTypeDef['enums'];
    let sampleValueValue = sampleValue[primitive];
    let OpenAPIType = getValueOpenAPIType(input);
    if (!OpenAPITypecheck(sampleValueValue, OpenAPIType)) {
      if (OpenAPIType.isArray) {
          addResult(`Must be an array of type ${OpenAPIType.type}, but the array contains this item: ${sampleValueValue}`);
      } else {
          addResult(`Must be of type ${OpenAPIType.type}. Value: ${sampleValueValue}`);
      }
    } else if (OpenAPIType.type === 'string' && sampleValueValue.length === 0) {
      addResult(`Must not be an empty string.`);
    } else if (itemTypeEnums && !validatorOptions.enumItemTypeIgnoreList.includes(itemType)) {
      let itemTypeGroup = getItemTypeGroup(input);
      let itemTypeGroupDef = taxonomy['x-ob-item-type-groups'][itemTypeGroup];
      if (!itemTypeEnums[sampleValueValue]) {
        addResult(`The item type '${itemType} does not define the enum '${sampleValueValue}'.`);
      } else if (itemTypeGroupDef && !itemTypeGroupDef.group.includes(sampleValueValue)) {
        addResult(`The item type group '${itemTypeGroup}' does not define the enum '${sampleValueValue}'.`)
      }
    } else {
      ValueValidators.forEach(v => v(sampleValueValue, itemType, addResult));
    }
  }
}

function ValuePercentItemType(value, itemType, addResult) {
  if (itemType === 'PercentItemType') {
    if (value < 0 || value > 100) {
      addResult(`(${itemType}) Must be between 0 and 100. Value: ${value}`);
    }
  }
}

function ValueUUIDItemType(value, itemType, addResult) {
  if (itemType === 'UUIDItemType') {
    let uuidRegex = '^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$';
    if (!(new RegExp(uuidRegex)).test(value)) {
      addResult(`(${itemType}) Must match the regex ${uuidRegex}. Value: ${value}.`)
    }
  }
}
