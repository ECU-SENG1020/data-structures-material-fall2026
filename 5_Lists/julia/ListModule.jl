module ListModule

include("NodeModule.jl")
using .NodeModule: Node

export DsList, append!, insert!, remove_at!, clear!, extend!

"""A simple singly linked list."""
mutable struct DsList
    head::Union{Nothing, Node}
end

DsList() = DsList(nothing)

function append!(list::DsList, data)
    if list.head === nothing
        list.head = Node(data)
        return list
    end

    current = list.head
    while current.next !== nothing
        current = current.next
    end

    current.next = Node(data)
    return list
end

function _node_at(list::DsList, index::Int)
    if index < 1
        throw(BoundsError(list, index))
    end

    current = list.head
    i = 1
    while current !== nothing
        if i == index
            return current
        end
        current = current.next
        i += 1
    end

    throw(BoundsError(list, index))
end

Base.length(list::DsList) = begin
    count = 0
    current = list.head
    while current !== nothing
        count += 1
        current = current.next
    end
    count
end

Base.getindex(list::DsList, index::Int) = _node_at(list, index).data

function Base.setindex!(list::DsList, value, index::Int)
    _node_at(list, index).data = value
    return list
end

"""Insert BEFORE the given 1-based index."""
function insert!(list::DsList, index::Int, value)
    if index < 1
        throw(BoundsError(list, index))
    end

    if index == 1
        new_head = Node(value)
        new_head.next = list.head
        list.head = new_head
        return list
    end

    prev = _node_at(list, index - 1)
    new_node = Node(value)
    new_node.next = prev.next
    prev.next = new_node
    return list
end

function remove_at!(list::DsList, index::Int)
    if index < 1
        throw(BoundsError(list, index))
    end

    if list.head === nothing
        throw(BoundsError(list, index))
    end

    if index == 1
        list.head = list.head.next
        return list
    end

    prev = _node_at(list, index - 1)
    if prev.next === nothing
        throw(BoundsError(list, index))
    end

    prev.next = prev.next.next
    return list
end

function clear!(list::DsList)
    list.head = nothing
    return list
end

"""Extend in-place from any iterable (including another DsList)."""
function extend!(list::DsList, items)
    for item in items
        append!(list, item)
    end
    return list
end

# Make the list iterable: for x in list
function Base.iterate(list::DsList, state=list.head)
    if state === nothing
        return nothing
    end
    return (state.data, state.next)
end

# Support: value in list
function Base.in(value, list::DsList)
    for item in list
        if item == value
            return true
        end
    end
    return false
end

# Support: list3 = list1 + list2
function Base.:+(a::DsList, b::DsList)
    result = DsList()
    extend!(result, a)
    extend!(result, b)
    return result
end

# Pretty printing: [1, 2, 3] or ['a', 'b']
function Base.show(io::IO, list::DsList)
    print(io, "[")
    first = true
    for item in list
        if !first
            print(io, ", ")
        end
        first = false
        print(io, repr(item))
    end
    print(io, "]")
end

end
