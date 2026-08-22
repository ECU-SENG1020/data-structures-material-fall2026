# Benchmark: build a Set from a Vector vs repeated membership checks.
# Mirrors 6_Sets/python/bench_set_vs_list.py

using Random

const PARAMS = [10_000, 100_000, 500_000]
const M = 10_000

println("Julia: ", VERSION)
println("Membership queries per test: ", M, "\n")

for n in PARAMS
    data = collect(0:(n - 1))
    Random.seed!(0)
    queries = [rand(0:(n - 1)) for _ in 1:M]

    t0 = time_ns()
    s = Set(data)
    t1 = time_ns()
    set_build = (t1 - t0) / 1e9

    t0 = time_ns()
    hits_list = 0
    for q in queries
        (q in data) && (hits_list += 1)
    end
    t1 = time_ns()
    list_membership = (t1 - t0) / 1e9

    t0 = time_ns()
    hits_set = 0
    for q in queries
        (q in s) && (hits_set += 1)
    end
    t1 = time_ns()
    set_membership = (t1 - t0) / 1e9

    @assert hits_list == hits_set == M

    println("n=", n)
    println("  set build time:          ", round(set_build, digits=6), " s")
    println("  list membership (m=", M, "): ", round(list_membership, digits=6), " s")
    println("  set  membership (m=", M, "): ", round(set_membership, digits=6), " s")
    if set_membership > 0
        println("  membership speedup (list / set): ", round(list_membership / set_membership, digits=1), "x")
    end
    println()
end

println("Note: speedups vary by CPU/cache and data sizes.")
println("Interpretation: building the set is O(n) but gives ~O(1) membership; repeated vector membership is O(n) per query.")
