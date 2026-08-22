# Precompile runner for 1_efficiency.jl
# This file loads `1_efficiency.jl` even if it contains markdown code fences,
# evaluates its contents into `Main`, and then calls representative functions
# to force compilation of commonly-used method specializations.

script_path = joinpath(@__DIR__, "1_efficiency.jl")
raw = read(script_path, String)

# Remove a leading ```...\n fence and a trailing ``` fence if present.
clean = replace(raw, r"^```.*\n" => "")
clean = replace(clean, r"\n```[ \t]*$" => "")

include_string(Main, clean, script_path)

# Call functions with representative inputs to trigger compilation.
try
    get_even_numbers_version_one(from_num=2, to_num=100_000)
    get_even_numbers_version_two(from_num=2, to_num=100_000)
catch err
    # If functions aren't defined or fail, print a warning but don't error.
    @warn "Precompile runner encountered an error" error=err
end
