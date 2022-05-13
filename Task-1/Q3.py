# COGNIZANCE
# DOMAIN : AI
# TASK 1


# QUESTION 3

f=open("about.txt","r")
r=f.read()
s=r.split(' ')
d={}
lst=[]
count=0
c=''
for j in range(len(s)):
    for char in s[j]:
        if char.isalpha():
            c=c+char
        else:
            continue
    s[j]=c
    c=''


for i in range(len(s)):
    if len(s[i])>=6:
        lst.append(s[i])
    if s[i] not in d:
        d[s[i]]=count
    if s[i] in d:
        d[s[i]]+=1

list_6=[]
for i in lst:
    if i not in list_6:
        list_6.append(i)

print("Words with atleast 6 letters")  
print()      
for i in list_6:
    print(i)
    
freq=0
keys=''
for i in d:
    if d[i]>freq:
        freq=d[i]
        keys=i

print()        
print("The most frequent word:",keys)




        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

