let Typo = require('typo-js');
let dictionaries;
export default (input, options) => {
  // initialize dictionaries (global) on first call to function only to prevent initialization on every function call
  dictionaries = dictionaries || options.dictionaries.map(dictInfo => new Typo(dictInfo.name, false, false, { dictionaryPath: dictInfo.path }));
  // split input into substrings of: numbers, one capital followed by lowercase letters, all-caps letters
  let substrings = input.match(/[0-9]+|[A-Z][a-z]+|[A-Z]+(?![a-z])/g) || [];
  // filter out numbers since numbers are not words
  let nonNumericalSubstrings = substrings.filter(isNaN);
  // filter for substrings not in any dictionary
  let misspellings = nonNumericalSubstrings.filter(s => !dictionaries.some(dict => dict.check(s)));
  if (misspellings.length > 0) {
    return [{ message: misspellings.join(', ') }];
  }
};
