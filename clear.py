# Запис у файл байтових рядків таробота з різними кодуваннями.
from pathlib import Path

text =' Привіт потік GOIT 19!'
print(text.encode())

print(text.encode('utf-16'))
print(text.encode('cp1251'))

cod = b' \xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82 \xd0\xbf\xd0\xbe\xd1\x82\xd1\x96\xd0\xba GOIT 19!'

print(cod.decode())

cod_2 = b'\xff\xfe \x00\x1f\x04@\x048\x042\x04V\x04B\x04 \x00?\x04>\x04B\x04V\x04:\x04 \x00G\x00O\x00I\x00T\x00 \x001\x009\x00!\x00'
print(cod_2.decode('utf-16'))

cod_3 = b' \xcf\xf0\xe8\xe2\xb3\xf2 \xef\xee\xf2\xb3\xea GOIT 19!'
print(cod_3.decode('cp1251'))



