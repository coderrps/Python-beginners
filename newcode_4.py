#functions

def sayhi():
    print("Hello, world!")
    word = input("Please say a word:")

print("Welcome User")
sayhi()
print("Bye User!")

#new function
def say_hi(name, age):
    print("Hello " + name + ", You are " + age)

say_hi("Ritu", "19")
say_hi("Shradha", "20")

#using string instead of putting the direct value
def say_hi(name, age):
    print("Hello " + name + ", You are " + str(age))

say_hi("Ritu", 19)
say_hi("Shradha", 20)


#creating your own function with return statements
def quad(num):
    return num*num*num*num
def pent(num):
    return num*num*num*num*num
    print("hello") #it's not gonna print this

print(quad(2)) #printing the function in one line

result = pent(3) #we can print the function like this also
print(result)