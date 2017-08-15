def decrypt(word):
  i=0
  list1 = list(word)
  list2 = []
  for x in list1:   
    if i > 0:
      p = ord(list2[-1]) + ord(x)
      while p >123:
        p = p-26
      list2.append(chr(p))      
    else:
      list2.append(chr(ord(x)+1))
      i = 1
  return(str(list2))
  

a = decrypt("crime")
print(a)
a = decrypt("encyclopedia")
print(a)
