# update: swap pairs problem
def swap_pairs(my_list):
    # if the length is even, then we want to range(0, length, 2)
    # if the length is odd, then we want to range(0, length -1, 2)

    length = len(my_list)
    if length % 2 != 0:
        length -= 1

    for i in range(0, length, 2):
        num = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = num


# update: for testing problems
def main():
    my_list = [10, 20, 30, 40, 50]
    print(my_list)
    swap_pairs(my_list)
    print(my_list)


main()
print("----------------------------------")


# update: the average string length of elements
def average_string_length():
    test_list = ["belt", "hat", "jelly", " bubble gum"]

    # printing original list
    print("The test list: " + str(test_list))

    # Average string lengths in list
    temp = [len(ele) for ele in test_list]
    res = 0 if len(temp) == 0 else (float(sum(temp)) / len(temp))

    # printing result
    print("The average string length: " + str(res))


average_string_length()
print("----------------------------------")


# update: whether the list is a palindrome
def palindrome():
    my_str = ["alpha", "beta", "gamma", "delta", "gamma", "beta", "alpha"]

    # my list
    print("My list is:" +str(my_str))

    # reverse the string
    rev_str = reversed(my_str)

    # check if the list is palindrome
    if list(my_str) == list(rev_str):
        print("My list is a palindrome.")
    else:
        print("My list is not a palindrome.")


palindrome()
print("----------------------------------")


# update: dictionary
def dictionary():
    my_dict = dict([('banana', 1),
                    ('peach', 2),
                    ('nectarine', 3),
                    ('kiwi', 1),
                    ('apple', 3)])
    print(my_dict)


dictionary()