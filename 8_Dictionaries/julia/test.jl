include("DsDictionaryModule.jl")

using SHA
using .DsDictionaryModule: DsDictionary, keys, values, items

failures = Tuple{String,String}[]
success_count = 0

function _record_success!()
    global success_count
    success_count += 1
end

function _record_failure!(name::String, err)
    push!(failures, (name, string(err)))
end

function test_create_empty()
    try
        d = DsDictionary()
        @assert length(d) == 0
        _record_success!()
    catch e
        _record_failure!("test_create_empty", e)
    end
end

function test_create_non_empty()
    try
        d = DsDictionary((("a", 1), ("b", 2)))
        @assert length(d) == 2
        _record_success!()
    catch e
        _record_failure!("test_create_non_empty", e)
    end
end

function test_set()
    try
        d = DsDictionary()
        d["a"] = 1
        @assert length(d) == 1
        _record_success!()
    catch e
        _record_failure!("test_set", e)
    end
end

function test_get()
    try
        d = DsDictionary((("a", 1),))
        @assert d["a"] == 1
        _record_success!()
    catch e
        _record_failure!("test_get", e)
    end
end

function test_overwrite_value()
    try
        d = DsDictionary()
        d["x"] = 5
        d["x"] = 10
        @assert d["x"] == 10
        @assert length(d) == 1
        _record_success!()
    catch e
        _record_failure!("test_overwrite_value", e)
    end
end

function test_delitem()
    try
        d = DsDictionary()
        d["k"] = "v"
        delete!(d, "k")
        @assert length(d) == 0
        _record_success!()
    catch e
        _record_failure!("test_delitem", e)
    end
end

function test_keyerror()
    try
        d = DsDictionary()
        try
            _ = d["missing"]
            _record_failure!("test_keyerror", "KeyError not thrown")
        catch e
            @assert e isa KeyError
            _record_success!()
        end
    catch e
        _record_failure!("test_keyerror", e)
    end
end

function test_len()
    try
        d = DsDictionary((("a", 1), ("b", 2), ("c", 3)))
        @assert length(d) == 3
        _record_success!()
    catch e
        _record_failure!("test_len", e)
    end
end

function test_iter()
    try
        d = DsDictionary((("a", 1), ("b", 2), ("c", 3)))
        ks = [k for k in d]
        @assert ks == ["a", "b", "c"]
        _record_success!()
    catch e
        _record_failure!("test_iter", e)
    end
end

function test_print_dsdictionary()
    try
        d = DsDictionary((("a", 1), ("b", 2)))
        normalized = replace(string(d), r"\s+" => "")
        @assert normalized == "{'a':1,'b':2}"
        _record_success!()
    catch e
        _record_failure!("test_print_dsdictionary", e)
    end
end

function test_print_keys()
    try
        d = DsDictionary((("a", 1), ("b", 2)))
        keys_view = keys(d)
        normalized = replace(string(keys_view), r"\s+" => "")
        @assert normalized == "DsDictionaryView_Keys(['a','b'])"
        _record_success!()
    catch e
        _record_failure!("test_print_keys", e)
    end
end

function test_print_values()
    try
        d = DsDictionary((("a", 1), ("b", 2)))
        values_view = values(d)
        normalized = replace(string(values_view), r"\s+" => "")
        @assert normalized == "DsDictionaryView_Values([1,2])"
        _record_success!()
    catch e
        _record_failure!("test_print_values", e)
    end
end

function test_print_items()
    try
        d = DsDictionary((("a", 1), ("b", 2)))
        items_view = items(d)
        normalized = replace(string(items_view), r"\s+" => "")
        @assert normalized == "DsDictionaryView_Items([('a',1),('b',2)])"
        _record_success!()
    catch e
        _record_failure!("test_print_items", e)
    end
end

function test_values()
    try
        d = DsDictionary((("a", 1), ("b", 2)))
        @assert collect(values(d)) == [1, 2]
        _record_success!()
    catch e
        _record_failure!("test_values", e)
    end
end

function test_items()
    try
        d = DsDictionary((("a", 1), ("b", 2)))
        @assert collect(items(d)) == [("a", 1), ("b", 2)]
        _record_success!()
    catch e
        _record_failure!("test_items", e)
    end
end

function test_view_reflects_changes()
    try
        d = DsDictionary((("a", 1),))
        keys_view = keys(d)
        @assert collect(keys_view) == ["a"]
        d["b"] = 2
        @assert collect(keys_view) == ["a", "b"]
        _record_success!()
    catch e
        _record_failure!("test_view_reflects_changes", e)
    end
end

function _sha256_no_ws(path::AbstractString)::String
    text = read(path, String)
    normalized = replace(text, r"\s+" => "")
    return bytes2hex(sha256(codeunits(normalized)))
end

function _parse_simple_json_object(text::String)
    pairs = Tuple{String,Union{String,Nothing}}[]
    for m in eachmatch(r"\"([^\"]+)\"\s*:\s*(null|\"([^\"]*)\")", text)
        key = m.captures[1]
        raw = m.captures[2]
        if raw == "null"
            push!(pairs, (key, nothing))
        else
            value = m.captures[3]
            push!(pairs, (key, value))
        end
    end
    return pairs
end

function test_file_hashes()
    try
        @assert isfile("file_hashes.json")
        expected = _parse_simple_json_object(read("file_hashes.json", String))
        for (fname, exp_hash) in expected
            @assert isfile(fname)
            actual = _sha256_no_ws(fname)
            @assert exp_hash == actual
        end
        _record_success!()
    catch e
        _record_failure!("test_file_hashes", e)
    end
end

function test_builtin_dictionary_used()
    try
        text = read("DsDictionaryModule.jl", String)
        # Disallow Dict usage in the implementation.
        @assert !occursin(r"\bDict\b", text)
        @assert !occursin("Dict{", text)
        _record_success!()
    catch e
        _record_failure!("test_builtin_dictionary_used", e)
    end
end

function main()
    test_create_empty()
    test_create_non_empty()
    test_set()
    test_get()
    test_overwrite_value()
    test_delitem()
    test_keyerror()
    test_len()
    test_iter()
    test_print_dsdictionary()
    test_print_keys()
    test_print_values()
    test_print_items()
    test_values()
    test_items()
    test_view_reflects_changes()
    test_file_hashes()
    test_builtin_dictionary_used()

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

    println("\nAll ", success_count, " tests passed\n")
end

main()
