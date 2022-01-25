#TODO: Create a program that generates random passwords based on the user's chocie and save them an encrypted place in the system
from random import choices, shuffle,randint
from os import path
def validate_password(password):
    x = 0
    while x == 0:
        try:
            password = int(input("What should the length of the password be?\n"))
            x = -1
        except ValueError as e:
            print("You have to enter a valid number for the password length, it should be a whole number / integer. Please try again")
    return password

def validate_user_input(user_input,input_type):
    valid_answer = ["Yes", "No", "yes", "no","y","n","Y","N"]
    any_answer=[str(x) for x in valid_answer]
    possible_choices=",".join(x for x in any_answer)
    x = 0
    while x == 0:
        try:
            user_input=input(f"Do you want {input_type} in your password\n")
            if user_input in valid_answer:
                x = -1
            else:
                raise ValueError(f"That is not a valid answer. Choose between {possible_choices}. Please try again.")
        except ValueError as e:
            print(e)
    return user_input
def ask_for_input():
    file_name = input("What should be the name of the file where the passsword will be added?\n")
    captalized_letters_exists=""
    small_letters_exists=""
    password_len=""
    digits_exists=""
    special_chrs_exists = ""
    password_len = validate_password(password_len)
    captalized_letters_exists=validate_user_input(captalized_letters_exists,"capitalized letters")
    small_letters_exists=validate_user_input(small_letters_exists,"small letters")
    digits_exists=validate_user_input(digits_exists,"digits")
    special_chrs_exists=validate_user_input(special_chrs_exists,"special characters")
    return [file_name,password_len,captalized_letters_exists,small_letters_exists,digits_exists,special_chrs_exists]
small_letters=[chr(x) for x  in range(97,123)]
captalized_letters=[chr(x) for x  in range(65,91)]
digits=[chr(x) for x  in range(48,58)]
special_chrs=[chr(x) for x  in range(32,48)]+([chr(x) for x  in range(58,65)])+([chr(x) for x  in range(91,97)])+([chr(x) for x  in range(123,127)])
inputs=ask_for_input()
print(type(inputs))
print(inputs)
digits_in_password=0
small_letters_in_password=0
big_letters_in_password=0
special_chrs_in_password=0
# all_in_password=digits_in_password+small_letters_in_password+big_letters_in_password+special_chrs_in_password
# while not all_in_password==ask_for_input:
#     x=randint(1,ask_for_input(1))
#     y=randint(1,ask_for_input(1))
#     z=randint(1,ask_for_input(1))
#     all_in_password=digits_in_password+small_letters_in_password+big_letters_in_password+special_chrs_in_password
# print(all_in_password)
