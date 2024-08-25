print("hello")

a=25
b="dark"
c=0.7
d=True
print(type(a))

# convert int into float

e=float(8)
print(e)

# no sizes for list list means array
list=[56,32,678]
print(list[2])

list.append(253)
print(list)

x=10
print(x==2)
print(x==10)
print(x<20)

# its interpeter language its means case sentive (space) its do line by line run panum and drowback is first line erro will be show and then next 

if x==10:
    print("x is eqal")
else:
    print("x is not eqal")
    j=10
    print(j)

# loop statementes
name=['dark','love','dk']
# abc namba create panra own name
for abc in name:
    print(abc)

for l in range(5):
    print(l)

# start and stop
for n in range(6,12):
    print(n)
# 2 mean i+2 
for w in range(10,20,2):
    print(w)

x=1
while x<10:
    print(x)
    x=x+1 #increment python la there is no increment and decrement like this i++ i--

#function declearation
def myfunction():
    print("hello")

myfunction() #function calling 

def add(o,p):
    return o+p

print(add(67,9))

g=add(89,9)
print(g)

dic={
    'name':'dharshu',
    'age':20,
    'city':'erode'
}

print(dic)
#particullary Value

print(dic['age'])

#add
dic['state']='tn'
print(dic)

#users value get

num =int(input())
print(num)

dic['name']=input()
print(dic)