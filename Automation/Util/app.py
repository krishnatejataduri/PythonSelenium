import importlib.util
import string
from time import sleep
import threading
import datetime
import random
from numpy import array
import json


def vol(rad):
    return (4 / 3) * (22 / 7) * (rad ** 3)



def ran_check(num, low, high):
    return num in range(low, high)


def up_low(your_sentence):
    d = {'upper': 0, 'lower': 0}
    for item in your_sentence:
        if item.isupper():
            d['upper'] += 1
        elif item.islower():
            d['lower'] += 1
        else:
            pass
    print(f"Original string has {d['upper']} upper case and {d['lower']} lower case characters.")


#  up_low('Hello, How are you Babe?')

def unique_list(input_list):
    my_list = [input_list[0]]
    for item in input_list:
        if item not in my_list:
            my_list.append(item)
    return my_list


#  print(unique_list([1,1,2,3,4,4,5,5,6,7,8,9,9]))

def multiply(numbers):
    product = 1
    for item in numbers:
        product = product * item
    return product


#  print(multiply([1,2,3,-4]))

def pangram(s):
    alphabet = string.ascii_lowercase
    for item in s.lower():
        if item in alphabet:
            alphabet.strip(item)
    return len(alphabet) == 0


#  print(pangram("The quick brown fox jumps over the lazy dog"))

def printer():
    spec = importlib.util.spec_from_file_location("Functions.Function_Library",
                                                  "C:\\Users\\krishna.teja.taduri\\Desktop"
                                                  "\\Functions\\Function_Library.py")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    func_lib_class_name = 'Function_Library'
    my_method = 'print_me'

    exec(f'foo.{func_lib_class_name}().{my_method}()')


#  printer()

def waiting_function(thread_name, lock):
    lock.acquire()
    print(f"This is Thread {thread_name}")
    sleep(10)
    print(f"Waited for Thread {thread_name}")
    lock.release()


def multi_threading():
    lock = threading.Lock()
    thread1 = threading.Thread(target=waiting_function, args=('Thread 1', lock))
    thread2 = threading.Thread(target=waiting_function, args=('Thread 2', lock))
    thread1.start()
    thread2.start()


#multi_threading()


def year_100():
    input('Enter your name: ')
    age = input('Enter your age: ')
    years_to_100 = 100 - int(age)
    current_year = datetime.date.today().year
    print(f"You are going to turn 100 in {current_year + years_to_100}")


#  year_100()

def odd_even():
    if int(input('Enter a number: ')) % 2 == 0:
        print('Number is even')
    else:
        print('Number is odd')


# odd_even()

def print_less_than_5():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in my_list:
        print(num if num < 5 else 0)


# print_less_than_5()

def print_divisors():
    my_num = int(input("Enter a number: "))
    divisor = 1
    while divisor <= my_num / 2:
        if my_num % divisor == 0:
            print(divisor)
        divisor += 1


# print_divisors()

def print_common_elements():
    list_1 = [2, 3, 5, 7, 8, 9]
    list_2 = [1, 2, 5, 6, 9, 10]
    for num in list_1:
        if num in list_2:
            print(num)


# print_common_elements()

def is_palindrome():
    palindrome = True
    word = input("Enter the word: ")
    char = 0
    word_length = len(word) - 1
    while char <= word_length / 2:
        if word[char] is not word[-char - 1]:
            palindrome = False
        char += 1
    print(f"{word} is palindrome!" if palindrome else f"{word} is not a palindrome.")


# is_palindrome()

def make_even_list():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print([num for num in my_list if num % 2 == 0])


# make_even_list()

def rock_paper_scissors():
    print('Welcome to Rock, paper, scissors!! \nRock - 1 \nPaper - 2 \nScissors - 3')
    my_dict = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    while True:
        player_1 = my_dict.get(int(input("Player 1: ")))
        player_2 = my_dict.get(int(input("Player 2: ")))
        if player_1 is not player_2:
            if player_1 == 'Rock' and player_2 == 'Scissors':
                print('Player 1 wins!!')
            elif player_1 == 'Scissors' and player_2 == 'Paper':
                print('Player 1 wins!!')
            elif player_1 == 'Paper' and player_2 == 'Rock':
                print('Player 1 wins!!')
            else:
                print('Player 2 wins!!')
        else:
            if input('\nIt\'s a tie!! Do you want to play again? Y/N: ') == 'Y':
                continue
            else:
                break
        if input('\nDo you want to play again? Y/N: ') == 'Y':
            continue
        else:
            break


# rock_paper_scissors()

def guess_the_num():
    user_guesses = []
    while True:
        num = random.randrange(0, 10, 1)
        user_guess = int(input('Enter a number between 0 to 9: '))
        if user_guess == num:
            print('You are right!')
        elif user_guess < num:
            print(f'You guess is a little too low. Number is {num} and your guess is {user_guess}')
        else:
            print(f'Your guess is a little too high. Number is {num} and your guess is {user_guess}')
        user_guesses.append(user_guess)
        if input('Do you want to continue? Y/N: ') == 'Y':
            continue
        else:
            print(f'Your guesses: {user_guesses}')
            break


# guess_the_num()

def common_elements():
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
    list_2 = [2, 4, 6, 7, 8, 9, 10, 11]
    print(list(dict.fromkeys([num for num in list_1 if num in list_2])))


# remove duplicates from list using list(dict.fromkeys())
# common_elements()

def is_prime():
    while True:
        prime = True
        try:
            num = int(input('Enter a number: '))
        except ValueError:
            print('Please enter a number.')
            continue
        divisor = 2
        while divisor <= round(num / 2):
            if num % divisor == 0:
                prime = False
                break
            divisor += 1
        print('Number is prime!!' if prime else 'Number is not a prime.')
        user_choice = input('Do you want to continue? Y/N: ')
        if user_choice.upper() == 'Y':
            continue
        else:
            break


# is_prime()

def check_for_prime(num):
    print("inside")
    prime = True
    divisor = 2
    while divisor <= round(num / 2):
        if num % divisor == 0:
            prime = False
            break
        divisor += 1
    print(f'{num} is prime!!' if prime else f'{num} is not a prime.')


def generate_num_list():
    my_list = [num for num in range(1, 100, 1)]
    x = map(check_for_prime, my_list)
    list(x)

# generate_num_list()

def my_generator(num):
    for i in range(num):
        yield i

def using_my_generator(input):
    for num in my_generator(input):
        print(num,end="\n")

# using_my_generator(10)

def fibonacci_generator(num):
    p = pp = 1
    for i in range(num):
        if i in [0,1]:
            yield 1
        else:
            num=p+pp
            pp,p = p,num
            yield num

def get_fibonacci(num):
    for i in fibonacci_generator(10):
        print(i)

#get_fibonacci(10)


def print_function(args,func):
    for x in args:
        print("f('",x,"') = ",func(x),sep="")

#print_function([x for x in range(-2,3)],lambda x : x**2-2*x+4)

def o(p):
    def q():
        return '*' * p

    return q

r = o(1)
s = o(2)
#print(r() + s())

def fun(d, k, v):
    d[k] = v
dc = {}
#print(fun(dc, '1', 'v'))

l = [[c for c in range(r)] for r in range(3)]
for x in l:
    if len(x) < 2:
     	print(l)


    class X:
        pass


    class Y(X):
        pass


    class Z(Y):
        pass

    x = X()
    z = Z()
    print(isinstance(x, Z), isinstance(z, X))


    class A:
        A = 1

        def __init__(self):
            self.a = 0


    #print(hasattr(A, 'A'))

    def multiply_lists():
        list1 = [2,3,4,5]
        list2 = [6,7,8,9]
        print([list1[num]*list2[num] for num in range(len(list1))])

    #multiply_lists()

    def multiply_lists_numpy():
        list1 = array([2,3,4,5])
        list2 = array([6,7,8,9])
        print(list1*list2)

    #multiply_lists_numpy()

    def load_Json():
        with open("C:/Users/krishna.teja.taduri/PycharmProjects/Config/Metadata.txt") as metadata:
            #print(type(metadata.readlines()))
            data = json.load(metadata)
            print(type(data))
            print(data['url']['PolicyCenter']['ST'])


    #load_Json()

import wx
def popup():
    app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
    frame = wx.Frame(None, wx.ID_ANY, "Hello World")  # A Frame is a top-level window.
    frame.Show(True)  # Show the frame.
    app.MainLoop()
popup()


from tkinter import *

def xyz():
    global a,root
    global retry_btn
    print (retry_btn.cget("text"))
    root.destroy()


def debugpopup():
    root = Tk()  # It is just a holder
    mes1 = Label({"text":"Error message comes here"})
    mes1.grid(row = 2,column=1)
    retry_btn = Button(root, text="Retry", command=xyz)
    retry_btn.grid(row=6, column=1)
    ignore_btn = Button(root, text="Ignore", command=xyz)
    ignore_btn.grid(row=6, column=3)
    abort_btn = Button(root, text="Abort", command=xyz)
    abort_btn.grid(row=6, column=3)
    root.mainloop()

#debugpopup()
