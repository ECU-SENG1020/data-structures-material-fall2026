
using Base.Threads

# 1) Efficiency (compare two algorithms)
# Run: julia 1_efficiency.jl

"""Algorithm 1: check every number."""
function get_even_numbers_version_one(; from_num::Int=2, to_num::Int=1000)
    number = from_num
    even_numbers = Int[]

    while number <= to_num
        if number % 2 == 0
            push!(even_numbers, number)
        end
        number += 1
    end

    return even_numbers
end

"""Algorithm 2: jump by 2 each time."""
function get_even_numbers_version_two(; from_num::Int=2, to_num::Int=1000)
    from_num > to_num && return Int[]

    thread_count = min(nthreads(), to_num - from_num + 1)
    chunk_size = cld(to_num - from_num + 1, thread_count)
    results = Vector{Vector{Int}}(undef, thread_count)

    @threads for chunk_index in 1:thread_count
        chunk_start = from_num + (chunk_index - 1) * chunk_size
        chunk_end = min(chunk_start + chunk_size - 1, to_num)

        local_result = Int[]

        for number in chunk_start:chunk_end
            if iseven(number)
                push!(local_result, number)
            end
        end

        results[chunk_index] = local_result
    end

    return reduce(vcat, results)
end

function get_even_numbers_version_three(; from_num::Int=2, to_num::Int=1000)
    first_even = iseven(from_num) ? from_num : from_num + 1
    return first_even > to_num ? Int[] : collect(first_even:2:to_num)
end

function main()
    # result1 = get_even_numbers_version_one(from_num=2, to_num=100000)
    # # println(result1)

    # result2 = get_even_numbers_version_two(from_num=2, to_num=100000)
    # # println(result2)

    start_time = time_ns()
    _ = get_even_numbers_version_one(from_num=2,to_num=100000000)
    elapsed_time = time_ns() - start_time
    println("Algorithm 1 took $(elapsed_time) nanoseconds.")

    start_time = time_ns()
    _ = get_even_numbers_version_two(from_num=2,to_num=100000000)
    elapsed_time = time_ns() - start_time
    println("Algorithm 2 took $(elapsed_time) nanoseconds.")

    start_time = time_ns()
    _ = get_even_numbers_version_three(from_num=2,to_num=100000000)
    elapsed_time = time_ns() - start_time
    println("Algorithm 3 took $(elapsed_time) nanoseconds.")
end


main()

# if abspath(PROGRAM_FILE) == @__FILE__
#     main()
# end
