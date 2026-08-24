# We modify any kind of function using decorators.
# For example , we need to greet anyone "Good Morning" and after completion we need to greet by saying "Thankyou for using this function" , then we will use decorator
# We will use "greet decorator" and then we need to make a function named "greet" , which will take any function as an input and return the same function as an output.



#defining function

def greet(fx):      #it will take function as an input
    def mfx():      #again we will define a function mfx i.e. modified fx
        print("Good Morning")
        fx()        #Function calling
        print("Thanks for using this function")
    return mfx      #using mfx it will display the message "Good morning" and "Thanks for using this function"

@greet      # Here we call greet and then we will call the function.

def hello():
    print("Hello World !")

hello()