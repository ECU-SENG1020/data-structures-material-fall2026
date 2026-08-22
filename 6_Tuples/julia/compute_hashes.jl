using SHA

const FILES = ["test.jl"]

function json_escape(s::AbstractString)::String
    buf = IOBuffer()
    for c in s
        if c == '"'
            print(buf, "\\\"")
        elseif c == '\\'
            print(buf, "\\\\")
        elseif c == '\n'
            print(buf, "\\n")
        elseif c == '\r'
            print(buf, "\\r")
        elseif c == '\t'
            print(buf, "\\t")
        else
            print(buf, c)
        end
    end
    return String(take!(buf))
end

function to_json_object(d::Dict{String,Any})::String
    keys_sorted = sort(collect(keys(d)))
    parts = String[]
    for k in keys_sorted
        v = d[k]
        vjson = v === nothing ? "null" : string('"', json_escape(string(v)), '"')
        push!(parts, string('"', json_escape(k), '"', ": ", vjson))
    end
    return "{\n  " * join(parts, ",\n  ") * "\n}\n"
end

function sha256_normalized(path::AbstractString)::String
    text = read(path, String)
    normalized = replace(text, r"\s+" => "")
    return bytes2hex(sha256(codeunits(normalized)))
end

function build_hashes()::Dict{String,Any}
    out = Dict{String,Any}()
    for fname in FILES
        out[fname] = isfile(fname) ? sha256_normalized(fname) : nothing
    end
    return out
end

function write_hashes(path::AbstractString="file_hashes.json")
    data = build_hashes()
    write(path, to_json_object(data))
end

if abspath(PROGRAM_FILE) == @__FILE__
    write_hashes()
    println("Wrote file_hashes.json")
end
