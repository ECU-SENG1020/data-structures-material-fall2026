# Benchmark: dictionary key lookup vs vector scan.
# Mirrors the spirit of 7_Sets/julia/bench_set_vs_list.jl.

using Random

const PARAMS = [10_000, 100_000, 500_000]
const M = 10_000

println("Julia: ", VERSION)
println("Key lookup queries per test: ", M, "\n")

for n in PARAMS
    entries = [("k_" * string(i), i) for i in 0:(n - 1)]
    Random.seed!(0)
    queries = ["k_" * string(rand(0:(n - 1))) for _ in 1:M]

    t0 = time_ns()
    d = Dict(entries)
    t1 = time_ns()
    dict_build = (t1 - t0) / 1e9

    t0 = time_ns()
    hits_scan = 0
    for q in queries
        found = false
        for (k, _) in entries
            if k == q
                found = true
                break
            end
        end
        found && (hits_scan += 1)
    end
    t1 = time_ns()
    vector_scan = (t1 - t0) / 1e9

    t0 = time_ns()
    hits_dict = 0
    for q in queries
        haskey(d, q) && (hits_dict += 1)
    end
    t1 = time_ns()
    dict_lookup = (t1 - t0) / 1e9

    @assert hits_scan == hits_dict == M

    println("n=", n)
    println("  dict build time:            ", round(dict_build, digits=6), " s")
    println("  vector scan lookup (m=", M, "): ", round(vector_scan, digits=6), " s")
    println("  dict key lookup (m=", M, "):   ", round(dict_lookup, digits=6), " s")
    if dict_lookup > 0
        println("  lookup speedup (vector / dict): ", round(vector_scan / dict_lookup, digits=1), "x")
    end
    println()
end

println("Note: speedups vary by CPU/cache and data sizes.")
println("Interpretation: building the dictionary is O(n), repeated key lookups are typically O(1).")
