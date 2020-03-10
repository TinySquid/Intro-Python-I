# STRETCH -> Rewrite code challenges you've solved before or projects you've implemented before in a different language in Python.
# Start getting in as much practice with the language as possible!


# Given an array of integers, find the sum of its elements.
# simpleArraySum has the following parameter(s):
# ar: an array of integers

# JS
# function simpleArraySum(ar){
#     return ar.reduce((acc, val) => acc += val);
# }

# Python
def simpleArraySum(ar):
    return sum(ar)


print("Pass") if simpleArraySum([1, 2, 4, 9]) == 16 else print("Fail")

# Write a function that determines if a provided number n is a prime number
# https://medium.com/@sarahdherr/prime-number-algorithm-in-js-f9fb2439c7ae

# JS
# function isPrime (num) {
#   if (num <= 1) {
#     return true
#   } else if (num <= 3) {
#     return true
#   } else if (num%2 === 0 || num%3 === 0) {
#     return false
#   }

#   let i = 5
#   while (i*i <= num) {
#     if (num%i === 0 || num%(i+2) === 0) {
#       return false
#     }
#     i += 6
#   }
#   return true
# }

# Python
def isPrime(n):
    if n <= 1:
        return True
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


nums = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    29,
    31,
    179,
    181,
    197,
    199,
]

for num in nums:
    print(isPrime(num))


# 1 How many seconds are there in 21 minutes and 15 seconds ?
print(f"There are {21 * 60 + 15} seconds in 21 minutes and 15 seconds.")

# 2 How many miles are there in 5 kilometers?
print(f"There are {0.621371 * 5} miles in 5 kilometers")

# 3 If you run a 5 kilometer race in 21 minutes and 15 seconds, what is your average pace (time per mile in minutes and seconds)?
distance = 0.621371 * 5
pace = 21.25 / distance

print(f"Your pace averaged {round(pace, 2)} minutes per mile")

# 4 What is your average speed in miles per hour?
print(f"Your speed averaged {round(60 / pace, 2)} MPH")

# 5 Suppose the cover price of a book is $19.95, but bookstores get a 25% discount.
# Shipping costs $2.50 for the first copy and $1 for each additional copy.
# What is the total wholesale cost for 75 copies?

# Shipping isn't included in discount because it specifies *cover price*, not total price.
# bookstore price
cover_price = 19.95 * 0.75

# first copy price
first_shipping_cost = 2.5
first_book_total = cover_price + first_shipping_cost

# now for additional copy price
additional_copy_price = cover_price + 1

# sum it all up
wholesale_cost = first_book_total + additional_copy_price * 74

print(f"Total wholesale cost for 75 book copies is ${round(wholesale_cost, 2)} USD")
