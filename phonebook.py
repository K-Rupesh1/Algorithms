"""names=["rupesh","umesh","rajesh"]
numbers=[6302686906,7337546283,8106467475]
phone=list(zip(names,numbers))
#print(phone)
name=input("name : ").lower()
#BY using range function
'''for i in range(len(phone)):
    if names[i]==name:
        print(f"{names}")
        break
else:
    print("not found")'''
#By using in function
for person,number in phone:
    if person==name:
        print(f"{person}:{number}")
        break
else:
    print("not found")"""
    
# BY Using Dictionary
phone={"rupesh":6302686906,"umesh":7337546283,"rajesh":8106467475}
name=input("enter a name : ").lower()
if name in phone:
    print(f"{name}:{phone[name]}")
else:
    print("Not Found")