import ply.lex as lex

# List of token names.

reserved = {
    'if'    :  'IF',
    'while' :  'WHILE',
    'else'  :  'ELSE',
    'for'   :  'FOR',
    'print' :  'PRINT',
    'char'  :  'CHAR',
    'int'   :  'INT',
    'void'  :  'VOID',
    'bool'  :  'BOOL',
    'float' :  'FLOAT',
    'return':  'RETURN',
    'or'    :  'OR',
    'and'   :  'AND',



}

tokens = [
    'NUMBER',
    'GREATER_THAN_EQUAL',
    'LESS_THAN_EQUAL',
    'GREATER_THAN',
    'LESS_THAN',
    'SEMICOLON',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'KEYWORD',
    'RPAREN',
    'IDENT',
    'EQUAL',
    'APPOINTMENT',
    'ID',
    'LCBRACKET',
    'RCBRACKET',
    'DOUBLEQUOTATION',
    'COMMA',
    'LBRACKET',
    'RBRACKET',


] + list(reserved.values())
# Regular expression rules for simple tokens
t_PLUS                  = r'\+'
t_MINUS                 = r'\-'
t_TIMES                 = r'\*'
t_EQUAL                 = r'\=='
t_GREATER_THAN_EQUAL    = r'\>='
t_LESS_THAN_EQUAL       = r'\<='
t_GREATER_THAN          = r'\>'
t_LESS_THAN             = r'\<'
t_SEMICOLON             = r'\;'
t_APPOINTMENT           = r'\='
t_DIVIDE                = r'/'
t_LPAREN                = r'\('
t_RPAREN                = r'\)'
t_LCBRACKET             = r'\{'
t_RCBRACKET             = r'\}'
t_DOUBLEQUOTATION       = r'\"'
t_COMMA                 = r'\,'
t_LBRACKET              = r'\['
t_RBRACKET              = r'\]'




def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for reserved words
    t.type = reserved.get(t.value, 'IDENT')
    return t


# A regular expression rule with some action code
def t_NUMBER(t):
     r'\d+'
     t.value = int(t.value)
     return t

# Define a rule so we can track line numbers
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)



# A string containing ignored characters (spaces and tabs)

t_ignore  = ' \t'

# Error handling rule
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

input_address = 'test5.txt'
# Test it
f=open(input_address,'r');
data=f.read();
f=open('out_' + input_address,'w');



# Give the lexer some input
lexer.input(data)



# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

    f.write(str(tok)+"\n");
