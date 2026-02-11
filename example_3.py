while True:
    n = int(input("How many times do you want to print 'woof'? "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        break

for _ in range(n):
    print("woof")