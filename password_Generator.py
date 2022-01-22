#TODO: Create a program that generates random passwords based on the user's chocie and save them an encrypted place in the system
from random import choices, shuffle
from os import path
small_letters=[chr(x) for x  in range(97,123)]
captalized_letters=[chr(x) for x  in range(65,91)]
digits=[chr(x) for x  in range(48,58)]
special_chrs=[chr(x) for x  in range(32,48)]+([chr(x) for x  in range(58,65)])+([chr(x) for x  in range(91,97)])+([chr(x) for x  in range(123,127)])
file_name=input("What should be the name of the file where the passsword will be added?\n")
password_len=input("What should the length of the password be?\n")
captalized_letters_max=input("How many capitalized letters in the password at maximum\n")
small_letters_max=input("How many small letters in the password at maximum\n")
digits_max=input("How many digits in the password at maximum?\n")
special_chrs_max=input("How many special characters in the password at maximum?\n")
