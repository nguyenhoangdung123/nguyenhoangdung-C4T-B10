while True:
txt = input("Enter a year of birth? ")
print(txt)
if txt.isdigit():
    print("a number")
    break
else:
    print("not a number")

print(2018 - int(txt))