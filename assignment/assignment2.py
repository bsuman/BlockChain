#1) Create a list of names and use a for loop to output the length of each name (len() ).
""" list of name initialization"""
name_list=[]
is_user_input_available = True

def get_user_choice():
    return input('Choice:')


def get_user_input_name():
    return input('Enter the name:')


def print_user_name_len():
    for name in name_list:
        #2) Add an if  check inside the loop to only output names longer than 5 characters.
        #3) Add another if  check to see whether a name includes a “n”  or “N”  character.

        if len(name) > 5 and ('n'in name or 'N' in name):
            print ('Name is:'+ name +' having length greater than 5 and contains letter n or N')
        
def add_name_to_list(name):
    name_list.append(name)


#4) Use a while  loop to empty the list of names (via pop() )
def empty_name_list():
    while len(name_list) > 0:
        popped_name = name_list.pop()
        print('The name popped from the list is '+ popped_name)


while is_user_input_available:
    print('Enter 1 to add a name to the list')
    print('Enter 2 to print the length of each name in the list')
    print('Enter e to pop each name in the list')
    print('Enter q to quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        name = get_user_input_name()
        add_name_to_list(name)
    elif user_choice == '2':
        print_user_name_len()
    elif user_choice == 'e':
        empty_name_list()
    elif user_choice == 'q':
        is_user_input_available = False
    else:
        print('Please make a valid choice!')
print('********User left!********')
