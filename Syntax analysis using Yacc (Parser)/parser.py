import ply.yacc as yacc
import lexer_ply

tokens = lexer_ply.tokens

start = 'program'



precedence = (
    ('left', 'AND', 'OR'),
    ('left', 'GREATER_THAN', 'LESS_THAN',
     'GREATER_THAN_EQUAL',
     'LESS_THAN_EQUAL',),
    ('left', 'APPOINTMENT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),

)


def p_program(p):
    """
     program    :   decl_list
    """
    pass



def p_decl_list(p):
    """
    decl_list   :   decl_list decl
                |   decl

    """
    pass

def p_decl(p):
    """
    decl    :   var_decl
            |   fun_decl
    """
    pass

def p_var_decl(p):
    """
    var_decl    :   type_spec IDENT SEMICOLON
                |   type_spec IDENT LBRACKET RBRACKET SEMICOLON
    """
    pass

def p_type_spec(p):
    """
    type_spec   :   VOID
                |   BOOL
                |   INT
                |   FLOAT
                |   CHAR
    """
    pass

def p_fun_decl(p):
    """
    fun_decl    :   type_spec IDENT LPAREN params RPAREN compound_stmt
    """
    pass

def p_params(p):
    """
    params  :   param_list
            |   VOID
            |   empty
    """
    pass

def p_param_list(p):
    """
    param_list  :   param_list COMMA param
                |   param
    """
    pass

def p_param(p):
    """
    param   :   type_spec IDENT
            |   type_spec IDENT LBRACKET RBRACKET
    """
    pass

def p_compound_stmt(p):
    """
    compound_stmt   :     local_decls stmt_list
    """
    pass

def p_local_decls(p):
    """
    local_decls    :    local_decls local_decl
                   |    empty
    """
    pass

def p_local_decl(p):
    """
    local_decl     :    type_spec IDENT SEMICOLON
                   |    type_spec IDENT LBRACKET RBRACKET SEMICOLON
    """
    pass

def p_stmt_list(p):
    """
    stmt_list   :   stmt_list stmt
                |   empty
    """
    pass

def p_stmt(p):
    """
    stmt    :   expr_stmt
            |   if_stmt
            |   while_stmt
            |   return_stmt

    """
    pass

def p_expr_stmt(p):
    """
    expr_stmt   :   expr SEMICOLON
                |   SEMICOLON
    """
    pass

def p_while_stmt(p):
    """
    while_stmt  :   WHILE LPAREN expr RPAREN stmt
    """
    pass


def p_if_stmt(p):
    """
    if_stmt  :     IF LPAREN expr RPAREN stmt
             |     IF LPAREN expr RPAREN stmt ELSE stmt
    """
    pass



def p_return_stmt(p):
    """
    return_stmt  :   RETURN SEMICOLON
                 |   RETURN expr SEMICOLON
    """
    pass


def p_expr(p):
    """
    expr    :   IDENT APPOINTMENT expr
            |   IDENT LBRACKET expr RBRACKET EQUAL expr
            |   expr OR expr
            |   expr AND expr
            |   expr EQUAL expr
            |   expr APPOINTMENT NUMBER
            |   expr LESS_THAN_EQUAL expr
            |   expr GREATER_THAN_EQUAL expr
            |   expr LESS_THAN expr
            |   expr GREATER_THAN expr
            |   expr TIMES expr
            |   expr PLUS expr
            |   expr DIVIDE expr
            |   expr MINUS expr
            |   '!' expr
            |   LPAREN expr RPAREN
            |   IDENT
            |   IDENT LBRACKET expr RBRACKET
            |   IDENT LPAREN args RPAREN
            |   NUMBER
    """


    if len(p) == 2:
        p[0] = p[1]



def p_arg_list(p):
    """
    arg_list    :   arg_list COMMA expr
                |   expr
    """
    pass

def p_args(p):
    """
    args    :   arg_list
            |   empty
    """
    pass


def p_empty(p):
    'empty : '
    pass


print("\033[31m" + "------------------------------" + "\033[39m")

def p_error(p):
     if p is not None:
        print("There is a syntax error!", p)


parser = yacc.yacc()
file = open(lexer_ply.input_address , "r")
input_data= file.read()



while True:
    try:
        print(input_data)
        s = input_data
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)

    if result == None:
        print("\033[31m" + "------------------------------" + "\033[39m")
        print("\033[32m"+"Parsing Successfully Finished!"+"\033[39m")
        print("\033[34m" + "paser.out and parsing_tables files generated!" + "\033[39m")
        break
