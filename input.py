#input_count = input("How many apples you want : ")
#print("your will buy " + input_count + " apples")

#write a program for adding numbers taking number from the users

num1 = input("Enter the first number : ")
num2 = input("Enter the second number : ")
count = int(num1)
count = int(num2)

print(str(num1 + num2))


apple_price = 2

# Receive the number of apples by using input(), and assign it to the input_count variable 
input_count = input("How many apples do you want?: ")

# Convert the input_count variable to an integer, and assign it to the count variable
count = int(input_count)
total_price = apple_price * count

print('You will buy ' + str(count) + ' apples')
print('The total price is ' + str(total_price) + ' dollars')