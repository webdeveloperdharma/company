def sum_of_multiples_1():             
    multiples = []                              # An empty list to store all the multiples of 3 or 5
    for numb in range(1,1000):                  # Iterating from 1 to 999 
        if numb%3 == 0 or numb%5 == 0:          # If the remainder is zero after dividing the number with 3 or 5
            multiples.append(numb)              # then the number is added into the list

    return sum(multiples)                       # Finally return the sum of all the numbers present in the list-multiples

print(sum_of_multiples_1())


def sum_of_multiples_2():
    all_multiples = [numb for numb in range(1,1000) if numb%3 == 0 or numb%5 == 0]      # List comprehesion which holds all the multiples
                                                                                        # of 3 and 5 below 1000
    return sum(all_multiples)                                                           # return the sum of multiples

# print(sum([i for i in range(1,1000) if i%3 == 0 or i%5 == 0]))    # this gives the same as above
