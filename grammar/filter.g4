grammar filter;

filter: condition EOF;

condition: manaCondition 
               | textCondition 
               | toughnessCondition 
               | powerCondition 
               | typeCondition
               | conjunctiveCondition;

conjunctiveCondition: '(' condition logicalOperator condition ')';

manaCondition: 'mana value' comparisonOperator INT;
powerCondition: 'power' comparisonOperator INT;
toughnessCondition: 'toughness' comparisonOperator INT;
textCondition: 'text' textOperator STRING;
typeCondition: 'type' textOperator STRING;

comparisonOperator: '=' | '<' | '>';
textOperator: 'contains' | 'not contains';

logicalOperator: AND | OR;

AND: 'and';
OR: 'or';

INT: [0-9]+;
STRING: '"' .*? '"';
WS: [ \t\n\r]+ -> skip;