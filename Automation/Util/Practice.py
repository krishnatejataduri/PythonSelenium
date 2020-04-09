
list_1 = [1,2,3]

list_2 = [num*num for num in list_1]

'''Prime Numbers Program'''



def prime_numbers():
    num = int(input("Enter the number: "))
    for i in range(1,num+1):
        is_prime = True
        for j in range(2,int(i/2+1)):
            if i%j==0:
                is_prime = False
                break
        if is_prime:
            print(i)

#prime_numbers()


'''List comprehension program'''

def generate_list(limit):
    my_list = [num for num in range(1,limit+1)]
    return my_list

#print(generate_list(25))



'''Palidrome Program'''

def is_palindrome():
    value = input("Enter the value: ")
    is_palindrome = True;
    for i in range(round(len(value)/2)):
        if value[i] != value[-i-1]:
            is_palindrome = False
            break
    if is_palindrome:
        print("It is is a palindrome!!")
    else:
        print("Sorry, try again.")

#is_palindrome()

'''Common elements in 2 lists'''

def common_elements():
    list_1 = [0,1,2,4,6,6,7,8,11]
    list_2 = [1,2,3,4,5,6,7,8,9,10]
    # for num in list_1:
    #     if num in list_2:
    #         print(num)
    common_list = list(dict.fromkeys([num for num in list_1 if num in list_2]))
    print(common_list)

#common_elements()




