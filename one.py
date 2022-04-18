#Donovan O'Linn

#Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 

def hello_name(user_name):
    print(f"Hello {user_name}")

#hello_name("Donovan")



# Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for number in range(0, 100):
        if number % 2 == 1:
            print(number)

#first_odds()



#Question 3: Please write a Python function, max_num_in_list to return the max number of a given list.

'''I wasn't sure if the question required a predetermined list of numbers or if you wanted the user to input the numbers themselves.
So, I created a function called create_list that allows the user to input however many numbers they want which are then saved into a list.
Once the user creates the list, it then returns the list and saves it to a_list.'''

def create_list():
    more_numbers = True
    my_list = []
    #I use a while loop to allow the user to enter in as many numbers as they wish.
    while more_numbers == True:
        my_numbers = input("What numbers would you like to add?\nWhen done, type 'done' ")
        if my_numbers.lower() == 'done':
            more_numbers = False
            break
        my_list.append(int(my_numbers))
    return my_list

# If you want to run the function, delete the # from the line below, then from the max_num_in_list() function on line 52
#a_list = create_list()


def max_num_in_list(a_list):
    current_max_number = 0
    for number in a_list:
        if number > current_max_number:
            current_max_number = number
    print(current_max_number)

#max_num_in_list(a_list)



#Question 4: Write a function to return if the given year is a leap year. The return should be boolean Type (true/false).


def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        return True
    return False


#print(is_leap_year(2000))


#Question 5: Write a function to check to see if all numbers in list are consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    a_list.sort()
    incriment = 0
    for numbers in range(a_list[0], a_list[0] + len(a_list)):
        if numbers == a_list[incriment]:
            numbers += 1
            incriment +=1
        else:
            return False
    return True


'''This question also uses the create_list() function from question three so make sure to delete the # on the line below'''
#a_list = create_list()
#print(is_consecutive(a_list))

        








