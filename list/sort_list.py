mylist = ["Orange", "apple", "Banana", "Kiki", "pineaple", "mango"]
# mylist.sort()
# print(mylist)
# mylist.sort(reverse=True)
# print(mylist)
mylist.sort(key=str.lower)
print(mylist)

mylist = [100, 200, 300, 400]
mylist.sort
print(mylist)
mylist.sort(reverse=True)
print(mylist)


def myfunc(n):
    return abs(n - 60)


mylist = [100, 50, 60, 88]
mylist.sort(key=myfunc)
print(mylist)

mylist= ["sengohng","dara","panha","Seyha"]
mylist.reverse
print(mylist)