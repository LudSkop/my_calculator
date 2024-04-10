text = 'I dont believe you. His offer seems so goot.\
      You olways say it .\
          123 it  i dont want to think about it.\
            I need it 2008.!!! >><<.'

alphabet ='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'

char_set = set()
symbol_set = set()
for el in text:
    if el.upper() in alphabet:
        char_set.add(el)
    else:
        symbol_set.add(el)


print(f'char : {char_set}')
print(f'symbol: {symbol_set}')