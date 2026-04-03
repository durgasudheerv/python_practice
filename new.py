def add_two_numbers(a, b):
    return a + b

# Example usage
result = add_two_numbers(5, 3)
print(result)  # Output: 8
'''''
PS F:\python_practice\python_practice> 2+3
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
>>> num =[10,20,30,40]
>>> num
[10, 20, 30, 40]
>>> len(my_name)      
7
>>> num = [10,88,11,2,55,0,66]
>>> num
[10, 88, 11, 2, 55, 0, 66]
>>> strings = [ff ,ff]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    strings = [ff ,ff]
               ^^
NameError: name 'ff' is not defined
>>> strings = ['fuck' 'blast']
>>> strings                   
['fuckblast']
>>> strings = ['fuck', 'blast']
>>> strings 
['fuck', 'blast']
>>> mix = ['love', 25 ,'no use']
>>> mix
['love', 25, 'no use']
>>> len mix
  File "<stdin>", line 1
    len mix
        ^^^
SyntaxError: invalid syntax
>>> mix    
['love', 25, 'no use']
>>> num[0]                    
10
>>> num0:]
  File "<stdin>", line 1
    num0:]
         ^
SyntaxError: unmatched ']'
>>> num[0:]
[10, 88, 11, 2, 55, 0, 66]
>>> num[0:2]
[10, 88]
>>> num[-4]
2
>>> max =[num ,mix]
>>> max
[[10, 88, 11, 2, 55, 0, 66], ['love', 25, 'no use']]
>>> num append(10)
  File "<stdin>", line 1
    num append(10)
        ^^^^^^
SyntaxError: invalid syntax
>>> python3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    python3
NameError: name 'python3' is not defined
>>> num
[10, 88, 11, 2, 55, 0, 66]
>>> num.append(10)
>>> num
[10, 88, 11, 2, 55, 0, 66, 10]
>>> num.remove(0)
>>> num
[10, 88, 11, 2, 55, 66, 10]
>>> num.pop(0)
10
>>> num
[88, 11, 2, 55, 66, 10]
>>> num.pop()
10
>>> num
[88, 11, 2, 55, 66]
>>> num.pop()
66
>>> num
[88, 11, 2, 55]
>>> num.remove(2)
>>> num
[88, 11, 55]
>>> num.append(25)
>>> num
[88, 11, 55, 25]
>>> num.insert(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    num.insert(0)
    ~~~~~~~~~~^^^
TypeError: insert expected 2 arguments, got 1
>>> num.insert(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    num.insert(10)
    ~~~~~~~~~~^^^^
TypeError: insert expected 2 arguments, got 1
>>> num.insert(2,22)
>>> num
[88, 11, 22, 55, 25]
>>> num.insert(3,28)
>>> num
[88, 11, 22, 28, 55, 25]
>>> num.remove(88)
>>> num
[11, 22, 28, 55, 25]
>>> num.pop(1)
22
>>> num
[11, 28, 55, 25]
>>> del num[0]
>>> num
[28, 55, 25]
>>> del num[2:]
>>> num
[28, 55]
>>> num.extend([55,2,6,9,88,55,66,1,5])
>>> num
[28, 55, 55, 2, 6, 9, 88, 55, 66, 1, 5]
>>> min(num) 
1
>>> max(num)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    max(num)
    ~~~^^^^^
TypeError: 'list' object is not callable
>>> min(num)
1
>>> max(num)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    max(num)
    ~~~^^^^^
TypeError: 'list' object is not callable
>>> del max
>>> max
<built-in function max>
>>> max(num)
88
>>> sum(num)
370
>>> num.sort()
>>> num
[1, 2, 5, 6, 9, 28, 55, 55, 55, 66, 88]
>>> del mix
>>> mix
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    mix
NameError: name 'mix' is not defined. Did you mean: 'max'?
>>> sel num[0:5]
  File "<stdin>", line 1
    sel num[0:5]
        ^^^
SyntaxError: invalid syntax
>>> del num[0:5]
>>> num
[28, 55, 55, 55, 66, 88]
>>> mix
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    mix
NameError: name 'mix' is not defined. Did you mean: 'max'?
>>>  
'''