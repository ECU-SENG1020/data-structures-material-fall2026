module IntegerArrayModule

    export IntArray

    struct IntArray <: AbstractVector{Int}
        ptr::Ptr{Int}
        len::Int
    end

    function IntArray(len::Int)
        len < 0 && throw(ArgumentError("length must be non-negative"))
        bytes = len * sizeof(Int)
        ptr = Base.Libc.malloc(bytes)
        Base.Libc.memset(ptr, 0, bytes)
        IntArray(Ptr{Int}(ptr), len)
    end

    # function Base.size(array::IntArray)
    #     return (array.len,)
    # end


    Base.size(array::IntArray) = (array.len,)
    Base.IndexStyle(::Type{IntArray}) = IndexLinear()

    Base.getindex(array::IntArray, i::Int) = unsafe_load(array.ptr, i)
    Base.setindex!(array::IntArray, v::Int, i::Int) = unsafe_store!(array.ptr, v, i)

    Base.iterate(array::IntArray, state=1) = state > array.len ? nothing : (unsafe_load(array.ptr, state), state + 1)

    Base.finalize(array::IntArray) = Base.Libc.free(array.ptr)

    function Base.show(io::IO, array::IntArray)
        print(io, "IntArray of length $(array.len): [")
        for i in 1:array.len
            i > 1 && print(io, ", ")
            print(io, unsafe_load(array.ptr, i))
        end
        print(io, "]")
    end

end
