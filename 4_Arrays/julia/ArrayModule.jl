module ArrayModule

    export DsArray

    struct DsArray{T} <: AbstractVector{T}
        ptr::Ptr{T}
        len::Int
    end

    function DsArray{T}(len::Int) where T
        bytes = len * sizeof(T)
        ptr = Base.Libc.malloc(bytes)
        Base.Libc.memset(ptr, 0, bytes)
        DsArray{T}(Ptr{T}(ptr), len)
    end

    Base.size(array::DsArray) = (array.len,)
    
    Base.IndexStyle(::Type{DsArray}) = IndexLinear()

    Base.getindex(array::DsArray, i::Int) = unsafe_load(array.ptr, i)

    Base.setindex!(array::DsArray, v, i::Int) = unsafe_store!(array.ptr, v, i)

    Base.iterate(array::DsArray, state=1) = state > array.len ? nothing : (unsafe_load(array.ptr, state), state + 1)

    Base.finalize(array::DsArray) = Base.Libc.free(array.ptr)

    function Base.show(io::IO, array::DsArray)
        print(io, "DsArray of length $(array.len): [")
        for i in 1:array.len
            i > 1 && print(io, ", ")
            print(io, string(unsafe_load(array.ptr, i)))
        end
        print(io, "]")
    end

end
