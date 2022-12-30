
                                                         #string build in function
#------------------------------------------------------------------------------------------------------------------
a= "hey i hey i i iam jubair34"
'''
b=a.count("i")               #how many word apperce on the string 
c=len(a)                     #it count whole string 
d=a.count("hey",0,3)         #use postion to find the word 
print(b)
print(c)
print(d)
'''
'''
c=a.replace("hey","hi")   # replace one string o another string
print(c)
'''
'''
x=("hey","hi","am","jubair") # it join single string
d=''.join(x)
print(d)
print(type(x))               #i print data type
'''
'''
y=a.title()                 # it return 1st letter as capital in whole sentence  
print(y)
'''
'''
z=a.capitalize()            #it return 1st letter as capital in the sentence 
print(z)
'''
'''
b=a.index("jubair")         #it return index key of he word where it pleaced
print(b)
'''
'''
sr="jubair123"                #it return true or false bcz of it present both number and alphabet it is alphanumeric
b=sr.isalnum()
print(b)
'''
'''
a="jubair"
b=a.isalpha()
c=a.islower()
d=a.isupper()
print(b)
print(c)
print(d)
'''
'''
b="1234"
c=b.isdigit()
print(c)
'''
'''
a=["a","b","c","d"]
b=reversed(a)
for i in b:
    print(i)
'''
'''
a=("d","r","a","y","c")
b=sorted(a)
print(b)
'''
'''
a=("a","b")
b=("c","d")
c=zip(a,b)
print(tuple(c))
'''
 






                                                          #list
#--------------------------------------------------------------------------------------------------------------------------

#defination list - order collection of data item,it is mutable and changeable , it is index based data item,it allow duplicate value, it is hetergenous obiect value allowed like int,fllot,bool 
#left to right and reverse equal to right to left
#list itertion
#append
#clear
#insert
#pop
#sort
#extend

#swapping list
'''
a=[1,2,3,4,5,"jubair","hi"]
a[0]="jubair"
a[5]=1
print(a)

#remove
a.remove(1)
print(a)

#inser using index
a.insert(2,"hi")
print(a)

#update
a.insert(7,"EEE")
print(a)

a[1]='salem'
print(a)
'''
'''
#separate value list
a[2]=["salem"]
print(a)
'''
'''
#clear all value in list
#a.clear()
#print(a)
'''
'''
#index based remove
a.pop()               #it remove value from reverse [-1] or u mention any order it remove its oreder
print(a)
'''
'''
a.append('jubairskv')
print(a)

a.append('kasimjubair')
print(a)


#remove multiple value in list
del a[0:3]
print(a)

del a[2:6]
print(a)
'''
'''
from itertools import repeat
a.extend(repeat(2,4))          #2 number 4- how many time
print(a)
'''
'''
# insert multiple value in list
b=[2,3,4]
a.extend(b)
print(a)

a.sort()
print(a)

#copy and var to another var

b=a
a.copy()
print(b)

#interchabging postion
def swappostion(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
list=[2,3,4,5,"hi","jubair"]
pos1,pos2=1,6
print(swappostion(list,pos1-1,pos2-1))

# intering value using insert and pop function

list.insert(0,a.pop())
print(list)

list[2]="jubair2"
print(list)

c=[1,0,2,3,4,0,0,5,6,0,0,0,7,8]
c.sort()
print(c)
'''
#arrabe value in oneside and zero in one side
'''
c=[1,0,2,3,4,0,0,5,6,0,0,0,7,8]
g=[]
e=[]
for i in c:
    if i==0:
        g.append(i)
    else:
        e.append(i)
for j in g:        
    e.append(j)
print(e)

#swap two variable
x=1
y=2
x,y=y,x
print(x)
print(y)
print(x,y)
'''
#subarray

#def subarrauy - it is order and continous element
#-----------------------------------------------------------------------------------------------------------------------------------------------

'''                                                     #tuple
#is is order collection of data item
#it is immutable and unchangable
#it is index based data item
#it allow duplicae value
#it is hetergenous object like int,float,boolen

#itertion-convert tuple to list is possible otherwise it own return value  
a=[(1,2),(3,4),(4,5),(2,4)]
a.sort()
print(tuple(a))

a=[("jubair",1),("Gugan",2),("mano",3)]
a.sort()
print(tuple(a))

a=(1,2,3,4,5,6)
b=list(a)
b.append("jubair")
print(tuple(b))

b[0]="hi"
print(tuple(b))'''
#---------------------------------------------------------------------------------------------------------------------------------------------------

                                                   #set
#it is unorder collection of data item
#it is unchangable
#it won't allow duplicate value
#it is heterogenous object
#it is unindexed data item
# it allow modification
#string randomly change
#------------------------------------------------
#add
#remove
#clear
#update
#copy
#pop
#discard
#union
#differenece
#intresection

'''a={1,2,3,4,5,6,}
a.add("jubair")
print(a)

b={7,8,9,0}
a.update(b)
print(a)

a.pop()
print(a)

a={1,2,3,4,'hi'}
b={1,2,3,"jubair","hi"}

a.difference_update(b)   #remove b elemet
print(a)

x=a.difference(b)       #returns set x element not y element
print(x)

x=a.intersection_update(b)      
print(x)


x=a.intersection(b)    #remove same element and return reminder element only
print(x)


a.discard('jubair')                   #remove exact elemnt of the set
print(a)

a.copy()
print(a)

a={1,2,3,4}
b={5,6,7,8,9}
x=a.union(b)
print(x)

x=a.update(b)
print(x)

b.remove(9)
print(b)

a.clear()
print(a)'''

#------------------------------------------------------------------------------------------------------------------------------
                                       #dict
#it is order collection of data item
#it is mutable and changable
#it won't duplicate keys

#update
#delete
#copy
#clear
#pop
#get


d= {'chinu':2,'c':3,'a':1,'jubair':4}
print(d)
'''
d['a']=d['chinu']                          #updating key
del d['chinu']
print(d)
'''
'''
for i in d.items():                       #return all items
    print(i)

for i in d.keys():                        #return keys
    print(i)

for i in d.values():                       #return values
    print(i)

for i in d:
    if i =='a':                           #changing value
        d[i]=2
        print(d)
'''
'''        
d['jubair'] = d['a']                       #changing key
del d['a']
print(d)
'''
'''
d['a']=1
print(dict(d))
d['jubair']=4
print(dict(d))
d['a']=d['jubair']
del d['jubair']
print(dict(d))
'''
'''
d['a']= 3                                 #updating pair
print(d)
'''
'''
x=sorted(d.items())                       #ordering dict
print(dict(x))
'''
'''
del d['jubair']
print(d)

d1=d
for i in d.copy():
    print(d1)
    
x=d.get('b')                                 #getting value
print(x)

d.pop('c')                                   #remove pair
print(d)
'''
#--------------------------------------------------------------------------------------------------------
