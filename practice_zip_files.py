import zipfile
from pprint import pprint
from random import randint

zip_file_name = '90202836.zip'

zFile = zipfile.ZipFile(zip_file_name, 'r')
# for filename in zFile.namelist():
#     zFile.extract(filename)

# stat ={'а': {'т':500, 'х':3},
#        't':['о':100, 'у':5]}
class Chatter:

    analize_count = 0
    def __init__(self, zFile):
        self.zip_file_name = zFile
        self.stat = {}

    def unzip(self):
        zFile = zipfile.ZipFile(self.zip_file_name, 'r')
        for filename in zFile.namelist():
            zFile.extract(filename)
        return filename

    def collect(self, filename):
        prev_char = ''*Chatter.analize_count
        with open(filename, 'r', encoding='cp1251') as file:
            for line in file:
                line = line[:-1]
                for char in line:
                    if prev_char in stat:
                        if char in stat[prev_char]:
                            stat[prev_char][char] += 1
                        else:
                            stat[prev_char][char] = 1
                    else:
                        stat[prev_char] = {char: 1}
                    prev_char = char

    def prepare(self):
        totals = {}
        stat_for_gen = {}
        for prev_char, char_stat in stat.items():
            totals[prev_char] = 0
            stat_for_gen[prev_char] = []
            for char, count in char_stat.items():
                stat_for_gen[prev_char].append((char, count))
                totals[prev_char] += count
            stat_for_gen[prev_char].sort()

    def chat(self):
        n = 1000
        printed = 0
        prev_char = ' '
        spaces_printed = 0
        while printed < n:
            char_stat = stat_for_gen[prev_char]
            total = totals[prev_char]
            dice = randint(1, total)
            pos = 0
            for char, count in char_stat:
                pos += count
                if dice <= pos:
                    break
            if char == ' ':
                spaces_printed += 1
                if spaces_printed >= 10:
                    print()
                    spaces_printed = 0
            print(char, end='')
            prev_char = char
            printed += 1








pprint(stat)


pprint(stat_for_gen)

