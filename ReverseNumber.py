def reverse_number(num):
    rev_num = 0

    while num != 0:
        rev_num = rev_num * 10 + num % 10
        num //= 10

    return rev_num


num = int(input("Enter the number to reverse: "))
reversed_num = reverse_number(num)
print(f"The reverse of {num} is {reversed_num}")

# ------------------------------------------------------------------

num = 123456
print("Reversed Number:", str(num)[::-1])
