export default (input, options, context) => {
  let itemTypes = Object.keys(context.document.data[options.objectPath]);
  if (input && !itemTypes.includes(input)) {
    return [{ message: input }];
  }
}
