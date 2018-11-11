
interval_design='-'*100
comment_design = '*'*100
print(interval_design)
print(comment_design)
print('First part of the assignment')
name=input("What's your name again ?! ")
age=input("What's you age again (fake age is also okay ;)! :  ")

def print_details():
    """ function to print my details """
    print('My name is '+ name +' and my age is ' + age + '.')
    print('Now concatenated string: ' + name+age)
print_details()
print(comment_design)
print(interval_design)

print(comment_design)
print('Second part of the assignment')


def print_anydata(i1,i2):
    """ function to print any two inputs as a single string """
    print('Now concatenated data: '+ i1 +i2)


""" User enters any two input information"""
input_1 = input("Enter first data: ")
input_2 = input("Enter second data: ")
print_anydata(input_1,input_2)
print(comment_design)
print(interval_design)

print(comment_design)
print('Third part of the assignment')


def get_num_decades(num_of_years_alive):
    """ function to calculate number of decades lived 
    Arguments: 
        num_of_years_alive: number of years the user has entered as alive
    """
    return(int(num_of_years_alive/10)) 

""" user enter the number of years lived"""
years_lived = float(input ('Enter the number of years lived: '))
decade_lived = get_num_decades(years_lived)
print('Decades Lived:' + repr(decade_lived))
print(comment_design)
print(interval_design)

print(comment_design)
print('Notes on assignment')
print('Most Challenging part of the assignment')
print("1. printing string and integer value as string ( finally could use str or repr inbuilt functions) \n2. arguments of any type are printed as string after concatenating as string")
print(comment_design)
print(interval_design)
