'''
Variables

1. What are Variables?
    Variables are containers for storing data values. 
    The name given during memory allocation
    Python has no command for declaring a variable.
    A variable is created the moment you first assign a value to it.

    x = 5
    y = "keer"
    print(x)    #5
    print(y)    #keer
----------------------------------------------------------------------------------------------------------------------

2. x = 10. Explain in detail for CRUD operations
	Create      - To Create the data (#x = 10)
	Retrieve    - Retrieve or Select the data (#print(x))
	Update      - Update or Modify the data (#x = 20)
	Delete      - Delete the data (#del x)
-----------------------------------------------------------------------------------------------------------------------

3. Tokens in Python. Explain all types
Tokens a very basic component of the source code. Characters are classified by four major categories:

1.	Keyword: Keywords are words that have some special meaning or significance in a programming language. They can’t be used as variable names, function names, or any other random purpose. They are used for their special features. In Python we have 33 keywords some of them are: try, False, True, class, break, continue, and, as, assert, while, for, in, raise, except, or, not, if, elif, print, import, etc.

2.	Identifier: Identifiers are the names given to any variable, function, class, list, methods, etc. for their identification.

3.	Literal:Literals are the fixed values or data items used in a source code. Python supports different types of literals such as:
(i) String Literals     : The text written in single, double, or triple quotes represents the string literals in Python. For example: “Computer Science”, ‘sam’, etc.
(ii) Character Literals : Character literal is also a string literal type in which the character is enclosed in single or double-quotes. a = 'G', b = "W"
(iii) Numeric Literals  : These are the literals written in form of numbers. Python supports the following numerical literals:
        *Integer Literal: It includes both positive and negative numbers along with 0. It doesn’t include fractional parts. It can also include binary, decimal, octal, hexadecimal literal.
        *Float Literal  : It includes both positive and negative real numbers. It also includes fractional parts.
        *Complex Literal: It includes a+bi numeral, here a represents the real part and b represents the complex part.
(iv) Boolean Literals   : Boolean literals have only two values in Python. These are True and False.
(v) Special Literals    : Python has a special literal ‘None’. It is used to denote nothing, no values, or the absence of value.
(vi)Literals Collections: Literals collections in python includes list, tuple, dictionary, and sets.
------------------------------------------------------------------------------------------------------------------------

4.	Operator: 
These are the tokens responsible to perform an operation in an expression. The variables on which operation is applied are called operands.
-------------------------------------------------------------------------------------------------------------------------

3. Garbage collection. How it works internally
    Python deletes unwanted objects automatically to free the memory space.
    The process by which periodically frees and reclaims the blocks of memory that no longer are in use is called garbage collection
-----------------------------------------------------------------------------------------------------------------------

4. Memory Management in Python
    Memory management in Python involves a private heap containing all Python objects and data structures.
    The management of this private heap is ensured internally by the Python memory manager.
-----------------------------------------------------------------------------------------------------------------------

5. Dynamically typed programming. Explain examples.
    We don't have to declare the type of variable while assigning a value to a variable in Python.
    Other languages like C, C++, Java, etc.., there is a strict declaration of variables before assigning values to them.
    It states the kind of variable in the runtime of the program. So, Python is a dynamically typed language
-----------------------------------------------------------------------------------------------------------------------

6. Initializing variable, static,dynamic way
Static typing:
    Static means that the types are known and checked for correctness before running your program. This is often done by the language compiler.
    int number = 1
    string name = "keer"
    string output = string(number)+name // =1keer

Dynamic typing:
    Dynamic Means that types are only known as your program is running
    number = 1
    name = "keer"
    output = number + name// = 1keer
----------------------------------------------------------------------------------------------------------------------

7. Assigning value to multiple variables. Explain
    Python allows you to assign values to multiple variables in one line:
    Example: x, y, z = "Orange", "Banana", "Cherry"
    And you can assign the same value to multiple variables in one line:
    Example: x = y = z = "Orange"
----------------------------------------------------------------------------------------------------------------------

15. Scope of variable. Explain about LEGB rule?
        Every object in Python functions within a scope. A scope is a block of code where an object in Python remains relevant. Namespaces uniquely identify all the objects inside a program. However, these namespaces also have a scope defined for them where you could use their objects without any prefix. A few examples of scope created during code execution in Python are as follows:
        A local scope refers to the local objects available in the current function.
        A global scope refers to the objects available throughout the code execution since their inception.
           -- L, Local — Names assigned in any way within a function (or lambda), and not declared global in that function.
                a = 10
                def function():
                  print(“Hello”)
                function()
                print(a)
                Output - Hello
                         10
                         
           -- E, Enclosing-function locals — Name in the local scope of any and all statically enclosing functions(or lambdas), from inner to outer.
                Msg = “This is declared globally”
                def function():
                    print(Msg)
                function()
                Output:This is declared globally

           -- G, Global (module) — Names assigned at the top-level of a module file, or by executing a global statement in a def within the file.
                msg = “global variable”
                def function():
                  msg = “local variable”
                  print(msg)
                function()
                print(msg)
                Output:
                local variable
                global variable
                
           -- B, Built-in (Python) — Names preassigned in the built-in names module : open, range,SyntaxError, etc.
                def vehicle():
                  fun= “Start”
                  def car():
                    model= “Toyota”
                    print(fun)
                    print(model)
                  car()
                vehicle()
                Output:
                Start
                Toyota
------------------------------------------------------------------------------------------------------------------------
'''
