names=[]
x=0
while x < 10:
    acceptedName=input("next in line: ")
    names.append(acceptedName)
    x=x+1

print("\n here is the names in order of the line: ")

while len(names):
    print(names.pop(0))
