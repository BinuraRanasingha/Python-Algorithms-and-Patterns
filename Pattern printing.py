lifelist=["The","Meaning","Of","Liff","42"]
print("\nPrac Test 1 Words:\n")
print(lifelist)
a=""

#for index in range(0,len(lifelist),1):
 #   print(index,lifelist[index])

#for index in range(0,len(lifelist),1):
 #   if index % 2 == 0:
  #      print(index,lifelist[index].upper())

for index in range(0,len(lifelist),1):
    if index % 2 != 0:
        a=lifelist[index][::-1]
        print(index,end=' ')
        for ind in range(0,len(a),1):
            if ind % 2 == 0:
                print(a[ind].lower(),end="")
        print()
               
    else:
        print(index,lifelist[index].upper())
