#  Crete a mondule entitled functions and insert  all functions into in
import functions as f



Text = "radar"
while ( Text ):
    f.funlambda(Text)
    Text = Text[:-1]
    print(f'\n {Text} {f.List1}')


print( f.fun2("orange", ["apple", "cherry", "peace"]))

randomNum = set(input("\nWrite random letters: "))

# Write code  if...elif...else that processes a value input by user and outputs a message
if ( len(randomNum) < 5 ): print(f"You don't know many letters, just {len(randomNum)} letters")

elif ( len(randomNum) < 7 ): print(f"I see your progress {len(randomNum)} letters ")

elif ( len(randomNum) == 9 ): print("Holy nine")

else: print(f"Wonderful, I'm proud of you! {len(randomNum)} letters")

# For 2 sequence type, pass all values using a for loop  
List1 = [1, 2, 4, 5, 6, 7, 10]
sumEven = 0

for x in range(len(List1)):  
    if x % 2 == 0: 
        sumEven += List1[x] 
    else: 
        List1[x] = 0  
print("\nResult:", sumEven, List1)


for letter in "Every morning starts with a smile":
    res = { 
    'e': "First letter is e",
    'v': "First letter is v",
    'w': "First letter is w"}.get(letter, "No desired letter") 
print(f'\n{res}\n')

# Write a code that will increament a counter using a while loop 
counter = 1
while (counter <= 6 ):
    if counter == 6:
        print("End") 
        break
    else: 
        print(f"{counter} ", end='')
        counter +=  1

# # Задание 2. Проанализируйте следующие коды Python и потом объясните какие будут результаты их интерпретирования.
# # a)
# i = sum = 0
# while i <= 4:
#     sum += i
#     i = i+1
# print(sum)
# #b)
# for char in 'PYTHON STRING':
#   if char == ' ':
#       break
#   print(char, end='')
#   if char == 'O':
#       continue
#   print('*', end='')
