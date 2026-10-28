# Set Data Structure Study Guide Design

## Goal

Create a standalone, student-facing Markdown study guide for the set data structure in `7_Sets`, complementing rather than replacing the broad repository study guide.

## Audience and scope

The guide is for introductory data-structures students. It will focus on concepts and use concise Python examples, matching the existing set demos and exercises. It will not duplicate full language-specific exercise instructions or implementation code.

## Content

The guide will cover:

- What a set is and its key characteristics: uniqueness, lack of indexing, and unordered iteration.
- How hashing supports typical membership, insertion, and deletion performance, including average- and worst-case complexity.
- Creating and modifying sets, membership, iteration, and mathematical operations: union, intersection, difference, and symmetric difference.
- When sets are useful and how they differ from lists and dictionaries.
- Common pitfalls, including empty-set syntax, duplicate values, unhashable elements, and relying on iteration order.
- A short review section with questions or prompts for self-check.

Examples will use Python's built-in `set`, with output descriptions that do not assume a particular iteration order. Complexity claims will distinguish expected average-case behavior from collision-related worst-case behavior.

## File and validation

Create `7_Sets/study-guide.md`. Review the final Markdown for consistency with the repository's existing set materials and verify all examples and stated operation behavior against the Python demo. No code tests are needed for a documentation-only change.

## Out of scope

Do not modify the existing top-level study guide, exercise files, tests, or language demos. Do not add a separate guide for each programming language.
