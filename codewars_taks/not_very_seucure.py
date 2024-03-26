import re
from string import punctuation, whitespace
def alphanumeric(password:str):
    # punctuation_chars = re.escape(punctuation+whitespace)
    # pattern = re.compile(f'[{punctuation_chars}]')
    # if password is None or re.search(pattern,password):
    #     return False
    # return True
    return password.isalnum()

print(alphanumeric("hello34234world"))



