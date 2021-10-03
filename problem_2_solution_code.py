def fib_even_sum():
    fibs = [1,2]                        # Initiate first two values as 1 and 2

    i, j = 0, 1                         # Two variables required to add the previous two fibonacci values
    while True:                         # A loop to find the fib values continuosly as long as the fibonacci value doesn't 	#exceed 4000000
        next_fib = fibs[i]+fibs[j]      # Each time we find the next fibonacci value by adding the previous two values

        if next_fib > 4000000:          # Break the loop if the next fibonacci value is more than 4000000
            break

        fibs.append(next_fib)           # Then append the next fib value in the list

        i += 1                          # Each time the two variable to access the indices gets increased by 1
        j += 1

    even_sum = 0                        # Intializing a variable to add all the even fibonacci values from the list
    for value in fibs:                  # check each value in the loop
        if value%2 == 0:                # If the value is even 
            even_sum += value           # Then we the value to our final sum

    return even_sum                     # Finally return the sum of all even values from the fibonacci list

print(fib_even_sum())
