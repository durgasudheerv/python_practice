dic = {1: 'one',2: 'two',3: 'three'}
print(dic.get(1))
print(dic.get(4)) # this will return None because 4 is not a key in the dictionary
print(dic.get(4, 'not found')) # this will return 'not found' because
# 4 is not a key in the dictionary and we provided a default value
print(dic.get(1, 'not found'))
# this will return 'one' because 1 is a key in the dictionary and we provided a default value
company_keys = ['name', 'employs', 'ctc', 'location']
details = ['google', 100000,'1lakh','visakhapatnam']
company = dict(zip(company_keys,details))
print(company)
# Output: {'name': 'google', 'employs': 100000, 'ctc': '1lakh', 'location': 'visakhapatnam'}
print(company['name']) # this will print 'google'
#  this will print 100000....
print(company['employs']) 
# this will print '1lakh'....
print(company['ctc'])
# this will print 'visakhapatnam'....
print(company.get('name')) # this will print 'google'
print(company.get('employs')) # this will print 100000      
print(company.get('ctc')) # this will print '1lakh'
print(company.get('location')) # this will print 'visakhapatnam'
print(company.get('ceo', 'not found')) # this will print 'not found'

govt_exam = {'names':['upsc','ssc','bank clerk','railway','police'],
             'qualifications':['graaduation','intermediate','graduation','intermediate','intermediate'], 
                'age limits':[32, 30, 27, 28, 30]}
print(govt_exam.get('names'))
#this will print ['upsc', 'ssc', 'bank clerk', 'railway', 'police'] because 'names' is a key in the dictionary and its value is a list of government exam names
print(govt_exam.get('qualifications'))
#this will print ['graaduation', 'intermediate', 'graduation', 'intermediate', 'intermediate'] because 'qualifications' is a key in the dictionary and its value is a list of qualifications for different government exams
print(govt_exam.get('age limits'))
# this will print [32, 30, 27, 28, 30]
print(govt_exam.get('slary', 'not found')) # this will print 'not found'
print(govt_exam)
# output {'names': ['upsc', 'ssc', 'bank clerk', 'railway', 'police'], 'qualifications': ['graaduation', 'intermediate', 'graduation', 'intermediate', 'intermediate'], 'age limits': [32, 30, 27, 28, 30]}

#sub dictionary
bus ={'name':{'garuda':{'price': 'very costly','reach':'ontime'},'surya':{'price': 'moderate','reach':'moderate'},'reddies':{'price': 'cheap','reach':'late'}}}
print(bus)
# output {'name': {'garuda': {'price': 'very costly', 'reach': 'ontime'}, 'surya': {'price': 'moderate', 'reach': 'moderate'}, 'reddies': {'price': 'cheap', 'reach': 'late'}}}
print(bus.get('name').get('garuda').get('price'))
# this will print 'very costly' because 'name' is a key in the dictionary and its value is another dictionary that contains 'garuda' as a key, which in turn has 'price' as a key with the value 'very costly'
print(bus.get('name').get('surya').get('reach'))
# this will print 'moderate' because 'name' is a key in the dictionary and its value is another dictionary that contains 'surya' as a key, which in turn has 'reach' as a key with the value 'moderate' 
print(bus.get('name').get('reddies').get('price'))
# this will print 'cheap' because 'name' is a key in the dictionary and its value is another dictionary that contains 'reddies' as a key, which in turn has 'price' as a key with the value 'cheap'
print(bus.get('name').get('reddies').get('reach'))      
# this will print 'late' because 'name' is a key in the dictionary and its value is another dictionary that contains 'reddies' as a key, which in turn has 'reach' as a key with the value 'late'
print(bus.get('name').get('reddies').get('rating','not found'))
# this will print 'not found' because 'name' is a key in the dictionary and


## below are varibles to know about the memory location and type of the variable
##tags which are used to identify the memory location of the variable and the type of the variable
## based data values are stored in the memory location and the variable name
#  is just a reference to that memory location
# when we assign a value to a variable, 
# Python creates an object in memory to 
# hold that value and assigns the variable name to
# reference that object. The id() function can be used to 
# get the memory address of the object that a variable references, 
# and the type() function can be used to get the type of the object.
'''''
>>> g = 10
>>> g
10
>>> h = 5
>>> h
5
>>> id(h)
140725343048744
>>> id(g)
140725343048904
>>> h =g
>>> id(h)
140725343048904
>>> k = 10
>>> id(k)
140725343048904
>>> type(k)
<class 'int'>
>>> PI =13.5
>>> PI
13.5
>>> type(PI)
<class 'float'>
>>> 
'''''


#######data_types####
''''
>>> type(PI)
<class 'float'>
>>> none k
  File "<stdin>", line 1
    none k
         ^
SyntaxError: invalid syntax
>>> k
10
>>> type(k)
<class 'int'>
>>> c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> k =2.5
>>> type(k)
<class 'float'>
>>> l =55
>>> k =l
>>> type(k)
<class 'int'>
>>> c= float(k)
>>> c
55.0
>>> int(c)
55
>>> g = c+k
>>> g
110.0
>>> jh =g + jk
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    jh =g + jk
            ^^
NameError: name 'jk' is not defined. Did you mean: 'k'?
>>> jh =g+ik
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    jh =g+ik
          ^^
NameError: name 'ik' is not defined. Did you mean: 'k'?
>>> in =2+j5
  File "<stdin>", line 1
    in =2+j5
    ^^
SyntaxError: invalid syntax
>>> num =5+kj
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    num =5+kj
           ^^
NameError: name 'kj' is not defined. Did you mean: 'k'?
>>> num =5+6j
>>> type(num)
<class 'complex'>
>>> c = complex(5,5)
>>> c
(5+5j)
>>> list = [55,55,66,22,55]
>>> range(10)
range(0, 10)
>>> list(range(10))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    list(range(10))
    ~~~~^^^^^^^^^^^
TypeError: 'list' object is not callable
>>> 5>k
False
>>> l =6>5
>>> l
True
>>> type(l)
<class 'bool'>
>>> int(l)
1
>>> float(l)
1.0
>>> l =(10,20,30,5,5)
>>> l
(10, 20, 30, 5, 5)
>>>  j ={55 , 6 , 8 , 68,55}
  File "<stdin>", line 1
    j ={55 , 6 , 8 , 68,55}
IndentationError: unexpected indent
>>>  j ={55,6,8,68,55}      
  File "<stdin>", line 1
    j ={55,6,8,68,55}
IndentationError: unexpected indent
>>>  j = {55,6,8,68,55}
  File "<stdin>", line 1
    j = {55,6,8,68,55}
IndentationError: unexpected indent
>>>  j = {55, 6, 8, 68, 55}
  File "<stdin>", line 1
    j = {55, 6, 8, 68, 55}
IndentationError: unexpected indent
>>> j = {55, 6, 8, 68, 55}
>>> j
{8, 68, 6, 55}
>>> list(range(10))  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    list(range(10))
    ~~~~^^^^^^^^^^^
TypeError: 'list' object is not callable
>>> del list
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10,2)) 
[2, 4, 6, 8]
>>> list(range(0,10,2))
[0, 2, 4, 6, 8]
>>> list(range(0,10,1))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(0,10,5))
[0, 5]
>>> list(range(0,10,3))
[0, 3, 6, 9]
>>> str ="charan"
>>> str
'charan'
>>> type(str)
<class 'str'>
>>> f ='f'
>>> str(f)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    str(f)
    ~~~^^^
TypeError: 'str' object is not callable
>>> type(f)
<class 'str'>
>>> 
'''
