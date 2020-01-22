Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Truthy and Falsy values
>>> bool(None)
False
>>> bool(Flase)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    bool(Flase)
NameError: name 'Flase' is not defined
>>> bool(False)
False
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool("")
False
>>> bool()
False
>>> bool[]
SyntaxError: invalid syntax
>>> bool[]
SyntaxError: invalid syntax
>>> bool([])
False
>>> bool(len())
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    bool(len())
TypeError: len() takes exactly one argument (0 given)
>>> 
