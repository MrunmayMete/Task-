#task 1
r = int(input("give radius of circle:"))
area_of_circle= a = ((22/7)*(r**2))
print("The area of circle is:" , a)


#task 2
file_name=fn=input("give file name:")
FN=fn.split(".")
x=(FN[1])
if x=="py":
    print("python file")
elif x == "c":
    print("c file")    
else:
    print("Invalid Extension")
input("press any key")