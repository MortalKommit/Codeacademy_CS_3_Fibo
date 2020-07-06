class InvalidInputError(Exception):
    def __init__(self, msg='Number out of range or invalid(non-integer)', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

def get_fibo_until(value):
    if value < 1 or isinstance(value, float):
        raise InvalidInputError
    
    first_num = 0
    second_num = 1
    print(first_num)
    print(second_num)
    
    while first_num + second_num <= value:
        next_num = first_num  + second_num
        print(next_num)
        first_num = second_num
        second_num = next_num
def generate_new_numbers():
    regenerate = True
    while regenerate:
        try:
            upperlimit = int(input('Enter a new number (upper limit):'))
            get_fibo_until(upperlimit)
            regenerate = True if input('Go again?(y/n):').upper() == 'Y' else False
        except ValueError:
            print('Value must be an integer!')
    return
generate_new_numbers()
        
