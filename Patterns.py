#Printng differnt Patterns 


'''# # # #
   # # # #
   # # # #
   # # # #'''

for i in range(4):
    for j in range(4):
        print("# ",end="")
    print()

for i in range(4):
    for j in range(i+1):
        print("# ",end="")
    print()

for i in range(4):
    for j in range(4-i):
        print("# ",end="")
    print()

for i in range(2,6):
    for j in range(1,i):
        print(j,end="")
    print()

for i in range(1,6):
    for j in range(i,5):
        print(j,end="")
    print()

a="ABCD"
for i in range(0,4):
    for j in a[i:4]:
        print(j,end="")
    print()


