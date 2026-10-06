export default (input, options, context) => {
  let schemas = Object.values(context.document.data.components.schemas);
  let isReferenced = schemas.some(schema => schema.allOf?.[1]?.[options.field] === input);
  if (!isReferenced) {
    return [{ message: input }];
  }
}
