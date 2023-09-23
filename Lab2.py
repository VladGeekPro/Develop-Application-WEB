#Greeting
print('Hello, Juracovschi Vladislav. I\'m glad to meet you. ')

#Assign 4 values
Int1 = 10
_Float = 9.99
ShortString = 'Winter'
LongString = '''In the bleak midwinter, frosty wind made moan,
Earth stood hard as iron, water like a stone;
Snow had fallen, snow on snow, snow on snow,
In the bleak midwinter, long ago.'''

#Output 2 variable's type
print(type(LongString), "\n", type(Int1))

#Output string's length
print(len(LongString))

#Output string in upper format
print(ShortString.upper())

#Cut and output a part from string
Piece = LongString[7:22]
print(Piece)

#To parse the next Python code
print('\nParsing:')
txt = "More results from text..."
substr = txt[4:12]
print(substr)
print(substr.strip())

txt = "More results from text..."
print(txt.split()) 