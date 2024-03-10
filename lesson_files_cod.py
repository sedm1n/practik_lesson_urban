# Ваша задача:
# Создайте в директории проекта текстовый файл с раширением txt
# Добавьте в этот файл следующий текст
# Создайте переменную с этим файлом
# Распечатайте содержимое текстового файла в консоль
# Закройте файл
import os.path

text = """
# -*- coding: utf-8 -*-
My soul is dark - Oh! quickly string
The harp I yet can brook to hear;
And let thy gentle fingers fling
Its melting murmurs o'er mine ear.
If in this heart a hope be dear,
That sound shall charm it forth again:
If in these eyes there lurk a tear,
'Twill flow, and cease to burn my brain.

But bid the strain be wild and deep,
Nor let thy notes of joy be first:
I tell thee, minstrel, I must weep,
Or else this heavy heart will burst;
For it hath been by sorrow nursed,
And ached in sleepless silence, long;
And now 'tis doomed to know the worst,
And break at once - or yield to song.
"""

file_name = 'text.txt'
if not os.path.exists(file_name):
    file = open(file_name, 'w')
    file.write(text)
    file.close()

file = open(file_name, 'r', encoding='utf8')
txt2 = file.read()
file.close()
print(txt2)