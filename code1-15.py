data=("Hans", "smith", 12.42)
format_string="Hello"
#desired output 
#Hans smith. You owe me 12 $

#Answer method 1:
print("%s %s. You owe me %d $" %(data))

#Answer method 2:
a="hans"
b='smith'
c=12.42
print(f"{a} {b}. You owe me {c} $")

