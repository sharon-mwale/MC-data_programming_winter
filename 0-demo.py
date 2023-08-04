if __name__ == "__main__":
    #Take user input for the upper limit
    upper_limit = int(input("Enter the upper limit: "))

    sum_of_evens = 0

    for num in range(1, upper_limit + 1):
        if num % 2 == 0:
            sum_of_evens += num
    #Print the final sum of even numbers
    print(f"The sum of even numbers between 1 and {upper_limit} is: {sum_of_evens}")
