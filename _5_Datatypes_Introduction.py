'''
1. What are Data Types in Python?
    The data type defines which operations can safely be performed to create, transform and use the variable in another computation.
    When a program language requires a variable to only be used in ways that respect its data type, that language is said to be strongly typed.

2. Different Datatypes in Python?
    a. Numeric          - int,float,complex
    b. Sequence Type    - string,tuple,list
    c. Boolean          - False,True
    d. Set
    e. Dictionary

a. Numeric - int,float,complex
    Int - This value is represented by int class. It contains positive or negative whole numbers
    a = 5
    print("Type of a: ", type(a))

    Float - This value is represented by float class.It is a real number with floating point representation. It is specified by a decimal point.
    b = 5.0
    print("\nType of b: ", type(b))

    Complex - Complex number is represented by complex class. It is specified as real part + imaginary part.
    c = 2 + 4j
    print("\nType of c: ", type(c))

b. Sequence Type - String,List,Tuple

    String - Strings in Python can be created using single quotes or double quotes or even triple quotes.
        . Strings are immutable
        . Strings supports slicing
        . String supports indexing
        . Strings are ordered
        . String supports duplicate items
        . String is both homogeneous and heterogeneous
        . The built-in-methods in String are given below
            capitalize()   	Converts the first character to upper case
            casefold()		Converts string into lower case
            center()		Returns a centered string
            count()		    Returns the number of times a specified value occurs in a string
            encode()		Returns an encoded version of the string
            endswith()		Returns true if the string ends with the specified value
            expandtabs()	Sets the tab size of the string
            find()		    Searches the string for a specified value and returns the position of where it was found
            format()		Formats specified values in a string
            format_map()	Formats specified values in a string
            index()		    Searches the string for a specified value and returns the position of where it was found
            isalnum()		Returns True if all characters in the string are alphanumeric
            isalpha()		Returns True if all characters in the string are in the alphabet
            isascii()		Returns True if all characters in the string are ascii characters
            isdecimal()		Returns True if all characters in the string are decimals
            isdigit()		Returns True if all characters in the string are digits
            isidentifier()	Returns True if the string is an identifier
            islower()		Returns True if all characters in the string are lower case
            isnumeric()		Returns True if all characters in the string are numeric
            isprintable()	Returns True if all characters in the string are printable
            isspace()		Returns True if all characters in the string are whitespaces
            istitle()		Returns True if the string follows the rules of a title
            isupper()		Returns True if all characters in the string are upper case
            join()		    Converts the elements of an iterable into a string
            ljust()		    Returns a left justified version of the string
            lower()		    Converts a string into lower case
            lstrip()		Returns a left trim version of the string
            maketrans()		Returns a translation table to be used in translations
            partition()		Returns a tuple where the string is parted into three parts
            replace()		Returns a string where a specified value is replaced with a specified value
            rfind()		    Searches the string for a specified value and returns the last position of where it was found
            rindex()		Searches the string for a specified value and returns the last position of where it was found
            rjust()		    Returns a right justified version of the string
            rpartition()	Returns a tuple where the string is parted into three parts
            rsplit()		Splits the string at the specified separator, and returns a list
            rstrip()		Returns a right trim version of the string
            split()		    Splits the string at the specified separator, and returns a list
            splitlines()	Splits the string at line breaks and returns a list
            startswith()	Returns true if the string starts with the specified value
            strip()		    Returns a trimmed version of the string
            swapcase()		Swaps cases, lower case becomes upper case and vice versa
            title()		    Converts the first character of each word to upper case
            translate()		Returns a translated string
            upper()		    Converts a string into upper case
            zfill()		    Fills the string with a specified number of 0 values at the beginning

    List - List in Python can be seperated by comma and denoted by Square brackets [] 
        . List is mutable
        . List supports slicing
        . List supports Indexing
        . List is ordered
        . List supports duplicate elements
        . List is both homogeneous and heterogeneous
        . List Built-in-methods are given below:
            append()	Adds an element at the end of the list
            clear()	    Removes all the elements from the list
            copy()	    Returns a copy of the list
            count()	    Returns the number of elements with the specified value
            extend()	Add the elements of a list (or any iterable), to the end of the current list
            index()	    Returns the index of the first element with the specified value
            insert()	Adds an element at the specified position
            pop()		Removes the element at the specified position
            remove()	Removes the first item with the specified value
            reverse()	Reverses the order of the list
            sort()	    Sorts the list

    Tuple - Tuple in Python can be seperated by comma and denoted by Square brackets [] 
        . Tuple is immutable
        . Tuple supports slicing
        . Tuple supports Indexing
        . Tuple is ordered
        . Tuple supports duplicate elements
        . Tuple is both homogeneous and heterogeneous
        . Tuple Built-in-methods are given below: 
            count()	Returns the number of times a specified value occurs in a tuple
            index()	Searches the tuple for a specified value and returns the position of where it was found
 
c. Boolean     
    *Boolean is a data type that is used to store two values True and False.
    *While comparing two values the expression is evaluated to either true or false.
    *It contains two keywords as True and False
    Below are the examples for booolean datatype
        *Greater Than (>)
        The condition turns TRUE if value of left operand is greater than right operand value.
        a>b

        *Less Than (<)
        The condition turns TRUE if value of left operand is lesser than right operand value.
        a < b

        *Equal to (==)
        If the value of left and right operand is same the condition turns TRUE.
        a == b

        *Not equal (!=)
        If values of two operands are not equal then the condition turns TRUE.
        a != b

        *Greater than or equal to (>=)
        The condition turns TRUE if the left operand value greater than the right operand value.
        a >= b

        *Less than or equal to (<=)
        The condition turns TRUE if the left operand value less than the right operand value.
        a <= b

        *and,	True if both are True,	x and y
        *or,	True if at least one is True,	x or y
        *not,	True only if False,	not x

d. Set 
    . Set is mutable
    . Sets doesn't supports slicing
    . Sets doesn't supports Indexing
    . Sets are unordered
    . Sets supports duplicate elements
    . Sets are both homogeneous and heterogeneous
    . Sets Built-in-methods are given below:
            add()	                        Adds an element to the set
            clear()	                        Removes all the elements from the set
            copy()	                        Returns a copy of the set
            difference()	                Returns a set containing the difference between two or more sets
            difference_update()	            Removes the items in this set that are also included in another, specified set
            discard()	                    Remove the specified item
            intersection()	                Returns a set, that is the intersection of two or more sets
            intersection_update()	        Removes the items in this set that are not present in other, specified set(s)
            isdisjoint()	                Returns whether two sets have a intersection or not
            issubset()	                    Returns whether another set contains this set or not
            issuperset()	                Returns whether this set contains another set or not
            pop()	                        Removes an element from the set
            remove()	                    Removes the specified element
            symmetric_difference()	        Returns a set with the symmetric differences of two sets
            symmetric_difference_update()	inserts the symmetric differences from this set and another
            union()  	                    Return a set containing the union of sets
            update()	                    Update the set with another set, or any other iterable

e. Dictionary
    . Dictionary is mutable
    . Dictionary doesn't supports slicing
    . Dictionary doesn't supports Indexing
    . Dictionary is unordered
    . Dictionary supports duplicate elements
    . Dictionary is both homogeneous and heterogeneous
    . Dictionary Built-in-methods are given below:
        clear()	    -	Removes all the elements from the dictionary
        copy()	    -	Returns a copy of the dictionary
        fromkeys()	-	Returns a dictionary with the specified keys and value
        get()		-	Returns the value of the specified key
        items()	    -	Returns a list containing a tuple for each key value pair
        keys()  	-	Returns a list containing the dictionary's keys
        pop()		-	Removes the element with the specified key
        popitem()	-	Removes the last inserted key-value pair
        setdefault()-	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
        update()	-	Updates the dictionary with the specified key-value pairs
        values()	-	Returns a list of all the values in the dictionary

'''