# Читання та запис у файл.

file = open('folder/folder_2/clear.txt',mode='a',encoding='utf-8')
file.write('Hello word\n')
file.write('Hello love\n')
file.writelines('Hi Vlad\n' 'Hi Oleg\n' 'Hi Alisa\n')
file.close()


file = open('clear.txt', mode='r', encoding='utf-8')
a = file.readlines()
print(a)
file.close()




