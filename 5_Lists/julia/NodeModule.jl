module NodeModule

export Node

"""A single node in a singly linked list."""
mutable struct Node
    data::Any
    next::Union{Nothing, Node}

    function Node(data)
        new(data, nothing)
    end
end

end
