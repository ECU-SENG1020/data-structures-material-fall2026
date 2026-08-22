module DsDictionaryModule

export DsDictionary, DsDictionaryView, items

import Base: iterate, length, getindex, setindex!, delete!, show, keys, values

_py_repr(x) = string(x)

function _py_repr(x::AbstractString)
    # Python-ish repr for strings: single quotes
    escaped = replace(x, "\\" => "\\\\", "'" => "\\'")
    return "'" * escaped * "'"
end

function _py_repr(x::Tuple)
    # Only needed for 2-tuples in this unit
    if length(x) == 2
        return "(" * _py_repr(x[1]) * ", " * _py_repr(x[2]) * ")"
    end
    inner = join((_py_repr(v) for v in x), ", ")
    return "(" * inner * ")"
end

function _py_list_str(values)
    return "[" * join((_py_repr(v) for v in values), ", ") * "]"
end

mutable struct DsDictionary
    store::Vector{Tuple{Any,Any}}

    function DsDictionary(items=nothing)
        d = new(Tuple{Any,Any}[])
        if items !== nothing
            for item in items
                k, v = item
                push!(d.store, (k, v))
            end
        end
        return d
    end
end

struct DsDictionaryView
    store::Vector{Tuple{Any,Any}}
    view_type::Symbol
end

function show(io::IO, d::DsDictionary)
    parts = String[]
    for (k, v) in d.store
        push!(parts, _py_repr(k) * ": " * _py_repr(v))
    end
    print(io, "{" * join(parts, ", ") * "}")
end

function show(io::IO, v::DsDictionaryView)
    if v.view_type === :keys
        ks = [k for (k, _) in v.store]
        print(io, "DsDictionaryView_Keys(" * _py_list_str(ks) * ")")
        return
    end
    if v.view_type === :values
        vs = [val for (_, val) in v.store]
        print(io, "DsDictionaryView_Values(" * _py_list_str(vs) * ")")
        return
    end
    if v.view_type === :items
        its = [(k, val) for (k, val) in v.store]
        print(io, "DsDictionaryView_Items(" * _py_list_str(its) * ")")
        return
    end
    throw(ArgumentError("Invalid view type"))
end

function setindex!(d::DsDictionary, value, key)
    for i in eachindex(d.store)
        k, _ = d.store[i]
        if k == key
            d.store[i] = (key, value)
            return value
        end
    end
    push!(d.store, (key, value))
    return value
end

function getindex(d::DsDictionary, key)
    for (k, v) in d.store
        if k == key
            return v
        end
    end
    throw(KeyError(key))
end

function delete!(d::DsDictionary, key)
    for i in eachindex(d.store)
        k, _ = d.store[i]
        if k == key
            deleteat!(d.store, i)
            return d
        end
    end
    throw(KeyError(key))
end

length(d::DsDictionary) = length(d.store)

function iterate(d::DsDictionary, state::Int=1)
    state > length(d.store) && return nothing
    k, _ = d.store[state]
    return (k, state + 1)
end

function keys(d::DsDictionary)
    return DsDictionaryView(d.store, :keys)
end

function values(d::DsDictionary)
    return DsDictionaryView(d.store, :values)
end

function items(d::DsDictionary)
    return DsDictionaryView(d.store, :items)
end

function iterate(v::DsDictionaryView, state::Int=1)
    state > length(v.store) && return nothing
    k, val = v.store[state]
    if v.view_type === :keys
        return (k, state + 1)
    end
    if v.view_type === :values
        return (val, state + 1)
    end
    if v.view_type === :items
        return ((k, val), state + 1)
    end
    throw(ArgumentError("Invalid view type"))
end

end
