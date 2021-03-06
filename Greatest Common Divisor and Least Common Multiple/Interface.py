from main import Calculator

while True:
    print("""
______________________________________________________________________________
 Calculator: Enter 2 or more whole numbers separated by spaces.
        """)
    user_input = input(" Plz type in your calc: ")
    print("")

    try:
        user_input = user_input.strip().split()
        user_input = tuple(map(int, user_input))

        for index, _ in enumerate(user_input):
            temp_message = [x for x in [Calculator().factor(_) for _ in user_input]]
            print(f' Prime factors: {_}  = {temp_message[index]}')

    except TypeError:
        print("TypeError: Only integers are allowed")
    except ValueError:
        print("ValueError: Only integers are allowed")
    except ZeroDivisionError:
        print("ZeroDivisionError: Sorry, no numbers below zero")

    else:
        print("")
        temp_message = ' * '.join(str(x) for x in Calculator().prime_factorization_lcm(*user_input))
        print(f' The least common multiple: {temp_message} = {Calculator().lcm(*user_input)} ')
        temp_message = ' * '.join(str(x) for x in Calculator().prime_factorization_gcd(*user_input))
        print(f' The greatest common divisor: {temp_message} = {Calculator().gcd(*user_input)} \n ')
        further_calc = input(f" Do you want to make any further calc?:[y/n] ")

        if further_calc.lower()[0] == "y" or "yes":
            continue
        else:
            break
