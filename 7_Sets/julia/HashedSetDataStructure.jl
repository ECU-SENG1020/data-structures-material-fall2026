module HashedSetDataStructure

export MyHashedSet, add!, remove!, contains

mutable struct MyHashedSet
    hash_set::Dict{UInt64,Any}
    MyHashedSet() = new(Dict{UInt64,Any}())
end

function add!(s::MyHashedSet, value)
    s.hash_set[hash(value)] = value
end

function remove!(s::MyHashedSet, value)
    h = hash(value)
    haskey(s.hash_set, h) || return
    delete!(s.hash_set, h)
end

contains(s::MyHashedSet, value) = haskey(s.hash_set, hash(value))

function Base.iterate(s::MyHashedSet, state=nothing)
    return iterate(values(s.hash_set), state)
end

function Base.show(io::IO, s::MyHashedSet)
    if isempty(s.hash_set)
        print(io, "set()")
        return
    end
    print(io, "{")
    first_item = true
    for v in values(s.hash_set)
        if !first_item
            print(io, ", ")
        end
        first_item = false
        print(io, string(v))
    end
    print(io, "}")
end

end
