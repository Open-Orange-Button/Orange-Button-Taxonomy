export default (input, options, context) => {
  let items = Object.keys(context.document.data[options.objectPath]);
  if (input && !items.includes(input)) {
    return [{ message: input }];
  }
}
