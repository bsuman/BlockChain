#1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
import copy
person_list=[]
input_waiting = True
# as each person can have multiple hobbies
i_hobbies = []

def print_names():
#2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
    print('Name list is:')
    list_name=[[el['name'] for el in person_list]]
    print(list_name)


#3) Use a list comprehension to check whether all persons are older than 20.
def check_if_old():
    return(all([int(el['age']) > 20 for el in person_list ]))

#4) Copy the person list such that you can safely
# edit the name of the first person (without changing the original list).

def edit_first_name():
    temp_person_list=copy.deepcopy(person_list[:])
    print('Temporary copied list: ')
    print(temp_person_list)
    new_name = input('Enter New Name')
    temp_person_list[0]['name'] = new_name
    print('Temporary modified list: ')
    print(temp_person_list)
    print('Unmodified original list: ')
    print(person_list)

def insert_data(i_name, i_age):
    person={'name':i_name,'age':i_age,'hobbies':i_hobbies  }
    person_list.append(person)

#5) Unpack the persons of the original list into different variables 
# and output these variables.

def unpack_dictionary():
    list_name= [[el['name'] for el in person_list]]
    print('unpacked names is ')
    print(list_name)

while(input_waiting):
    print('Enter 1 to add details')
    print('Enter 2 to just print all dictionary entries')
    print('Enter 3 to just print list of names')
    print('Enter 4 to check if the age group is above 20')
    print('Enter 5 edit first names')
    print('Enter 6 to unpack the persons of the original list')
    print('Enter "q" to Quit')
    choice = input('Enter choice')
    if choice == '1':
        print('Enter name, age, hobbies')
        i_name= input('Name: ')
        i_age= input('Age: ')
        i_hobbies= input('Hobbies: ')
        insert_data(i_name, i_age)
    elif choice =='2':
        print(person_list)
    elif choice == '3':
        print_names()
    elif choice == '4':
        if check_if_old():
            print('All persons are above 20')
        else:
            print('One or more persons are below 20')
    elif choice == '5':
        edit_first_name()
    elif choice == '6':
        unpack_dictionary()
    elif choice == 'q':
         input_waiting= False
    else:
        print('Please choose a valid option')

print('User done!')
