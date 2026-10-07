import random

num = random.randint(1, 6)
word = "N/A"

match num:
    case 1:
        word = "one"
    case 2:
        word = "two"
    case 3:
        word = "three"
    case 4: 
        word = "four"
    case 5: 
        word = "five"
    case 6: 
        word = "six"

print("I generated the number" + " " + word +".")