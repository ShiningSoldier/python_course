palindrome_string = "sracecars"

def check_if_palindrome(some_string):

    first_index = 0
    last_index = len(some_string) - 1

    while first_index <= last_index:
        if some_string[first_index] != some_string[last_index]:
            return False
        first_index+=1
        last_index-=1

    return True

print(check_if_palindrome(palindrome_string))
