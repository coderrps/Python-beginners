#lists in python

friends = ["Gray", "Tom", "Mike", "John", "Bob"] #lists
print(friends[1]) #print that name lies in that index number
print(friends[2:4]) #print the name from index 2 to the index 3 i,e,. (n-1)
print(friends[0:]) #print all the names after that index number till end


#lists functions
 
names = ["Gray", "Tom", "Mike", "John", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Bob", "Hema", "Texas"]
lucky_numbers = [111, 2, 39, 24, 5, 69, 27]
lucky_numbers.reverse() #print the list in reversed order
lucky_numbers.sort() #print the list in alphabetical / numerical order
print(lucky_numbers)
names.extend(lucky_numbers) #add the another list to the previous list
names.append("Creed") #only one item could be inserted at a time
names.append("24") #only one item could be inserted at a time
names.insert(2, "Kelly") #insert the item at any position given as per the index number
names.remove("Tom") #to remove any element from the list
names.clear() #remove all the elements from the list and print an empty lists
names.pop() #remove the last element from the list
print(names.index("Tom")) #prints the index of that element in the list
print(names.count("Bob")) #print that how many time the element is written in the lists
names.sort() #print the elements in the alphabetical order in the lists
names2 = names.copy() #copy the names list and print as the new list
print(names2)
print(names)

#tuples
general = [(23, 4), (24, 5), (25, 6), (26, 8)] #this is how we describe tuples