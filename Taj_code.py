from __future__ import division
import random
import math
import itertools

#################################################################################
# Function: sum_func
# Purpose: Calulates the sum of an array
# Inputs -
# arr: An array of positive integers
#################################################################################
def sum_func(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return(sum)

#################################################################################
# Function: exhaustive_subset_sum
# Purpose: Prints all solutions to subset sum problem 
# Inputs-
# arr: set of positive integers
# T: target sum
##################################################################################
def exhaustive_subset_sum(arr, T):
    # if the target sum is zero, return true
    if T==0:
        print("True: Target sum is 0")

    # Generates all combinations of an array and checks if subset sums up to target value
    for i in range(0, len(arr)+1):
        for subset in itertools.combinations(arr, i):
            subset_sum = sum_func(subset)
            if subset_sum == T:
                return True

#################################################################################
# Function: random_set_generator
# Purpose: Generates random set of numbers
# Inputs-
# r: max range that random numbers can be chosen from
# n: total number of elements in the set
##################################################################################
def random_set_generator(r, n):
    # Generates random numbers without duplicates within range and number of elements
    import random
    randSet = random.sample(range(r), n) 
    density = n / math.log(max(randSet),2)
    print(randSet)
    print(density)
    return randSet

class Instance():
    def __init__(self, arr, n, b, density, target_sum):
        self.arr = arr
        self.n = n
        self.b = b
        self.density = density
        self.target_sum = target_sum

   
    #################################################################################
    # Function: bit_random_set_generator
    # Purpose: Generates random set of numbers with given bitch length
    # Inputs-
    # n: total number of elements in the set
    # b: bit length of each number in a set
    ##################################################################################
    def bit_random_set_generator(self):
        self.density = self.n / self.b
        # Generates random numbers without duplicates within range and number of elements
        for x in range(self.n):
            bits = []
            for j in range(self.b):
                bits.append(str(random.randint(0,1))) 
            self.arr.append(int(''.join(bits), 2))
        

        #print(self.arr)
        #print(self.density)

    #################################################################################
    # Function: target_sum_generator
    # Purpose: Generates target sum based on half of given set
    # Inputs-
    # arr: A set of positive integers
    ##################################################################################
    def target_sum_generator(self):

        if (self.n % 2) != 0:
            print("Array must be an even number length")

        else:   
            list = random.sample(self.arr,self.n // 2)
            self.target_sum = sum_func(list)
            #print(self.target_sum)
    


if __name__ == "__main__":
    inst = Instance([],6,4,0,0)
    inst.bit_random_set_generator()
    inst.target_sum_generator()
    # print(inst.density)
    print(inst.target_sum)
    print(inst.arr)
    if (exhaustive_subset_sum(inst.arr, inst.target_sum) == True):
        print("There is a possible subset with sum", inst.target_sum)

    if (exhaustive_subset_sum([1,2,3,4], 20) == True):
        print("There is a possible subset with sum", inst.target_sum)
    else:
        print("There is no possible subset within the given subset")
    