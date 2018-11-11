names = ["Marko", "Nenad", "Zeljko", "Dejan", "Miroslav", "Darko"]
 
print()
print ("List of names and their length: ")
print()
for name in names:
    print(name + " - " + str(len(name)) + " character(s)")
 
 
print("-" * 50)
 
 
# 2) Add an if check inside the loop to only output names longer than 5 characters.
 
print()
print ("Names longer then 5 characters are: ")
print()
for name in names:
    if len(name) > 5:
        print (name)
 
 
print("-" * 50)
 
 
# 3) Add another if check to see whether a name includes a “n” or “N” character.
 
print()
print ("List of names which contain \"n\" or \"N\" character: ")
print()
for name in names:
    if "n" in name or "N" in name:
        print(name)
 
print("-" * 50)
 
 
# 4) Use a while loop to empty the list of names (via pop())
 
while len(names)>= 1:
    names.pop()
 
print(names)