n=input()
m=input()
print("Operator :",end=" ")
operator=input()
if int(n)>= int(m) and operator=="+":
  dash=len(n)+2
  for i in range(2):
    print(" ",end="")
  print(n) 
  print("+",end="")
  for i in range(dash-len(m)-1):
    print(" ",end="")
  print(m)  
  for i in range(dash-1):
    print("-",end="")
  print("-")  
  sum=int(n)+int(m)
  sum=str(sum)
  for i in range(dash-len(sum)):
    print(" ",end="")
  print(sum)  

if int(n)>= int(m) and operator=="-":
  dash=len(n)+2
  for i in range(2):
    print(" ",end="")
  print(n) 
  print("-",end="")
  for i in range(dash-len(m)-1):
    print(" ",end="")
  print(m)  
  for i in range(dash-1):
    print("-",end="")
  print("-")  
  sum=int(n)-int(m)
  sum=str(sum)
  for i in range(dash-len(sum)):
    print(" ",end="")
  print(sum)   

if int(n)<int(m) and operator=="+":
  dash=len(m)+2
  for i in range(dash-len(n)):
    print(" ",end="")
  print(n)
  print("+",end="")  
  for i in range(dash-len(m)-1):
    print(" ",end="")
  print(m)
  for i in range(dash-1):
    print("-",end="")
  print("-")
  sum=int(n)+int(m)
  sum=str(sum)
  for i in range(dash-len(sum)):
    print(" ",end="")
  print(sum)

if int(n)<int(m) and operator=="-":
  dash=len(m)+2
  for i in range(dash-len(n)):
    print(" ",end="")
  print(n)
  print("-",end="")  
  for i in range(dash-len(m)-1):
    print(" ",end="")
  print(m)
  for i in range(dash-1):
    print("-",end="")
  print("-")
  sum=int(n)-int(m)
  sum=str(sum)
  for i in range(dash-len(sum)):
    print(" ",end="")
  print(sum)  