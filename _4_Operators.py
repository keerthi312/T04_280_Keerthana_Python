'''
Operators 
    Operators are the symbols used in Python Programming which has it's own specific Operation

    The Types of Operators are:
    a.Arithmetic Operators - (+,-,/,*,//,%,**)

        *Addition -  (+) is the addition operator. It is used to add 2 values.
            a = 2
            b = 3
            res = a + b
            print(res)  #5
        
        *Substraction - (–) is the subtraction operator. It is used to subtract the second value from the first value.
            a = 2
            b = 3
            res = a - b
            print(res)  #-1
        
        * Multiplication -  (*) is the multiplication operator. It is used to find the product of 2 values.
            a = 2
            b = 3
            res = a * b
            print(res)  #6
        
        * Division -  (/) is the division operator. It is used to find the quotient when first operand is divided by the second.
            a = 2
            b = 3
            res = a / b 
            print(res)  #1.5
        
        * Modulus -  (%) is the modulus operator. It is used to find the remainder when first operand is divided by the second.
            a = 2
            b = 3
            res = a % b
            print(res)  #2
            
        *Floor division - (//) is used to conduct the floor division. It is used to find the floor of the quotient when first operand is divided by the second.
            a = 2
            b = 3
            res = a ** b
            print(res)  #8

    b.Relational Operators(==,<,>,<=,>=,!=)
        *Equal to: This operator returns True if both the operands are equal i.e. if both the left and the right operand are equal to each other.
            a=10
            b=20
            print(a==b) #False
    
        *Less than: This operator returns True if the left operand is less than the right operand.
            a=10
            b=20
            print(a<b)  #True
            
        * Greater than: This operator returns True if the left operand is greater than the right operand.
            a=10
            b=20
            print(a>b)  #False
            
        *Less than or equal to: This operator returns True if the left operand is less than or equal to the right operand.
            a=10
            b=20
            print(a<=b) #True
            
        *Greater than or equal to: This operator returns True if the left operand is greater than or equal to the right operand.
            a=10
            b=20
            print(a>=b) #False
                
        * Not equal to: This operator returns True if both the operands are not equal.
            a=10
            b=20
            print(a!=b) #True

    c.Logical Operators(AND,OR,NOT)

        * Logical AND: True if both the operands are true
            a=10
            b=20
            print(a and b)

        * Logical OR: True if either of the operands is true 
            a=10
            b=20
            print(a or b)
        
        * Logical NOT: True if the operand is false 
            a=10
            b=20
            print(a not b)

    d.Assigment Operator( =,+=,-=,*=,**=,//=,/=,,^=,&=,>>=,<<=)
    
        * Assignment Operator = A simple assignment operator assigns the right side operand expression or value to the left side operand.
            a=5
            b=a
            print(b)
            output:5

        * Add and Assign: This operator is used to add the right side operand with the left side operand and then assigning the result to the left operand.
            a = 3
            b = 5
            a += b
            print(a)
            Output:8
            
        *  Subtract and Assign: This operator is used to subtract the right operand from the left operand and then assigning the result to the left operand.
            a = 3
            b = 5
            a -= b
            print(a)
            Output:-2
            
        * Multiply and Assign: This operator is used to multiply the right operand with the left operand and then assigning the result to the left operand.
            a = 3
            b = 5
            a *= b
            print(a)
            Output:15
            
        *  Divide and Assign: This operator is used to divide the left operand with the right operand and then assigning the result to the left operand.
            a = 3
            b = 5
            a /= b
            print(a)
            Output:0.2
            
        * Modulus and Assign: This operator is used to take the modulus using the left and the right operands and then assigning the result to the left operand.
            a = 3
            b = 5
            a /= b
            print(a)
            Output:3
            
        * Divide (floor) and Assign: This operator is used to divide the left operand with the right operand and then assigning the result(floor) to the left operand.
            a = 3
            b = 5
            a /= b
            print(a)
            Output:0
            
        * Exponent and Assign: This operator is used to calculate the exponent(raise power) value using operands and then assigning the result to the left operand.
            a = 3
            b = 5
            a /= b
            print(a)
            Output:243
            
        * Bitwise AND and Assign: This operator is used to perform Bitwise AND on both operands and then assigning the result to the left operand.
            a = 3
            b = 5
            a &= b
            print(a)
            Output:1
            
        * Bitwise OR and Assign: This operator is used to perform Bitwise OR on the operands and then assigning result to the left operand.
            a = 3
            b = 5
            a |= 7
            print(a)
            Output:1
            
        *  Bitwise XOR and Assign: This operator is used to perform Bitwise XOR on the operands and then assigning result to the left operand.
            a = 3
            b = 5
            a ^= 7
            print(a)
            Output:6
            
        * Bitwise Right Shift and Assign: This operator is used to perform Bitwise right shift on the operands and then assigning result to the left operand.
            a = 3
            b = 5
            a >>= 7
            print(a)
            Output:0
            
        * Bitwise Left Shift and Assign: This operator is used to perform Bitwise left shift on the operands and then assigning result to the left operand.
            a = 3
            b = 5
            a >>= 7
            print(a)
            Output:96

    e.Bitwise Operators - (&,|,^,<<,>>,~)
        *Bitwise AND operator: Returns 1 if both the bits are 1 else 0.
            a=10
            b=7
            c=a&b
            print(c)
            Output:2
            
        *Bitwise or operator: Returns 1 if either of the bit is 1 else 0.
            a=10
            b=7
            c=a|b
            print(c)
            Output:15
            
        *Bitwise not operator: Returns one’s complement of the number.
            a=10
            b=~a
            print(b)
            Output:-11
        
        *Bitwise xor operator: Returns 1 if one of the bits is 1 and the other is 0 else returns false.
            a=10
            b=7
            c=a^b
            print(c)
            Output:13
            
        *Bitwise right shift: Shifts the bits of the number to the right and fills 0 on voids left( fills 1 in the case of a negative number) as a result. Similar effect as of dividing the number with some power of two.
            a=10
            b=a>>7
            print(b)
            Output:0
            
        *Bitwise left shift: Shifts the bits of the number to the left and fills 0 on voids right as a result. Similar effect as of multiplying the number with some power of two.
            a=10
            b=a>>7
            print(b)
            Output:1280

    f.Membership - In and Not In 
        *In - this operator will return true if the value is present in collection else returns false
            keer=["a","b","c","d"]
            print("a" in keer)
            Output - True
            
        *Not In - this operator will return true if the value is present in collection else returns false 
            keer=["a","b","c","d"]
            print("a"  not in keer)
            Output - False
            
    g.Identity - Is,Is Not
        *Is - this operator will compare the id of the variables of identifier if they are different return as false or else true
            a=10
            b=20
            print(a is b)
            Output - False
            
        *Is Not - this operator will not compare the id of the variables of identifier if they are different return as false or else true
            a=10
            b=20
            print(a is not b)
            Output - True
            
    h.Slicing - this operator can specify where to start the slicing, where to end, and specify the step
            Lst = [50, 70, 30, 20, 90, 10, 50]
            print(Lst[-7::1])
            Output - [50, 70, 30, 20, 90, 10, 50]
'''
