start = int(input("enter starting number: "))
end = int(input("enter ending number: "))
print("four-digit numbers with all even digits and perfect squers:")
for num in range(start, end + 1):
    root = int(num ** 0.5)
    if root * root == num:
        digits = str(num)
        if all(int(d) % 2 ==0 for d in digits):
            print(num)