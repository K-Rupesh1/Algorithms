# finding a number in the array
'''num=[10,20,30,40,50,55]
n=int(input("enter a number : "))
for i in range(len(num)):
    if num[i]==n:
        print(f"number found {n} ")
        break
print("number not found")'''
    
# finding a name in the array

name=["rupesh","umesh","raju","rajesh"]
n=str(input("enter a name : ")).lower()
for i in range(len(name)):
    if name[i]==n:
        print(f"name found : {n}")
        break
else:
    print(f"name not found ")