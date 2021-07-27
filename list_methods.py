
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


