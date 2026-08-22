

"""Algorithm 1: check every number."""
function get_even_numbers_version_one(from_num, to_num)
    number = from_num
    even_numbers = []

    while number <= to_num
        # check to see if number is even
        if number % 2 == 0
            push!(even_numbers, number)
        end

        # increase number by 1
        number += 1
    end

    return even_numbers
end

"""Algorithm 2: jump by 2 each time."""
function get_even_numbers_version_two(from_num, to_num)
    number = from_num
    even_numbers = []

    while number <= to_num
        if number % 2 == 0
            push!(even_numbers, number)
        end
        number += 2
    end

    return even_numbers
end

function main()

    start_time = time_ns()
    _ = get_even_numbers_version_one(2, 1000)
    elapsed_time = time_ns() - start_time
    println("Algorithm 1 took $(elapsed_time) nanoseconds.")



    start_time = time_ns()
    _ = get_even_numbers_version_two(2,1000)
    elapsed_time = time_ns() - start_time
    println("Algorithm 2 took $(elapsed_time) nanoseconds.")
end


main()


