def main():
    n = get_number()
    woofs(n)


def get_number():
    while True:
        x = int(input("How many times do you want to print 'woof'? "))
        if x <= 0:
            continue
        else:
            return x
        
def woofs(y):
    for _ in range(y):
        print("woof")

main()

#when functions are used they can be called at anytime and don't have to be run sequentially.


def main():
    n = get_number()
    woofs(n)


def get_number():
    while True:
        x = int(input("How many times do you want to print 'woof'? "))
        if x > 0:
            return x #implied break
        
def woofs(y):
    for _ in range(y):
        print("woof")

main()