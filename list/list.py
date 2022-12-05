mylist = ["sengonh", "senghong2", "senghong3"]
print(mylist)


list1 = ['dara', 'panha', 'kakada']
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = [True, False, False]

print(list1+list2+list3)

this_list = list(("snegonh", "dara"))
print(this_list)

# List Item
print('===================================')

thisList = ["apple", "banana", "Orange", "dara", "name", "Flower"]
print(thisList[2: 5])
print(thisList[: 5])
print(thisList[4:])
print(thisList[-4:-2])

if "apple" in thisList:
    print("Yes , 'apple' is in the Lists")


# change list
listA = ["apple", "banana", "Orange"]
listA[1] = "Has Chnaged"
print(listA)

listA[1:2] = ["blackcurrant", "watermelon"]
print(listA)

listA.insert(2, "Dara new insert")
print(listA)

# Add list Item #?append() for add item to end of list
listA.append("Orange")
print(listA)

listA.insert(1, "has been added")
print(listA)

thisList = ["apple", "Orange", "Chery"]
tropical = ["mango", " pineaple", "papaya"]
thisList.extend(tropical)
print(thisList)

# Remove lists Item

listA.remove("apple")
print(listA)

# ?The pop() method removes the specified index
listA.pop(1)
print(listA)

# ?The del keyword can also delete the list completely.
ListB = [1, 3, 4, 5, 67, 4, 6, 4, 56]
del ListB[1]
# print(ListB)

# ? The clear() method empties the list.
# ListB.clear()
# print(ListB)

# ?You can loop through the list items by using a for loop:

for x in ListB:
    print(x)

# ?Use the range() and len() functions to create a suitable iterable.
ListB = ["sengonf", "Lise", "test", "EMMEME"]
for i in range(len(ListB)):
    print(ListB[i])

# ?Print all items, using a while loop to go through all the index numbers
print("==============")
thisList = ["Senghong", "Dara", "Seyha"]
i = 0
while i < len(thisList):
    print(thisList[i])
    i = i + 1

# ?List Comprehension

fruits = ["apple", "banana", "cherry", "Kiki", "Mango"]
newList = []
for x in fruits:
    if "a" in x:    
        newList.append(x)
print(newList)

# this shot
newList = [x for x in fruits if "a" in x]
print(newList)

newList = [x for x in fruits if x!="apple"]
print(newList)

newList = [x for x in range(10)]
print(newList)

newlist = [x for x in range(10) if x < 5]
print(newList)

newList = [x.lower() for x in fruits]
print(newList)
newList = [x.upper() for x in fruits]
print(newList)

newlist = ['Hello' for x in fruits]
print(newlist)

newlist = [x if x !='banana' else "Orange" for x in fruits ]
print(newlist)
