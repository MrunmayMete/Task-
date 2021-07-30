string1=input("enter a word ")
import collections
a={}
for x in string1:
    if x in a.keys():
        a[x]+=1
    else:
        a[x]=1
sorted_dict = dict( sorted(a.items(),
                            key=lambda item: item[1],
                            reverse=True))
print("Processed output: ", sorted_dict)