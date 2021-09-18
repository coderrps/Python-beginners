#if-else statements 
is_female = True #if function value is true then only it will print the if statement otherwise it will not print anything or else statement will be printed

if is_female:
    print("Yes ! You are right !")
else :
    print("No ! You are wrong !") #if is_female = false then else statement will be printed


#if statements and comparisons
def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num3 and num2>=num1:
        return num2
    else:
        return num3        

print(max_num(3, 6, 1))