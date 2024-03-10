import re
class StrExtension:

    @staticmethod
    def remove_vowels(value: str):
        re.
        vowls = ('a e i o u y').split()
        for vowl in vowls:
            value = value.replace(vowl, '')
        return value

    @staticmethod
    def leav_alpha(value:str):
        string = ''
        for i in value:
            if i.isalpha():
                string += i
        return string


    @staticmethod
    def raplace_all(string:str, chars, char):
        s =''
        for simbol in chars:
            string = string.replace(simbol, char)
        return string


print(StrExtension.remove_vowels('Python'))
print(StrExtension.leav_alpha('&_ljh1_)('))
print(StrExtension.raplace_all('gsdfkjlj8w0','jsg', '7'))
