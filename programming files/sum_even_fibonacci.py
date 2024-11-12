#initializing sequence
a, b = 0, 1
#create variable
sum_even = 0
#loop that generates sequence until b is 4000000
while b < 4000000:
    #check if b is even
    if b % 2 == 0:
        #if its even add to the sum
        sum_even += b
    #move to next number
    a, b = b, a+b

print(sum_even)

# answer should be 4613732
