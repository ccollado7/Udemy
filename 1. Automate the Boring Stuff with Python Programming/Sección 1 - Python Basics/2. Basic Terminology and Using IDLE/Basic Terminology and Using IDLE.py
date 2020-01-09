Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#Operaciones algebraicas basicas en python. Se puede utilizar como calculadora
>>> 2 + 2 #Suma
4
>>> 2
2
>>> 5 - 2 #Resta
3
>>> 3 * 7 #Producto
21
>>> 3 x 7 #El producto no se realiza por medio de la x....
SyntaxError: invalid syntax
>>> 22 / 7 #Division en punto flotante 
3.142857142857143


#Operaciones algrbraicas agrupadas. Para todos los casos se utiliza la procedencia tipica de operaciones algebraicas

>>> 2 + 3 * 6
20
>>> (2 + 3) * 6
30
>>> (5 - 1) * ((7 + 1) / (3 - 1))
16.0
>>> 4 * ((7 + 1) / (3 - 1))
16.0
>>> 4 * (8 / (3 - 1))
16.0
>>> 4 * (8 / 2)
16.0
>>> 4 * 4.0
16.0
>>> 5 + #Falta un componente de la operacion algebraica, por lo tanto dara error
SyntaxError: invalid syntax

>>> -2 #Entero negativo
-2
>>> 30 #Entero positivo
30 
>>> 3.14 #Punto flotante
3.14
>>> 42
42
>>> 42.0
42.0

#Strings

>>> "Hello World"
'Hello World'
>>> "Alice" + "Bob" #Concatenacion de strings
'AliceBob'
>>> "Alice" * 3
'AliceAliceAlice'
>>> "Hello" + "!" * 10
'Hello!!!!!!!!!!'

# Variables (asignacion)

>>> spam = 42
>>> spam
42
>>> spam "Hello" #Error por falta del operador de asignacion =
SyntaxError: invalid syntax
>>> spam = "Hello"
>>> spam + "World" #Concatenacion de una variable con un string explicito
'HelloWorld'
>>> spam + " World"
'Hello World'
>>> spam = "Goodbye"
>>> spam + "World"
'GoodbyeWorld'
>>> 
>>> 
>>> 
>>> spam = 2 + 2
>>> spam
4
>>> spam = 10 
>>> spam = spam + 1 
>>> 
