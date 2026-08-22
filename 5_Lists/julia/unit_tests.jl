include("ListModule.jl")
using .ListModule: DsList, append!, insert!, remove_at!, clear!

failures = String[]
success_count = 0

function check(test_name::String, f::Function)
    global success_count
    try
        f()
        success_count += 1
    catch e
        push!(failures, "$(test_name) -> $(e)")
    end
end

check("test_append") do
    ds = DsList()
    append!(ds, "a")
    append!(ds, "b")
    append!(ds, "c")
    @assert length(ds) == 3
end

check("test_get_item") do
    ds = DsList()
    append!(ds, "a")
    append!(ds, "b")
    append!(ds, "c")
    @assert ds[2] == "b"
end

check("test_set_item") do
    ds = DsList()
    append!(ds, "a")
    append!(ds, "b")
    append!(ds, "c")
    ds[2] = "d"
    @assert ds[2] == "d"
end

check("test_iter") do
    ds = DsList()
    append!(ds, "a")
    append!(ds, "b")
    count = 0
    for _ in ds
        count += 1
    end
    @assert count == 2
end

check("test_add") do
    ds1 = DsList()
    append!(ds1, "e")
    append!(ds1, "b")

    ds2 = DsList()
    append!(ds2, "f")
    append!(ds2, "f")

    ds3 = ds1 + ds2
    @assert string(ds3) == "['e', 'b', 'f', 'f']"
end

check("test_in_true") do
    ds = DsList()
    append!(ds, "e")
    append!(ds, "b")
    append!(ds, "f")
    append!(ds, "f")
    @assert ("b" in ds) == true
end

check("test_in_false") do
    ds = DsList()
    append!(ds, "e")
    append!(ds, "b")
    append!(ds, "f")
    append!(ds, "f")
    @assert length(ds) == 4
    @assert ("z" in ds) == false
end

check("test_clear") do
    ds = DsList()
    append!(ds, "e")
    append!(ds, "b")
    append!(ds, "f")
    append!(ds, "f")
    clear!(ds)
    @assert length(ds) == 0
end

println()
if !isempty(failures)
    for msg in failures
        println("ERROR: ", msg)
    end
    println("\n$(length(failures)) tests failed")
    println("\n$(success_count) tests passed")
    println()
    exit(1)
end

println("All $(success_count) tests passed")
println()
