def validate_args(func):
    def wrapp(*args):

        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"   
        
        arg = args[0]  

        if not isinstance(arg, int):
            return "Wrong types" 
          
        if arg < 0:
            return "Negative argument" 
        
        return func(*args)
    return wrapp

@validate_args
def example_function(x):
    return x

print(example_function(1))  
print(example_function(1, 2)) 
print(example_function())   
print(example_function("text"))  
print(example_function(-1))  