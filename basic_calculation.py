def calculate (num1, num2, operator):
    if operator == 'add' : 
        return num1 + num2
    elif operator == 'minus' : 
        return num1 - num2
    elif operator == 'times' : 
        return num1 * num2
    else : 
        return num1 // num2

def convert (x, func = None) :
    if func == None : 
        return x
    else : 
        operator, value = func
        return calculate(x, value, operator)

def zero(func=None):
    return convert(0, func)
        
def one(func=None): 
    convert(1, func)
def two(func=None): 
    return convert(2, func)
    
    
def three(func = None): 
    return convert(3, func)
def four(func = None):
    return convert(4, func)
def five(func = None):
    return convert(5, func)
def six(func = None):
    return convert(6, func) 
    #your code here
def seven(func = None):
    return convert(7,func) #your code here
def eight(func = None): 
    return convert(8, func)
def nine(func =None): 
    return convert(9, func)
def plus(func = None): 
    if func == None :
        return ('add', 0)
    else : 
        value = func
        return ('add', value)
    
    
def minus(func = None): 
    if func == None :
        return ('minus', 0)
    else :  
        value = func
        return ('minus', value)
def times(func = None): 
    if func == None :
        return ('times', 0)
    else : 
        value = func
        return ('times', value)
def divided_by(func =None):
    if func == None :
        return ('divided_by', 0)
    else : 
        value = func
        return ('divided_by', value)

#create 5 test cases 

print (seven(times(five()))) # must return 35
print (four(plus(nine()))) # must return 13
print (eight(minus(three()))) # must return 5
print (six(divided_by(two()))) # must return 3
zero(plus(five()))
print (5//7)