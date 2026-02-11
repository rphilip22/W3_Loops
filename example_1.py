i = 0
while i != 3:
    print("woof")
    i = i + 1

#you can also use print("woof\n" * 3) to print "woof" three times, 
# but it will add an extra newline at the end.

#to fix this, you can use print("woof\n" * 3, end="") to avoid adding the extra newline.