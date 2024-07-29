# Check if a given number is prime or not

# To check if a given number is prime or not we need to check for its square root
# there fore we iterate over the numbers from 2 to num**0.5 (doing sq root of number) and then adding +1 to include the
# integer part of the number

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


is_prime(6)
