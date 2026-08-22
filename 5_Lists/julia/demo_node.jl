include("NodeModule.jl")
using .NodeModule: Node

node = Node("a")
node.next = Node("b")
node.next.next = Node("c")

current = node
count = 0
while current !== nothing
    println(current.data)
    count += 1
    current = current.next
end

println(count)
