import json
import pickle
input_list= []

#1) Write a short Python script which queries the 
# user for input (infinite loop with exit possibility) 
# and writes the input to a file.
def get_user_input():
    return (input('Please enter data: '))

def save_data(data):
    with open('assignment6_data.txt', mode = 'a') as f:
        f.write(str(data))
    
    

#2) Add another option to your user interface:
# The user should be able to output the data stored in the file in the terminal.
def display_data():
    print('='*50)
    print('Data Displayed from regular read')
    with open('assignment6_data.txt', mode = 'r') as f:
        data =f.read()
        print ('Entered data is: {}'.format(data))

    #4) Adjust the logic to load the file content to work with pickled/ json data.

    print('='*50)
    print('Data Displayed from pickle read')
    with open('assignment6_data_pickle.p', mode = 'rb') as f:
        data = pickle.loads(f.read())
        print ('Entered data is: {}'.format(data))

    print('='*50)
    print('Data Displayed from json read')
    with open('assignment6_data_json.txt', mode = 'r') as f:
        data_list= []
        data_list = json.loads(f.read())
        print ('Entered data is: {}'.format(data_list))
    
        
#3) Store user input in a list
# (instead of directly adding it to the file) and
#  write that list to the file – both with pickle and json.

def save_data_usingLib():
    with open('assignment6_data_pickle.p', mode = 'wb') as f:
        f.write(pickle.dumps(input_list))

    with open('assignment6_data_json.txt', mode = 'w') as f:
        f.write(json.dumps(input_list))

input_available= True
while input_available:
    print('Enter 1 for inputing data.')
    print('Enter 2 for displaying data.')
    print('Enter q to quit.')
    ch = input('Enter the choice: ')
    if ch == '1':
        data = get_user_input()
        input_list.append(data)
        save_data_usingLib()
        save_data(data)
    elif ch == '2':
        display_data()
    elif ch == 'q':
        input_available = False
    else:
        print('Please enter valid choice!')

print('User left!')
