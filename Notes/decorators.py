
def cough(func):
    
    def func_wrapper():
        #stuff that happens before function
        print("*cough*")

        func()

        #stuff that happens after function
        print("*cough*")

    return func_wrapper


@cough
def awkward():
    print("Can I get a discount?")

@cough
def answer(): 
    print("This is a dollar tree...")


awkward()
answer()
