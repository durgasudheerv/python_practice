print("hello world, python is working")
print(3 + 4)
print("the result of 3 // 4 is", 4 // 2)
print("the result of 3 / 4 is", 2 ** 4)
print("hello i am charan")
print("the result of 2 + 3 is", 5)
print('charan is a good boy')
print('charan is a god\'s "boy"') # this will print: charan is a god's
print('charan' + 'charan')# this will concatenate the two strings
print('charan ' * 10) # this will print 'charan ' 10 times
print(r'c:\charan\newfile') # this will print the path without treating \n as a newline character
x =5
y = 10
x+y
print("the result of x + y is", x + y)
print("the result of x * y is",x * y)
'''
#PS F:\python_practice\python_practice> 2+3
5
PS F:\python_practice\python_practice> _+5
_+5 : The term '_+5' is not recognized as the name of a cmdlet, function, script file, or operable program. 
At line:1 char:1
+ _+5
+ ~~~
    + CategoryInfo          : ObjectNotFound: (_+5:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS F:\python_practice\python_practice> _ + 5
_ : The term '_' is not recognized as the name of a cmdlet, function, script file, or operable program. 
At line:1 char:1
+ _ + 5
+ ~
    + CategoryInfo          : ObjectNotFound: (_:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS F:\python_practice\python_practice> python
Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> 10 + 6
16
>>> _ + 5
21
>>> XYZ
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    XYZ
NameError: name 'XYZ' is not defined
>>> xyz =10
>>> xyz+5
15
>>> _ + 20
35
>>> name ='cha_h'
>>> name
'cha_h'
>>> name + lock
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name + lock
           ^^^^
NameError: name 'lock' is not defined
>>> name + 'lock'
'cha_hlock'
>>> name[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name[5]
    ~~~~^^^
IndexError: string index out of range
>>> name[0]
'c'
>>> name[-1]
'h'
>>> name[-2]
'_'
>>> name = hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = hello
           ^^^^^
NameError: name 'hello' is not defined. Did you mean: 'help'?
>>> name ='hello'
>>> name[0]
'h'
>>> name[-1]
'o'
>>> name[-2]
'l'
>>> name[1:2]
'e'
>>> name[0:2]
'he'
>>> name[0:]
'hello'
>>> hey + name[0:]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    hey + name[0:]
    ^^^
NameError: name 'hey' is not defined. Did you mean: 'hex'?
>>> 'he'+ name[0:]
'hehello'
>>> my_name ="no name"
>>> len(my_name)
7
'''

###### tuple practice ####
s = (1, 2, 3, 4, 5)
print(s[0]) # this will print the first element of the tuple
print(s[-1]) # this will print the last element of the tuple
print(s[1:4]) # this will print the elements from index 1 to 3 (4 is not included)
print(s.count(5)) # this will count the occurrences of 5 in the tuple
print(s.index(3)) # this will print the index of the first occurrence of 3 in the tuple
#s[0] = 10 # this will raise an error because tuples are immutable
'''TypeError: 'tuple' object does not support item assignment
'''

######### set practice ######

print("**********set practice******")
s = {1, 11,55,22,44,55,56,66}
print(s) # this will print the set, duplicates will be removed
print(55 in s) # this will check if 55 is in the set
print(100 in s) # this will check if 100 is in the set
s.add(100) # this will add 100 to the set
print(s) # this will print the set with 100 added
s.remove(11) # this will remove 11 from the set
print(s) # this will print the set with 11 removed
s.copy() # this will create a copy of the set
print(s) # this will print the original set
print(s.difference({22, 44})) # this will return a new set with elements that are in s but not in the given set
print(s.intersection({55, 56, 66})) # this will return a new set with elements that are common in both sets
print(s.union({77, 88})) # this will return a new set with all elements from both sets
print(s.isdisjoint({99, 100})) # this will check if s has no elements in common with the given set
print(s.issubset({1, 55, 56, 66, 100})) # this will check if s is a subset of the given set
print(s.issuperset({1, 55})) # this will check if s is a superset of the given set                              