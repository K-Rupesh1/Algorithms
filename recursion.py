def draw(height):
    if height<=0:
        return 
    draw(height-1)
    for i in range(height):
        print("#",end="")
    print(" ")
n=int(input("height :"))
draw(n)