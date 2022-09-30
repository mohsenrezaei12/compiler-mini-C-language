import ply.lex as lex

# List of token names.

reserved = {
    'if'    :  'IF_KEYWORD',
    'while' :  'WHILE_KEYWORD',
    'else'  :  'ELSE_KEYWORD',
    'for'   :  'FOR_KEYWORD',
    'print' :  'PRINT_KEYWORD',
    'char'  :  'CHAR_KEYWORD',
    'int'   :  'INT_KEYWORD',
}

tokens = [
    'NUMBER',
    'GREATER_THAN_EQUAL',
    'LESS_THAN_EQUAL',
    'GREATER_THAN',
    'LESS_THAN',
    'SEMI_COLON',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'KEYWORD',
    'RPAREN',
    'IDENTIFIER',
    'EQUAL',
    'APPOINTMENT',
    'ID',
    'LBRACKET',
    'RBRACKET',
    'DOUBLEQUOTATION'


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
t_SEMI_COLON              = r'\;'
t_APPOINTMENT           = r'\='
t_DIVIDE                = r'/'
t_LPAREN                = r'\('
t_RPAREN                = r'\)'
t_LBRACKET               = r'\{'
t_RBRACKET               = r'\}'
t_DOUBLEQUOTATION       = r'\"'




def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for reserved words
    t.type = reserved.get(t.value, 'ID')
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


# Test it
f=open('test5.txt','r');
data=f.read();
f=open('out_test5.txt','w');



# Give the lexer some input
lexer.input(data)



# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    #print(tok)
    f.write(str(tok)+"\n");
