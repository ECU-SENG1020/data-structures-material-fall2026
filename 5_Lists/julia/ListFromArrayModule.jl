module ListFromArrayModule

include(joinpath(@__DIR__, "ArrayModule.jl"))
using .ArrayModule: DsArray

export DsList, append!, insert!, remove_at!, clear!, extend!

"""A simple list backed by `ArrayModule.DsArray{Any}` with dynamic growth."""
mutable struct DsList
    arr::Union{Nothing, DsArray{Any}}
    len::Int
end

DsList(capacity::Int=4) = DsList(DsArray{Any}(capacity), 0)

function ensure_capacity!(list::DsList, mincap::Int)
    if list.arr === nothing
        list.arr = DsArray{Any}(max(mincap, 4))
        return
    end
    if list.arr.len >= mincap
        return
    end
    newcap = max(list.arr.len * 2, mincap)
    new = DsArray{Any}(newcap)
    for i in 1:list.len
        new[i] = list.arr[i]
    end
    Base.Libc.free(list.arr.ptr)
    list.arr = new
end

function append!(list::DsList, data)
    ensure_capacity!(list, list.len + 1)
    Base.setindex!(list.arr, data, list.len + 1)
    list.len += 1
    return list
end

function _elem_at(list::DsList, index::Int)
    if index < 1 || index > list.len
        throw(BoundsError(list, index))
    end
    return list.arr[index]
end

Base.length(list::DsList) = list.len

Base.getindex(list::DsList, index::Int) = _elem_at(list, index)

function Base.setindex!(list::DsList, value, index::Int)
    if index < 1 || index > list.len
        throw(BoundsError(list, index))
    end
    Base.setindex!(list.arr, value, index)
    return list
end

"""Insert BEFORE the given 1-based index."""
function insert!(list::DsList, index::Int, value)
    if index < 1 || index > list.len + 1
        throw(BoundsError(list, index))
    end
    ensure_capacity!(list, list.len + 1)
    # shift right
    for i in list.len:-1:index
        Base.setindex!(list.arr, list.arr[i], i + 1)
    end
    Base.setindex!(list.arr, value, index)
    list.len += 1
    return list
end

function remove_at!(list::DsList, index::Int)
    if index < 1 || index > list.len
        throw(BoundsError(list, index))
    end
    # shift left
    for i in index:list.len-1
        Base.setindex!(list.arr, list.arr[i + 1], i)
    end
    list.len -= 1
    return list
end

function clear!(list::DsList)
    list.len = 0
    return list
end

function extend!(list::DsList, items)
    for item in items
        append!(list, item)
    end
    return list
end

function Base.iterate(list::DsList, state=1)
    state > list.len ? nothing : (list.arr[state], state + 1)
end

function Base.in(value, list::DsList)
    for item in list
        if item == value
            return true
        end
    end
    return false
end

function Base.:+(a::DsList, b::DsList)
    result = DsList()
    extend!(result, a)
    extend!(result, b)
    return result
end

function Base.show(io::IO, list::DsList)
    print(io, "[")
    first = true
    for i in 1:list.len
        if !first
            print(io, ", ")
        end
        first = false
        print(io, repr(list.arr[i]))
    end
    print(io, "]")
end

end
