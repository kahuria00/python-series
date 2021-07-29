
#accessing list items

#list indexing

companies = ["Apple","Huawei","Samsung","Infinix","Oppo","Nokia","BlackBerry"]

#positive indexing

print(companies[0]) #get first item in list


#negative indexing

print(companies[-1]) #gets last item in list


#range indexing

print(companies[2:4])# gets specified range returns new list


#checking if item in list

if 'Oppo' in  companies:
	print("Yeebo,'oppo' in companies")


#getting sum of integers in a list

list1 = [1,56,90,50,34,5,9,11]
x=sum(list1)
print(x)


# alternatively

def num_sum(items):
	sum_of_numbers = 0

	for num in items:
		sum_of_numbers += num
	return sum_of_numbers
print(num_sum([20,60,45,5,30,90]))


#or dynamically like so
user_list = [] #EMPTY LIST

user_input = int(input("how many numbers: ")) #number of list items

for num in range(user_input):
	numbers = int(input('Enter number'))
	all_num = user_list.append(numbers)
print(sum(user_list))



#deleting elements in a list

estate_listings = ['Kamulu','Ruiru','Joska',"Muchatha","Kikopey"]

del estate_listings[-2]# deletes specified index
print(estate_listings)

#alternatively

estate_listings.pop() #removes last element by default

print(estate_listings)

estate_listings.remove('Joska') 
print(estate_listings)


#removing multiple elements from list

#remove odd numbers from list

mixed_numbers = [2,45,66,13,37,49,89,7,87]

for number in mixed_numbers[:]:
	if number%2 !=0:
		mixed_numbers.remove(number)

print("Just Even:",mixed_numbers)


#remove all even using list comprehension

mixed_numbers = [2,45,66,13,37,49,89,7,87]

mixed_numbers = [num for num in mixed_numbers if num %2!=0]

print(mixed_numbers)


#MAP , FILTER and REDUCE in lists

#using Map with one Iterable/one item

classmates = ["Sassy","Jamie","Jon","Sansa","Bran","Rob","Arya"]

uppercased = list(map(str.upper,classmates))

print(uppercased)

#using Map with multiple items or iterables

circle_area = [3.567777,5.57866,4.00091,56.24421,9.909092,321.8989899,15.0867451]

all_areas = list(map(round,circle_area,range(1,7)))

print(all_areas)


#map to create zip()

my_letters =["A","B","C","D"]
my_numbers = [1,2,3,4]

results = list(map(lambda x,y:(x,y),my_letters,my_numbers))
print(results)


#Using filter

grades =[40,50,90,80,70,87,100]

def is_A_student(grade):
	return grade >75

over_75 = list(filter(is_A_student,grades))

print(over_75)


#palindrome detector with filter

names = ["rewire","madam","fluf",'alfafa',"decide"]

palindromes = list(filter(lambda word: word == word[::-1],names))
print(palindromes)





