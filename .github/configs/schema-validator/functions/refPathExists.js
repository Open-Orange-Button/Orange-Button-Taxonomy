export default (input, options, context) => {
  let refPathResolvedObj = input.split('/').filter(key => key !== '#')
    .reduce((obj, key) => obj[key] ? obj[key] : false, context.document.data);
  if (!refPathResolvedObj) {
    return [{ message: input }];
  }
}
