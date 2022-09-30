letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
            ,'n','o','p','q','r','s','t','u','v','w','x','y','z'
            ,'A','B','C','D','E','F','G','H','I','J','K','L','M'
            ,'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

digits = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['+','=','(',')','{','}','-','*','/',';','<','>','!','"']

whitespace = ['\n','\t',' ']

keywords = ['if','while','else','for','print','char','int']


current_state = 1
current_point = -1




def get_token(current_line):

    global current_state
    global current_point

    current_state = 1


    token = ""

    while(True):

        if(current_state == 1):
            ch = get_next_char(current_line)
            token = token +ch



            if(is_digit(ch)):
                current_state = 2

            elif(is_letter(ch)):
                current_state = 3



            elif(is_symbol(ch)):
                current_state = 4

            elif(is_whitespace(ch)):
                current_state = 5

            else:
                return token + "is not defined "



        elif(current_state == 2):

            if(is_digit(check_next_char(current_line))):

                ch = get_next_char(current_line)
                token = token + ch
                current_state = 2

            else:
                return "< " + token + " , integer > "






        elif(current_state == 3):


            if(is_digit(check_next_char(current_line)) or is_letter(check_next_char(current_line))):

                ch = get_next_char(current_line)
                token = token + ch
                current_state = 3


            else:
                if(is_keyword(token)):
                    return "<" + token + " , KEYWORD >"

                else:
                    return "<" + token + " , IDENTIFIER >"



        elif(current_state == 4):
            if(is_symbol(check_next_char(current_line))):

                ch = get_next_char(current_line)
                token = token + ch
                current_state = 4

            else:
                return "< " + token + " , symbol > "


        elif (current_state == 5):

            #token = ""
            current_state = 1
            if(token=='\n'):
                return "< " + repr("\n") + " , white space > "
            if(token==' '):
                return "< " + "space" + " , white space > "
            if(token=='\t'):
                return "< " + repr("\t") + " , white space > "





#---------------get_char-----------------------------------

def get_next_char(current_line):

    global current_point

    current_point = current_point + 1

    if ( current_point >= len(current_line)):
        return "error"


    ch = current_line[current_point]

    if(not(is_digit(ch) or is_letter(ch) or is_symbol(ch) or is_whitespace(ch))):

        print("character " + ch + " is not in Alphabet")


    return ch

#-------------------------------check_cahr----------------------------

def check_next_char(current_line):

    global current_point

    if (current_point+1 >= len(current_line)):
        return "error"
    ch = current_line[current_point + 1]

    return ch

#-----------------is_methods -----------------------------

def is_digit(ch):
    if (ch in digits):
        return True
    else:
        return False


def is_letter(ch):
    if(ch in letters):
        return True
    else:
        return False


def is_symbol(ch):
    if(ch in symbols):
        return True
    else:
        return False


def is_whitespace(ch):
    if(ch in whitespace):
        return True
    else:
        return False


def is_keyword(ch):
    if(ch in keywords):
        return True
    else:
        return False

#-----------------------main---------------------


fo= open('test5.txt' , 'r')
test=fo.read()
fo.close()

fr = open("out_test5.txt", 'w')


while(current_point < len(test) -1):

    token = get_token(test)
    fr.write(token + "\n")
    print(token)

fr.close()
