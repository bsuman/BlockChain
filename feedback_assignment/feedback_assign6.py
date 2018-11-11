import json as j
import pickle as p
 
waiting_for_quit = True
 
 
while waiting_for_quit:
    print('Please choose')
    print('1 - Wanna write something - json')
    print('2 - Wanna write something - pickle')
    print('3 - Output - json')
    print('4 - Output - pickle')
    print('q - Exit')
    
    user_choice = input('Choose: ')
    
    if user_choice == '1':
        with open('file_exercise.txt', mode='w') as f:
            text = input('Write something: ')
 
            list = []
            list.append(text)
            
            #with json
            f.write(j.dumps(list))
            f.write('\n')
    elif user_choice == '2':
        with open('file_exercise.p', mode='wb') as f:
            text = input('Write something: ')
 
            list = []
            list.append(text + '\n')
            #with pickle
            f.write(p.dumps(list))
    elif user_choice == '3':
        with open('file_exercise.txt', mode='r') as f:
            print(f.read())
    elif user_choice == '4':
        with open('file_exercise.p', mode='rb') as f:
            print(p.loads(f.read()))
    elif user_choice == 'q':
        waiting_for_quit = False
else:
    print('Exit')  