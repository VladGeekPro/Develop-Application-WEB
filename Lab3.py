# Create a list, output first and third values, and change one value 
List1 = [1, "Sun", True, 14.4, ['a','b'], {"first":"apple", 2:False}, (4,5,6)]
print(List1[0], List1[2], end='\n')

List1[1] = {2, 1, 2, 5, 1}
print(List1)


# Create type tuple, output it's type, first and last values
Tuple1 = ( {True:"Right"}, False, ["Cloud", 0] ) 
print("\nIs variable Tuple1 a tuple? ",isinstance(Tuple1, tuple),"\n", type(Tuple1), end='\n')
print(f'{Tuple1[0]}  {Tuple1[-1]}')
print()
#Create type set with repeated symbols
Text = 'Life is worthy don\'t waste your time'
Set1 = set(Text)
print(f'\n{Set1}', end='\n')

Set2 = { 1, 2, 1, 3, 2}
print(Set2)


# Create two dictionaries. One with string keys, another with numeric keys. Output at least two elements from every dictionary
ListStringKey = ['First','one']
ListStringKey2 = ['Second','two']
Dict1 = dict([ListStringKey, ListStringKey2])
print('\n'+ Dict1['First'], Dict1['Second'], sep="  ", end='\n')


Dict2 = {0 : False , 1 : True}
print(Dict2[0], Dict2[1], sep='  ')

# Change previous type in another one. Give example, where it can be useful
StrNum1 = "10"
StrNum2 = "10"
Sum = int(StrNum1) + int(StrNum2)
print(f'\nResult = {Sum}',"\n", type(Sum))


#  Create two lists: one for product names and the second for their price. Use the format method to output values from these lists
ProductNames = ["Orange", "Banana", "Kiwi"]
ProductPrices = [10, 12, 14]
Info = '''\nProducts information:
{} : {}
{} : {}
{} : {}'''

print(Info.format(ProductNames[0],ProductPrices[0],ProductNames[1],ProductPrices[1],ProductNames[2],ProductPrices[2] ))


# Let the user to enter their age. Convert it to an int, use operator assign, concatination and arithmetic.  
Age = int( input ("Enter your age: "))
Age += 5
print('After 5 years, you will be ' + str(Age) + " years old")


# Use operators in and not in
Var1 = 'cats'
SimpleText =  'People that like cats are so cute!'
Animals = ['elephant', 'dog', 'kiwi', 'butterfly']

if Var1 in SimpleText:
    print('\nI found it')

if 'lion' not in Animals:
    print('Unfortunately this animal wasn\'t found in the list of animals')
