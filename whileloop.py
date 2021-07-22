n=int(input("Till which number you want multiple:"))
m=int(input("Of which number multiples should be:"))
#initiation

i=0

#execution/condition
while i<=n:
    if m>=0 :
        print(i)
        i=i+(m)

#updation/modification
    else:
        print("Invalid number")
        break
print("DONE!")