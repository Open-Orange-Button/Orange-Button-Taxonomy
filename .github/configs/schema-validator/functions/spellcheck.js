let Typo = require('typo-js');
let dictionaries;
export default (input, options) => {
  // initialize dictionaries (global) on first call to function only to prevent initialization on every function call
  dictionaries = dictionaries || options.dictionaries.map(dictInfo => new Typo(dictInfo.name, false, false, { dictionaryPath: dictInfo.path }));
  // split input into substrings of: numbers, one capital followed by lowercase letters, all-caps letters
  let substrings = input.match(/[0-9]+|[A-Z][a-z]+|[A-Z]+(?![a-z])/g) || [];
  let nonNumericalSubstrings = substrings.filter(isNaN);
  let misspellings = nonNumericalSubstrings.filter(s => {
    let anyDictHasWord = dictionaries.reduce((hasWord, dict) => hasWord || dict.check(s), false);
    return !anyDictHasWord;
  });
  if (misspellings.length > 0) {
    return [{ message: misspellings.join(', ') }];
  }
};
