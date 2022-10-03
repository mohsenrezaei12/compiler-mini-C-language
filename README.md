# first-two-phases-of-a-compiler-for-mini-C-language

### First step:Lexical analysis without using tools
In this stage of lexical analysis, some examples of lexical structures, including keywords, identifiers, operators, etc., are extracted from the given grammar, and regular expressions related to them are created.


### Second step: Lexical analysis using Lexer tools(PLY)
In this step, we do the same work done in the previous step with the help of the PLY library in python. Regular expressions in the desired format are given as input to the lexer to identify the tokens used in the program.
 
### Third step: Syntax analysis using Yacc (Parser)
In this step, we convert the given grammar to the format of the tool to perform syntax analysis automatically. The program's output is to declare that the program is syntactically correct or to show an error message if there is an error.
