// Define a grammar called Hello
grammar Hello;
r  : 'hello' name ('and' name)* ;         // match keyword hello followed by an identifier
name : ID ID* ID ;
ID : [a-z]+ ;             // match lower-case identifiers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
