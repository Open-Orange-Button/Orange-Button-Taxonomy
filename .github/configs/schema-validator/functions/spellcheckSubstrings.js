let Typo = require('typo-js');
let dictionaries;
export default (input, options) => {
  // initialize dictionaries (global) on first call to function only to prevent initialization on every function call
  dictionaries = dictionaries || options.dictionaries.map(dictInfo => new Typo(dictInfo.name, false, false, { dictionaryPath: dictInfo.path }));
  let substrings = input.match(new RegExp(options.substringMatch, 'g')) || [];
  // filter out numbers since numbers are not words
  let nonNumericalSubstrings = substrings.filter(isNaN);
  // filter for substrings not in any dictionary
  let misspellings = nonNumericalSubstrings.filter(s => !dictionaries.some(dict => dict.check(s)));
  let wholeInputIsWord = dictionaries.some(dict => dict.check(input));
  if (!wholeInputIsWord && misspellings.length > 0) {
    return [{ message: misspellings.join(', ') }];
  }
};
