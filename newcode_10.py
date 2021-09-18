#for loops
friends = ["Jim", "karen", "Kevin"]
for friend in friends:
    print(friend)
    
for letter in "Amsterdam Academy":
    print(letter)

for index in range(2, 5):
    print(index)  

for index in range(len(friends)): #prints the number of elements in the list
    print(friends[index]) 
    friends[2]     

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")        