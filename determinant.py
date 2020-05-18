import copy
from fractions import Fraction

listoflists = []
list = []
for i in range(0,10):
    list.append(i)
    if len(list)>3:
        list.remove(list[0])
        listoflists.append((list, list[0]))


def numeric_compare(alist1, alist2):

    list1 = alist1[0]
    list2 = alist2[0]

    alist1[0].sort()
    alist2[0].sort()

    if len(list1) > len(list2):
        return 1
    elif len(list1) < len(list2):
        return -1
   
    for i in range(0,len(list1)):
        if list1[i] != list2[i]:
            return list1[i] - list2[i]

    return 0

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

list1 = [4,4,8]
list2 = [1,2,3]
list3 = [1,3,9]
alist1 = [list1,-1]
alist2 = [list2,1]
alist3 = [list3,-7]
listoflists = [alist1,alist2,alist3]

listoflists.sort(key=cmp_to_key(numeric_compare))


# The following multiply is for determinant function
# Example varlist = [6, 2]

def multiply(onelist,varlist):
  for i in range(0,len(onelist)):
      partlist1 = (onelist[i])[0]
      partlist1.append(varlist[0])
      partlist1.sort()
      (onelist[i])[1] = (onelist[i])[1] * varlist[1]
      
  return onelist

varlist = [6, 2]
n = multiply(listoflists,varlist)


def determinant2(col1,col2):
    list1 = [col1[0],col2[1]]
    list2 = [col1[1],col2[0]]
    list1.sort()
    list2.sort()
    alist1 = [list1,1]
    alist2 = [list2,-1]
    listoflists = [alist1,alist2]
    return listoflists

def determinant3(col1,col2,col3):
    # To compute the first component
    s11 = [col2[1],col2[2]]
    s12 = [col3[1],col3[2]]
    v1 = [col1[0],1]
    listoflists = multiply(determinant2(s11,s12),v1)

    # To compute the second component
    s21 = [col1[1],col1[2]]
    s22 = [col3[1],col3[2]]
    v2 = [col2[0],-1]
    listoflists =  listoflists + multiply(determinant2(s21,s22),v2)

    # To compute the third component
    s31 = [col1[1],col1[2]]
    s32 = [col2[1],col2[2]]
    v3 = [col3[0],1]
    listoflists =  listoflists + multiply(determinant2(s31,s32),v3)
    
    return listoflists

def determinant4(col1,col2,col3,col4):
    # To compute the first component
    s11 = [col2[1],col2[2],col2[3]]
    s12 = [col3[1],col3[2],col3[3]]
    s13 = [col4[1],col4[2],col4[3]]
    v1 = [col1[0],1]
    listoflists = multiply(determinant3(s11,s12,s13),v1)

    # To compute the second component
    s21 = [col1[1],col1[2],col1[3]]
    s22 = [col3[1],col3[2],col3[3]]
    s23 = [col4[1],col4[2],col4[3]]
    v2 = [col2[0],-1]
    listoflists =  listoflists + multiply(determinant3(s21,s22,s23),v2)

    # To compute the third component
    s31 = [col1[1],col1[2],col1[3]]
    s32 = [col2[1],col2[2],col2[3]]
    s33 = [col4[1],col4[2],col4[3]]
    v3 = [col3[0],1]
    listoflists =  listoflists + multiply(determinant3(s31,s32,s33),v3)

    # To compute the fourth component
    s41 = [col1[1],col1[2],col1[3]]
    s42 = [col2[1],col2[2],col2[3]]
    s43 = [col3[1],col3[2],col3[3]]
    v4 = [col4[0],-1]
    listoflists =  listoflists + multiply(determinant3(s41,s42,s43),v4)
    
    return listoflists

col1 = [1, 2, 3, 4]
col2 = [5, 6, 7, 8]
col3 = [9, 10, 11, 12]
col4 = [13, 14, 15, 16]
n = determinant4(col1,col2,col3,col4)
n.sort(key=cmp_to_key(numeric_compare))

def multiplypoly(list1,list2):
    t = []
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            p = (list1[i])[0] + (list2[j])[0]
            s = (list1[i])[1] * (list2[j])[1]
            t.append([p,s])
    return t

# To combine like terms for a list
# example of list: [[[1, 4],-1],[[1, 8],1]]

def merge(list):

    #print(f'list={list}')
    list.sort(key=cmp_to_key(numeric_compare),reverse=True)

    #print(f'after list={list}')
   
    p = list[0]
    r = []
    for i in range(1,len(list)):
        c = list[i]
        
        if c[0] == p[0]:
            temp = copy.deepcopy(c)
            
            temp[1] = temp[1] + p[1]
            
            p = temp
        elif p[1] != 0:
            r.append(p)
            p = copy.deepcopy(c)
        else: p = copy.deepcopy(c)

    # To process the last element in the list
    if i== len(list)-1:
        if c[0] == p[0]:
            
            if p[1] != 0:
                r.append(p)
        else:
                r.append(c)

    #print(f'r is {r}')
    return r

def initial_u(x):
    listu = []
    for i in range(0,x):
        listu.append([])
    return listu


# Given two lists, return long - short
# For example long =[1,2,2] short= [1,2,3], return [2]

def diflist(short,long):
    tmp = copy.deepcopy(long)
    for k in short:
        if k in tmp:
            tmp.remove(k)
    return tmp

# check if the short list is a sublist of long
# assume that two lists are sorted integers

def sublist(short,long):

    short.sort()
    long.sort()

    #print(f'short={short}')
    #print(f'long={long}')
    
    if (len(long) < len(short)):
        return False
    
    i = 0
    j = 0

    while i<len(short):
        if short[i]==long[j]:
            i += 1
            j += 1
            if j==len(long) and i<len(short):
                return False
        elif short[i]<long[j]:
            return False
        else:
            j += 1
            if j==len(long):
                return False

    return True
        

# return -1 if no leading powerproduct of fi can divide h
# otherwise return the minimal f index number

def dividable(listf,h):

    h.sort(key=cmp_to_key(numeric_compare),reverse=True)
    lph = (h[0])[0]
    for i in range(0,len(listf)):
        listf[i].sort(key=cmp_to_key(numeric_compare),reverse=True)
        lpf = ((listf[i])[0])[0]
        if sublist(lpf,lph):
            return i

    return -1

# This function is used in Buchberger algorithm
# to generate the initiative pairs for all polynomials f
def generatePairs(F):
    P = []
    for i in range(0,len(F)):
        for j in range(i+1,len(F)):
          P.append([F[i],F[j]])
    return P

# Input: F = {f1,f2,...}, output: G={g1,g2,...} a Grobner basis for F
def Buchberger(F):
    G = copy.deepcopy(F)
    Pairs = generatePairs(F)
    while len(Pairs)>0:
        p = Pairs.pop(0)
        s= Spolynomial(p[0],p[1])
        #print(f'p[0]={p[0]}')
        #print(f'p[1]={p[1]}')
        #print(f's={s}')
        h = reduce(s,G)
        #print(f'h={h}')
        if len(h)>0:
            for i in range(0,len(G)):
                Pairs.append([G[i],h])
            G.append(h)
    
    return G

# compute the S-polynomial of f and g
def Spolynomial(f,g):
    f.sort(key=cmp_to_key(numeric_compare),reverse=True)
    g.sort(key=cmp_to_key(numeric_compare),reverse=True)
    listf=f[0]
    listg=g[0]
    
    dif1 = diflist(listf[0],listg[0])
    c1 = listg[1]

    dif2 = diflist(listg[0],listf[0])
    c2 = listf[1]
        
    nf= multiplypoly([[dif1,c1]],f)
    ng= multiplypoly([[dif2,-c2]],g)
    
    return merge(nf+ng)

# Reduce algorithm
# Input f and listf including f1,f2,...fn
# Output r is reduced with respect to (f1,f2,...fn) with respect to
# f = u1f1 + ... + unfn + r

def reduce(f, listf):
    listu = initial_u(len(listf))
    r = []
    h = copy.deepcopy(f)
    times = 0
    
    #while len(h)>0 and times<=1000:
    while len(h)>0:
        times += 1
        if times%1000 == 0:
            print(times)
            #print(f'listf={listf}')
            #print(f'h={h}')
    
        d = dividable(listf,h)
        #print(f'listf={listf}')
        #print(f'h={h}')
        if times%1000 == 0:
            print(f'd={d}')
            print(f'listf={listf[d]}')
        if d != -1:
            diflp = diflist(((listf[d])[0])[0],(h[0])[0])
            #c = (h[0])[1] / ((listf[d])[0])[1]
            c = Fraction((h[0])[1], ((listf[d])[0])[1])
            listu[d].append([diflp,c])
            h += multiplypoly(listf[d],[[diflp,-c]])
            h = merge(h)
            if times%1000 == 0:
                print(f'Match h={h}')
        else:
            r.append(h[0])
            del h[0]
            if times%1000 == 0:
                print(f'Cannot match h={h}')
    #print(f'u={listu[0]}') 
    return r

 
# Convert ID to the column list for generation of columns in Determinant generation
# the id starts from 0.
# For example, if id =1, size =3, then the returned list is [3,4,5]

def id2Column(id,size):
    r = []
    for i in range(0,size):
        r.append(i+id*size)
    return r

def generate_determinant2(i1,i2):
    t1=id2Column(i1,2)
    t2=id2Column(i2,2)
    return determinant2(t1,t2)

def generate_determinant3(i1,i2,i3):
    t1=id2Column(i1,3)
    t2=id2Column(i2,3)
    t3=id2Column(i3,3)
    return determinant3(t1,t2,t3)


f1 = generate_determinant3(1,4,5)
f2 = generate_determinant3(3,4,6)
f3 = generate_determinant3(5,2,6)
f4 = generate_determinant3(7,4,2)
f5 = generate_determinant3(7,5,3)
f6 = generate_determinant3(7,6,1)

F = [f1,f2,f3,f4,f5,f6]

#print(f2)
B=Buchberger(F)
print(f'Grobner basis inludes {len(B)} elements.')
for i in range(0,len(B)): 
    print(f'E{i}: {B[i]}')


#f3 = generate_determinant2(1,2)
#f4 = generate_determinant2(0,3)
#f = merge(multiplypoly(f3,f4))
#print(f)
#print(reduce(f, B))


#f1 = [[[2,2],1],[[1,2],1],[[1,1],1]]
#f2 =  [[[1],1],[[2],1]]
#f3 =  [[[2],1]]
#f1 = [[[1],1],[[2],1],[[5],1],[[6],1]]
#f2 =  [[[3],1],[[4],1],[[5],1],[[6],1]]
#f3 =  [[[1],1],[[2],1],[[7],1],[[8],1]]
#f4 =  [[[3],1],[[4],1],[[7],1],[[8],1]]
#f5 =  [[[5],1],[[6],1],[[7],1],[[8],1]]


#f1 = [[[4],1],[[5],1],[[6],1]]
#f2 =  [[[7],1],[[8],1],[[9],1]]
#f3 =  [[[2],1],[[4],2],[[9],1]]
#f4 =  [[[2],1],[[6],1],[[7],1]]
#f5 =  [[[4],3],[[1],1],[[8],1]]
#f6 =  [[[5],1],[[1],2],[[7],1]]
#f7 =  [[[5],1],[[3],1],[[9],1]]
#f8 =  [[[3],1],[[6],1],[[8],1]]
#F = [f1,f2,f3,f4,f5,f6,f7,f8]

"""
f1 = [[[4],1],[[5],1],[[1],3]]
f2 =  [[[4],1],[[3],1],[[6],1]]
f3 =  [[[2],1],[[5],2],[[6],1]]
f4 =  [[[1],1],[[6],1],[[7],1]]
f5 =  [[[3],4],[[5],1],[[7],1]]
f6 =  [[[2],1],[[4],1],[[7],4]]
#f7 = [[[5],1],[[11],2],[[9],1]]
#f8 =  [[[6],1],[[10],1],[[9],1]]
#f9 =  [[[5],1],[[8],3],[[10],1]]
#f10 =  [[[6],1],[[8],2],[[11],1]]
#f11 =  [[[2],1],[[8],1],[[9],2]]
#f12 =  [[[2],3],[[11],1],[[10],2]]
#F = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12]
F = [f1,f2,f3,f4,f5,f6]
B=Buchberger(F)
print(f'Grobner basis inludes {len(B)} elements.')
for i in range(0,len(B)): 
    print(f'E{i}: {B[i]}')
"""

#print(Spolynomial(f1,f2))

#f1 = [[[3,1],2],[[2,1],1],[[1],1]]
#f2 =  [[[1, 1],1],[[2],-1]]
#listf = [f1]
#f = [[[3,3,2,1],1],[[3,2,1],4],[[2,2,1],-3]]

#print(f'reminder is {reduce(f, listf)}')

#print(dividable(listf,h))

short = [1,2]
long = [1,1,2,3,3]

#print(diflist(short,long))

