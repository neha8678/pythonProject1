def say_hello():  # No Return Type and No Parameter / Argument
    # Write the Code
    print("Hello")
say_hello()


def say_hello_arg(name): #No return type with arument
    print("Hello", name)
say_hello_arg("Neha")


def say_hello_args(name, age): #No return type with Multiple aruments
    print("Hello", name, age)
say_hello_args("Neha",30)


def say_hello_arg_default(name="Neha"):  # No Return Type and No Parameter / default argument
    # Write the Code
    print("Hello", name)
say_hello_arg_default()
say_hello_arg_default("Vicky")

def sum_num_arg_return(a,b) :       #Function with an arguments
    return a + b
result=sum_num_arg_return(3, 4)
result2=sum_num_arg_return("Neha", "Patel")
print(result)
print(result2)