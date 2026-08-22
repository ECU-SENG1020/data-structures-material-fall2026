module SetDataStructure

export MySet, add!, remove!

mutable struct MySet
    data::Vector{Any}
    function MySet(args...)
        s = new(Any[])
        for a in args
            add!(s, a)
        end
        return s
    end
end

Base.length(s::MySet) = length(s.data)

function Base.show(io::IO, s::MySet)
    if isempty(s.data)
        print(io, "set()")
        return
    end
    print(io, "{")
    for (i, item) in enumerate(s.data)
        i > 1 && print(io, ", ")
        print(io, string(item))
    end
    print(io, "}")
end

function add!(s::MySet, value)
    (value in s.data) && return
    push!(s.data, value)
end

function remove!(s::MySet, value)
    idx = findfirst(==(value), s.data)
    idx === nothing && return
    deleteat!(s.data, idx)
end

Base.in(value, s::MySet) = value in s.data

function Base.iterate(s::MySet, state::Int=1)
    state > length(s.data) && return nothing
    return (s.data[state], state + 1)
end

# union
function Base.:|(a::MySet, b::MySet)
    out = MySet()
    for x in a
        add!(out, x)
    end
    for x in b
        add!(out, x)
    end
    return out
end

# intersection
function Base.:&(a::MySet, b::MySet)
    out = MySet()
    for x in a
        (x in b) && add!(out, x)
    end
    return out
end

# difference
function Base.:-(a::MySet, b::MySet)
    out = MySet()
    for x in a
        !(x in b) && add!(out, x)
    end
    return out
end

end
