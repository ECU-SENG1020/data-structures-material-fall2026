import time

#Algorithm 1: check every number.
def get_even_numbers_version_one(from_num, to_num):
    number = from_num
    even_numbers = []

    while number <= to_num:
        # check to see if number is even
        if number % 2 == 0:
            even_numbers.append(number)
    
        # increase number by 1
        number += 1

    return even_numbers


#Algorithm 2: jump by 2 each time.
def get_even_numbers_version_two(from_num, to_num):
    number = from_num
    even_numbers = []
    while number <= to_num:
        # check to see if number is even
        if number % 2 == 0:
            even_numbers.append(number)
        
        # increase number by 2
        number += 2
    return even_numbers

def main():

    start_time = time.perf_counter_ns()
    _ = get_even_numbers_version_one(2, 1000)
    end_time = time.perf_counter_ns()
    elapsed_time = end_time - start_time
    print(f"Algorithm 1 took {elapsed_time} nanoseconds.")



    start_time = time.perf_counter_ns()
    _ = get_even_numbers_version_two(2, 1000)
    end_time = time.perf_counter_ns()
    elapsed_time = end_time - start_time
    print(f"Algorithm 2 took {elapsed_time} nanoseconds.")


if __name__ == "__main__":
    main()
