module SetByDictionary

export MySetDict, add!, remove!, copy_set

mutable struct MySetDict
    data::Dict{Any,Bool}
    function MySetDict(args...)
        s = new(Dict{Any,Bool}())
        for a in args
            add!(s, a)
        end
        return s
    end
end

Base.length(s::MySetDict) = length(s.data)

function Base.show(io::IO, s::MySetDict)
    if isempty(s.data)
        print(io, "set()")
        return
    end
    print(io, "{")
    first_item = true
    for k in keys(s.data)
        if !first_item
            print(io, ", ")
        end
        first_item = false
        print(io, string(k))
    end
    print(io, "}")
end

add!(s::MySetDict, value) = (s.data[value] = true)

function remove!(s::MySetDict, value)
    haskey(s.data, value) || return
    delete!(s.data, value)
end

Base.in(value, s::MySetDict) = haskey(s.data, value)

function Base.iterate(s::MySetDict, state=nothing)
    return iterate(keys(s.data), state)
end

# union
function Base.:|(a::MySetDict, b::MySetDict)
    out = MySetDict()
    for x in a
        add!(out, x)
    end
    for x in b
        add!(out, x)
    end
    return out
end

# intersection
function Base.:&(a::MySetDict, b::MySetDict)
    out = MySetDict()
    for x in a
        (x in b) && add!(out, x)
    end
    return out
end

# difference
function Base.:-(a::MySetDict, b::MySetDict)
    out = MySetDict()
    for x in a
        !(x in b) && add!(out, x)
    end
    return out
end

function copy_set(s::MySetDict)
    out = MySetDict()
    for x in s
        add!(out, x)
    end
    return out
end

end
