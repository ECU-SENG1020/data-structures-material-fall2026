using SHA

include("TupleModule.jl")
using .TupleModule: DsTuple

failures = Tuple{String,String}[]
success_count = 0

function record_success!()
    global success_count
    success_count += 1
end

function test_create()
    try
        t = DsTuple("a", "b", "c")
        @assert length(t) == 3
        record_success!()
    catch e
        push!(failures, ("test_create", sprint(showerror, e)))
    end
end

function test_get_item()
    try
        t = DsTuple("a", "b", "c")
        @assert t[2] == "b"  # Julia arrays are 1-based; this matches Python's ds_tuple[1]
        record_success!()
    catch e
        push!(failures, ("test_get_item", sprint(showerror, e)))
    end
end

function test_iter()
    try
        t = DsTuple("a", "b", "c")
        c = 0
        for _ in t
            c += 1
        end
        @assert c == 3
        record_success!()
    catch e
        push!(failures, ("test_iter", sprint(showerror, e)))
    end
end

function test_add()
    try
        t1 = DsTuple("a", "b", "c")
        t2 = DsTuple("e", "f", "g")
        t3 = t1 + t2
        s = replace(string(t3), " " => "")
        @assert s == "(a,b,c,e,f,g)"
        record_success!()
    catch e
        push!(failures, ("test_add", sprint(showerror, e)))
    end
end

function test_in_true()
    try
        t = DsTuple("a", "b", "c")
        result = ("b" in t)
        @assert length(t) == 3 && result == true
        record_success!()
    catch e
        push!(failures, ("test_in_true", sprint(showerror, e)))
    end
end

function test_in_false()
    try
        t = DsTuple("a", "b", "c")
        result = ("z" in t)
        @assert result == false
        @assert length(t) == 3 && result == false
        record_success!()
    catch e
        push!(failures, ("test_in_false", sprint(showerror, e)))
    end
end

function test_index()
    try
        t = DsTuple("a", "b", "c")
        @assert TupleModule.index(t, "b") == 1
        record_success!()
    catch e
        push!(failures, ("test_index", sprint(showerror, e)))
    end
end

function test_count()
    try
        t = DsTuple("a", "b", "c", "b")
        @assert TupleModule.count(t, "b") == 2
        record_success!()
    catch e
        push!(failures, ("test_count", sprint(showerror, e)))
    end
end

function sha256_normalized(path::AbstractString)
    text = read(path, String)
    normalized = replace(text, r"\s+" => "")
    return bytes2hex(sha256(codeunits(normalized)))
end

function parse_simple_json_object(text::AbstractString)::Dict{String,String}
    # Minimal parser for {"key": "value", ...} where values are strings.
    # This is sufficient for our generated file_hashes.json.
    out = Dict{String,String}()
    for m in eachmatch(r"\"([^\"]+)\"\s*:\s*\"([^\"]*)\"", text)
        out[m.captures[1]] = m.captures[2]
    end
    return out
end

function test_file_hashes()
    try
        json_text = read("file_hashes.json", String)
        hashes = parse_simple_json_object(json_text)
        for (fname, expected) in hashes
            @assert isfile(fname)
            actual = sha256_normalized(fname)
            @assert expected == actual
        end
        record_success!()
    catch e
        push!(failures, ("test_file_hashes", sprint(showerror, e)))
    end
end

function test_builtin_tuple_used()
    try
        text = read("TupleModule.jl", String)
        if occursin(r"\bTuple\b", text) || occursin(r"\btuple\s*\(", text)
            error("Detected use of built-in Tuple/tuple() in TupleModule.jl")
        end
        record_success!()
    catch e
        push!(failures, ("test_builtin_tuple_used", sprint(showerror, e)))
    end
end

function main()
    test_create()
    test_get_item()
    test_iter()
    test_add()
    test_in_true()
    test_in_false()
    test_index()
    test_count()
    test_file_hashes()
    test_builtin_tuple_used()

    println()
    if !isempty(failures)
        for (name, msg) in failures
            println("ERROR: ", name, " -> ", msg)
        end
        println("\n", length(failures), " tests failed")
        println("\n", success_count, " tests passed")
        println()
        exit(1)
    end

    println("All ", success_count, " tests passed")
    println()
end

main()
