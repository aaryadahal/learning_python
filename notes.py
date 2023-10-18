name="Hi i am Aarya Dahal."; 
print(name[0:9]);#yesma 0 dekhi 8 position samma ko character print hunxa ie "Hi i am A"
print(name[1]); # 1 positon ko print hunxa ie i
print(name[-1]); #pachadi bata 2nd position ko print hunxa ie l
print(name[-5:]); #":" pachi ya aghi kei na hunu ko artha start bata ki ta end samma ho


fname="John"; 
lname="Stones"; 
ms_1=f"[{fname} {lname}] is a famous footballer."; 
ms_2="["+fname+" "+lname+"] is a famous footballer."; 
print(ms_1);
print(ms_2);
''' we have used formatted and unformatted strings in above cases.
ms_2 is a unformatted one and ms_1 is a formatted one where f is a part of systax'''

print(len(name)); #len is used to calculate length of a string.
u_name=name.upper(); #alphahets are uppercase.
l_name=name.lower(); #alphahets are lowecase.
f_name=name.title(); #first alphabet of each word is capital.
print(u_name);
print(l_name);
print(f_name);


print(name.find("y")); #here the function finds the first A and prints its position along the line.
print(name.find("Aarya")); #here if the entire string is found, the position of 1st character is shown.
print(name.find("q")); #if the character or string is not present, it prints -1 by default.
print(name.replace("a","q")); #here al the a in the string are replaced by q.
print(name.replace("a","aa")); #it can replace character with string and vice versa
print("Aarya" in name); 
#this is an example of in function where it checks the string in given variable and prints Boolean output (True or false).
#here "Aarya" in name is a Boolean expression whose value we find using print function


import math #we now can import all the mathematical function using this line.
x=2.9; 
print(round(x));  #this is a round off function which prints the nearest integer to it.
print(abs(-2.8)); #abs() function is the modulus.
print(math.ceil(2.9)); #round function using math functions.
'''We can go to google to learn about various mathmatical function whenever we need them.'''

'''lists'''
numbers=[1,3,4,56,87,4];
print(numbers);  
numbers.append(45); #this is used to add data to a list or arrray
print(numbers);   
numbers.insert(0,4); #this puts 4 in 0th position
print(numbers); 
numbers.remove(4); #removes 4 from the list
print(numbers); 
numbers.pop(); #removes last item in list
print(numbers); 
# numbers.index(5); gives position of number in list. gives error if number not in list
# print(numbers); 
numbers.sort(); #sorts the list
print(numbers); 
numbers.reverse(); #using this after sort helps in desending sorting
print(numbers); 
number_2=numbers.copy(); #copying your list to a new one
print(f"This is in new variable={number_2}"); 
numbers.clear(); #empties the list
print(numbers); 

'''Tuple'''
numbers=(1,2,3,4); #these are constant list which can only be printed and can never be modified but can be used
 
'''Dictionaries'''#this is literally just structure from C, Just the printing method is like array.
# or can be used as an array inside an array 
numbers={
    'name':'Aarya Dahal',
    'age':45,
    'underage':False 
}
numbers["birthday"]="TODAY YOU MORON"; #adding a new data to the collection
print(numbers["name"]); 
print(numbers["birthday"]); 
print(numbers.get("name")); #another way of usin it
print(numbers.get("apple")); #prints none rather than showing error and ruining the entire program if we misplace
print(numbers.get("naem","You typed it fast")); #can provide output for placing wrong word 