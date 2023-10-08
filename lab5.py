# def additionProduct( shoppingList, product):
#     if product not in shoppingList:
#         shoppingList.append(product)
#     else:
#         print(f"{product} is already added in shopping list", end = '\n\n')
#     return shoppingList

# def deleteProduct(shoppingList, product):
#     if product in shoppingList:
#         while (product in shoppingList):
#             shoppingList.remove(product)
#     else: print(f"Shopping list doesn't contain {product}", end = '\n\n')

# def printList(shoppingList):
#     if not shoppingList:
#         print("Shopping list is empty", end = '\n\n')
#     else:
#         output = ", ".join(shoppingList)
#         print(f"Shopping list = {output}.", end = '\n\n')

# def additionProductDict( shoppingList, product):
#     if product not in shoppingList.values():
#         shoppingList[len(shoppingList) + 1] = product
#     else:
#         print(f"{product} is already added in shopping list", end = '\n\n')
    

# def deleteProductDict(shoppingList, product):
#     prodRemove = [key for key, value in shoppingList.items() if value == product]
#     if prodRemove:
#         for key in prodRemove:
#             del shoppingList[key]
#     else: print(f"Shopping list doesn't contain {product}", end = '\n\n')

# def printListDict(shoppingList):
#     if not shoppingList:
#         print("Shopping list is empty", end = '\n\n')
#     else:
#         output = ", ".join(shoppingList.values())
#         print(f"Shopping list = {output}.", end = '\n\n')

def additionProductSet( shoppingList, product):
    if product not in shoppingList:
        shoppingList.add(product)
    else:
        print(f"{product} is already added in shopping list", end = '\n\n')

def deleteProductSet(shoppingList, product):
    if product in shoppingList:
        shoppingList.remove(product)
    else: print(f"Shopping list doesn't contain {product}", end = '\n\n')

def printSet(shoppingList):
    if not shoppingList:
        print("Shopping list is empty", end = '\n\n')
    else:
        output = ", ".join(shoppingList)
        print(f"Shopping list = {output}.", end = '\n\n')


Menu = """Menu:
1 - Print list
2 - Add item
3 - Delete item
4 - Exit"""

shoppingList = set()

while True:
    print(Menu)
    response = input("\nEnter a value from 1 - 4:")

    match response:
        case "1":
            printSet(shoppingList)
        case "2":
            addProduct = input("Enter a product:")
            additionProductSet( shoppingList, addProduct)
        case "3":
            delProduct = input("Enter a product to delete from shopping list:")
            deleteProductSet(shoppingList, delProduct)
        case "4":
            break
        case _:
            print("Wrong symbol, enter from 1 - 4", end = '\n\n')
            