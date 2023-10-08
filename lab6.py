import re

def enteredData(surname, name, childNumber):
    cond = r'^[A-z-]{3,20}$'
    cond2 = r'^\d{1,2}$'
    
    if re.match(cond, surname) and re.match(cond, name) and re.match(cond2, childNumber) :
        dataStr = f'{surname} {name} {childNumber}'
        with open("data.txt",mode = 'a', encoding = 'cp1252') as f:
            f.write(dataStr + "\n")
        
    
def outputData(file = "data.txt"):
    cond = r'\d{1,2}'
    TotalChildren = 0
    with open(file, mode = 'r', encoding = 'cp1252') as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())
            workerNumberChild  = int(re.search(cond, line).group())
            TotalChildren += workerNumberChild 
    print('The total number of children = {}'.format(TotalChildren), end = '\n\n')
    


pattern = ''

menu = """Menu:
1 - Insert data in file
2 - Read file from file 
3 - Exit"""

while True:
    print(menu)
    response = input("Choose number 1 - 3 from menu:")
    print("")
    match response:
        case "1":
            surname = input("Enter surname: ")
            name = input("Enter name: ")
            childNumber = input("Enter number of children: ")
            print("")
            enteredData(surname, name, childNumber)
        case "2":
            outputData()

        case "3":
            break
        case _:
            print("Wrong symbol. Enter value from 1-3 ")