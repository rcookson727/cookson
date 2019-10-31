#1
def a_function(h):
    m = 0
    if h%2 == 0:
        m = 4
    else:
        m = 9
    return m

x = 0
while x <= 13:
    g = a_function(x)
    print(str(g))
    x += 3
    
print""    
#2
w = 9
while w > 2:
    w = w - 6
    print(str(w))
    w += 3

print"" 
#3

p = 0
j = [2,"g",3.1,False,"hola",4,"apples"]                
while p < 6:
    for q in j:
        if j[p] == q:
            print q
    
    p += 1

print"" 
#4
for i in range(2,15,2):
    g = i + 5
    print g

b = 2
while b<15:
    g = b + 5
    print g
    b += 2
       
     