if __name__ == "__main__":
    input_str = input("Enter a list of integers separated by spaces: ")

    # Converting the input string into a list of integers
    input_list = [int(x) for x in input_str.split()]

    # Using the sorted function with a lambda function as the key
    sorted_list = sorted(input_list, key=lambda x: x)

    #Print the sorted list
    print("Sorted list in ascending order:", sorted_list)
