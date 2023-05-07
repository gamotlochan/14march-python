import random
import array
 
MAX_LEN = 8
 
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
L_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
U_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
SYMBOLS = ['@', '#', '$', '%','*']
 
COMBINED_LIST = DIGITS + U_CHARACTERS + L_CHARACTERS + SYMBOLS
 
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(U_CHARACTERS)
rand_lower = random.choice(L_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
 
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
 
for J in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
 
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
 
password = ""
for J in temp_pass_list:
        password = password + J
         
print(password)
