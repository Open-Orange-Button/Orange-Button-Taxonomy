/**
 * Wrapper of IBM OAS (@ibm-cloud/openapi-ruleset) to let its schema rules check schema definitions in OpenAPI components.
 *
 * The code here (https://github.com/IBM/openapi-validator/blob/098138ab7387a18f1a600ff33da9430ed1c4461f/packages/ruleset/src/collections/index.js#L11)
 * shows that schema rules of IBM OAS only check schema definitions that are used in an OpenAPI path, not those only defined in OpenAPI components.
 */
const IBMOAS = require('@ibm-cloud/openapi-ruleset');
const { schemas: locationsWhereSchemaCanBeUsed } = require('@ibm-cloud/openapi-ruleset/src/collections/index.js');
Object.values(IBMOAS.rules).forEach(ruleDef => {
  // A schema rule is identified by what JSONPaths it is given to check.
  let isSchemaRule = Array.isArray(ruleDef.given) && ruleDef.given.every(location => locationsWhereSchemaCanBeUsed.includes(location));
  if (isSchemaRule) {
    ruleDef.given = '$.components.schemas[*]';
  }
});
module.exports = {
  extends: IBMOAS
};
