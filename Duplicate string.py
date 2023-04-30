import array as arr
s1=input("enter tthe sting ")
s=set()
for i in range(0,len(s1)):
    s.add(s1[i])
l=list(s);
a=arr.array('u',l)
for i in range(0,len(a)-1):
    if(i!=len(a)):
          print(a[i] ,"," ,end=" ");
    else:
        print(a[i],end=" ");

