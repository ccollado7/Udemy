Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/User0044/Desktop/Udemy/Automate the Boring Stuff with Python Programming/hello.py 
Hello world
What is your name?
What is your name?claudio
It is good to meet you, What is your name?claudio
The lenght of your name is:
25
What is yor age?
What is yor age?45
Traceback (most recent call last):
  File "C:/Users/User0044/Desktop/Udemy/Automate the Boring Stuff with Python Programming/hello.py", line 11, in <module>
    print("You will be", str(int(myAge) + 1), "in a year)")
ValueError: invalid literal for int() with base 10: 'What is yor age?45'
>>> 
 RESTART: C:/Users/User0044/Desktop/Udemy/Automate the Boring Stuff with Python Programming/hello.py 
Hello world
What is your name?
claudio
It is good to meet you, claudio
The lenght of your name is:
7
What is yor age?
34
You will be35in a year)
>>> 
 RESTART: C:/Users/User0044/Desktop/Udemy/Automate the Boring Stuff with Python Programming/hello.py 
Hello world
What is your name?
Claudio
It is good to meet you, Claudio
The lenght of your name is:
7
What is yor age?
34
You will be 35 in a year)
>>> 
 RESTART: C:/Users/User0044/Desktop/Udemy/Automate the Boring Stuff with Python Programming/hello.py 
Hello world
What is your name?
Claudio
It is good to meet you, Claudio
The lenght of your name is:
7
What is yor age?
34
You will be 35 in a year
>>> len("Al")
2
>>> len("Albert")
6
>>> len()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    len()
TypeError: len() takes exactly one argument (0 given)
>>> len("")
0
>>> len("Al") * 10
20
>>> str(26)
'26'
>>> int("1234")
1234
>>> float("3.1")
3.1
>>> float("3")
3.0
>>> # The input() function always return a string value. Taheke care aabout it because we can not do math with strings
>>> "26" + 1
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    "26" + 1
TypeError: can only concatenate str (not "int") to str
>>> int("26") + 1
27
>>> 27 + "years old"
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    27 + "years old"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(27) + " years old"
'27 years old'
>>> 
