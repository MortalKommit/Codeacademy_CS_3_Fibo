class InvalidInputError(Exception):
    def __init__(self, msg='Number(s) out of range or invalid(non-integer)', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

def get_fibo_until(low_limit, high_limit):
    if low_limit >= high_limit or low_limit < 0 or high_limit < 1 or isinstance(low_limit, float) or isinstance(high_limit, float):
        raise InvalidInputError
    
    first_num = 0
    second_num = 1
    if low_limit >= 0:
        print(first_num)
        print(second_num)
    while first_num + second_num <= high_limit:
        next_num = first_num  + second_num
        if next_num >= low_limit:
            print(next_num)
        first_num = second_num
        second_num = next_num

def generate_new_numbers():
    regenerate = True
    while regenerate:
        try:
            lowerlimit = int(input('Enter a new number (lower limit):'))
            upperlimit = int(input('Enter a new number (upper limit):'))
            get_fibo_until(lowerlimit, upperlimit)
            regenerate = True if input('Go again?(y/n):').upper() == 'Y' else False
        except ValueError:
            print('Value must be an integer!')
    return

def check_if_fibo(number):
    if isinstance(number, float):
        raise InvalidInputError

    first_num = 0
    second_num = 1

    while first_num + second_num <= number:
        next_num = first_num  + second_num
        first_num = second_num
        second_num = next_num
    if next_num == number:
        return True
    return False

def fibo_functions():
    try:
        choice = int(input('''
        Choose an option
        1.Generate fibonacci numbers in range
        2.Check if a number belongs to finbonacci series (1/2):'''))
        while choice not in (1,2):
            print("Invalid choice")
            choice = int(input('''
        Choose an option
        1.Generate fibonacci numbers in range
        2.Check if a number belongs to finbonacci series (1/2):'''))
        if choice == 1:
            generate_new_numbers()
        else:
            number = int(input('\nEnter a number to check if it is a fibonacci number:'))
            print(check_if_fibo(number))
    except ValueError:
        print("Error: Not a valid choice, enter either 1 or 2")

        
fibo_functions()