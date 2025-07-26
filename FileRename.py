import os
current = "bye.txt"
new  = "newfile.txt"
try:
    os.rename(current, new)
except FileNotFoundError:
    print(f"{current} does not Exit")
else:
    print(f"{new} is now .....")
