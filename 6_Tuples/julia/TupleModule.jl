module TupleModule

export DsTuple, count, index

mutable struct DsTuple
    items::Vector{Any}

    function DsTuple(args...)
        if length(args) == 0
            throw(ArgumentError("DsTuple requires at least one item"))
        end
        return new(Any[args...])
    end
end

Base.length(t::DsTuple) = length(t.items)

function Base.show(io::IO, t::DsTuple)
    if length(t) == 1
        print(io, "(", string(t.items[1]), ",)")
        return
    end
    print(io, "(")
    for (i, item) in enumerate(t.items)
        i > 1 && print(io, ", ")
        print(io, string(item))
    end
    print(io, ")")
end

function Base.iterate(t::DsTuple, state::Int=1)
    state > length(t.items) && return nothing
    return (t.items[state], state + 1)
end

Base.in(value, t::DsTuple) = any(item -> item == value, t.items)

Base.getindex(t::DsTuple, i::Int) = t.items[i]

function Base.:+(a::DsTuple, b)
    b isa DsTuple || return nothing
    return DsTuple((a.items..., b.items...)...)
end

function Base.:*(t::DsTuple, n::Int)
    new_items = Any[]
    for _ in 1:n
        append!(new_items, t.items)
    end
    return DsTuple(new_items...)
end

function count(t::DsTuple, value=nothing)
    value === nothing && return 0
    total = 0
    for item in t.items
        item == value && (total += 1)
    end
    return total
end

function index(t::DsTuple, value)
    value === nothing && return -1
    for (i, item) in enumerate(t.items)
        item == value && return i - 1  # match the Python version's 0-based index return
    end
    return -1
end

end
