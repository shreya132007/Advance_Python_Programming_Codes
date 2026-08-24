#For example , we are adding any 2 numbers and for that we need to pass arguments
# So for this , we need to use *args and **kwargs
# *args - means taking arguments as a tuple
# **kwargs - means taking argumnets as a dictionary (key value pairs)

def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx  


# @greet  # we will use another method here to call decorator

def add(a,b):
    print(a+b)
    
greet(add)(4,6)