export default (input, options, context) => {
  let schemas = context.document.data.components.schemas;
  if (!schemas[input].allOf?.[1]?.['x-ob-item-type']) {
    return;
  }

  let elementRef = `#/components/schemas/${input}`;
  let isReferenced = Object.values(schemas).some(schema =>
    [schema.properties, schema.allOf?.[1]?.properties]
      .filter(Boolean)
      .some(properties => Object.values(properties).some(property => property.$ref === elementRef))
  );
  if (!isReferenced) {
    return [{ message: input }];
  }
}
