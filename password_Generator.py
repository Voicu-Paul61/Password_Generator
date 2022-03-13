# TODO: Create a program that generates random passwords based on the user's chocie and save them an encrypted place in the system
from random import choices, shuffle, randint
from os import path

def create_password():
    password_string=str()
    generated_password=list()
    captalized_letters_in_password=list()
    small_letters_in_password=list()
    digits_in_password=list()
    special_chrs_in_password=list()
    number_of_characters_in_password = int()
    number_of_digits_in_password = 0
    number_of_small_letters_in_password = 0
    number_of_capitalized_letters_in_password = 0
    number_of_special_chrs_in_password = 0
    while not number_of_characters_in_password == password_len:
        if captalized_letters_exists in yes:
            number_of_capitalized_letters_in_password = randint(1, password_len)
            number_of_characters_in_password = number_of_characters_in_password + number_of_capitalized_letters_in_password
            captalized_letters_in_password=choices(captalized_letters,k=number_of_capitalized_letters_in_password)

        else:
            number_of_capitalized_letters_in_password = 0
        if small_letters_exists in yes:
            number_of_small_letters_in_password = randint(1, password_len)
            number_of_characters_in_password = number_of_characters_in_password + number_of_small_letters_in_password
            small_letters_in_password=choices(small_letters,k=number_of_small_letters_in_password)
        else:
            number_of_small_letters_in_password = 0
        if digits_exists in yes:
            number_of_digits_in_password = randint(1, password_len)
            number_of_characters_in_password = number_of_characters_in_password + number_of_digits_in_password
            digits_in_password=choices(digits,k=number_of_digits_in_password)
        else:
            number_of_digits_in_password = 0
        if special_chrs_exists in yes:
            number_of_special_chrs_in_password = randint(1, password_len)
            number_of_characters_in_password = number_of_characters_in_password + number_of_special_chrs_in_password
            special_chrs_in_password=choices(special_chrs,k=number_of_special_chrs_in_password)

        else:
            number_of_special_chrs_in_password = 0
        number_of_characters_in_password=number_of_capitalized_letters_in_password+number_of_small_letters_in_password+number_of_digits_in_password+number_of_special_chrs_in_password

    generated_password=generated_password+captalized_letters_in_password
    generated_password=generated_password+small_letters_in_password
    generated_password=generated_password+digits_in_password
    generated_password=generated_password+special_chrs_in_password
    shuffle(generated_password)
    password_string=password_string.join(generated_password)
    return password_string
def validate_password(password_length):
    x = 0
    while x == 0:
        try:
            password_length = int(input("What should the length of the password be?\n"))
            if(password_length<0):
                raise ValueError("You have to enter a valid number for the password length, it should be a whole positive number. Please try again")
            x = -1
        except ValueError as e:
            e=ValueError("You have to enter a valid number for the password length, it should be a whole positive number. Please try again")
            print(e)
            # print(
            #     "You have to enter a valid number for the password length, it should be a whole positive number. Please try again")
    return password_length
def validate_user_input(user_input, input_type):
    valid_yes_answer = ["Yes", "yes", "y", "Y"]
    valid_no_answer = ["No", "no", "n", "N"]
    any_answer = [str(x) for x in valid_yes_answer + valid_no_answer]
    possible_choices = ",".join(x for x in any_answer)
    x = 0
    while x == 0:
        try:
            user_input = input(f"Do you want {input_type} in your password\n")
            if user_input in valid_yes_answer + valid_no_answer:
                x = -1
            else:
                raise ValueError(f"That is not a valid answer. Choose between {possible_choices}. Please try again.")
        except ValueError as e:
            print(e)
    return user_input
small_letters = [chr(x) for x in range(97, 123)]
captalized_letters = [chr(x) for x in range(65, 91)]
digits = [chr(x) for x in range(48, 58)]
special_chrs = [chr(x) for x in range(33, 48)] + ([chr(x) for x in range(58, 65)]) + (
[chr(x) for x in range(91, 97)]) + ([chr(x) for x in range(123, 127)])
yes = ["Yes", "yes", "y", "Y"]
no = ["No", "no", "n", "N"]
file_name = input("What should be the name of the file where the passsword will be added?\n")
captalized_letters_exists = ""
small_letters_exists = ""
password_len = ""
digits_exists = ""
special_chrs_exists = ""
password_len = validate_password(password_len)
captalized_letters_exists = validate_user_input(captalized_letters_exists, "capitalized letters")
small_letters_exists = validate_user_input(small_letters_exists, "small letters")
digits_exists = validate_user_input(digits_exists, "digits")
special_chrs_exists = validate_user_input(special_chrs_exists, "special characters")
password=create_password()
print(password)
f_name=f"{file_name}.txt"
if not path.exists(f_name):
    with open(f_name, "w") as f:
        if(len(password)>0):
            f.write(f"{password}\n")
else:
    with open(f_name,"a") as f:
        if (len(password) > 0):
            f.write(f"{password}\n")




