#TODO: Create a program that generates random passwords based on the user's chocie and save them an encrypted place in the system
from random import choices, shuffle
from os import path
small_letters=[chr(x) for x  in range(97,123)]
captalized_letters=[chr(x) for x  in range(65,91)]
numbers=[chr(x) for x  in range(48,58)]
special_chrs=[chr(x) for x  in range(32,48)]+([chr(x) for x  in range(58,65)])+([chr(x) for x  in range(91,97)])+([chr(x) for x  in range(123,127)])
