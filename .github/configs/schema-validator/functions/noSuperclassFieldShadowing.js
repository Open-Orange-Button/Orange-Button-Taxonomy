export default (input, options, context) => {
    let superclassFields = new Set(Object.keys(getSuperclassProperties(input[0])));
    let subclassFields = Object.keys(input[1].properties);
    let shadowedFields = subclassFields.filter(p => superclassFields.has(p)).sort();
    if (shadowedFields.length > 0) {
        return [{ message: `OB Object defines fields that shadow fields defined by its superclass: ${shadowedFields.join(', ')}` }];
    }
}

function getSuperclassProperties(defn) {
    if (defn.properties) {
        return defn.properties;
    }
    let properties = defn.allOf[1].properties;
    if (Object.keys(properties).length > 0) {
        return properties;
    }
    return getSuperclassProperties(defn.allOf[0]);
}
