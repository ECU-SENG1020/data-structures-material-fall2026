using SHA

const FILES = ["test.jl"]

function sha256_file_no_whitespace(path::AbstractString)::String
    text = read(path, String)
    normalized = replace(text, r"\s+" => "")
    return bytes2hex(sha256(codeunits(normalized)))
end

function build_hashes()::Vector{Tuple{String,Union{String,Nothing}}}
    out = Tuple{String,Union{String,Nothing}}[]
    for fname in FILES
        if isfile(fname)
            push!(out, (fname, sha256_file_no_whitespace(fname)))
        else
            push!(out, (fname, nothing))
        end
    end
    return out
end

function write_hashes(path::AbstractString="file_hashes.json")
    kvs = build_hashes()
    open(path, "w") do io
        println(io, "{")
        for (i, (k, v)) in enumerate(kvs)
            value_str = v === nothing ? "null" : "\"" * v * "\""
            comma = i < length(kvs) ? "," : ""
            println(io, "  \"" * k * "\": " * value_str * comma)
        end
        println(io, "}")
    end
end

if abspath(PROGRAM_FILE) == @__FILE__
    write_hashes()
    println("Wrote file_hashes.json")
end
