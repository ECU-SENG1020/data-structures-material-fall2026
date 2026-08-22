

def selection_sort(numbers):
   """Sort the list `numbers` in place using selection sort.

   Selection sort works by repeatedly finding the smallest remaining
   element and swapping it into the next position. This implementation
   modifies the input list directly.
   """
   # [10, 2, 78, 4, 45, 32, 7, 11] 
   #  [2,10, 78, 4, 45, 32, 7, 11] 
   # [2,4, 78, 10, 45, 32, 7, 11] 
   # We go from the first element to the second-to-last element
   # because each step places the correct item at position i.
   for i in range(len(numbers) - 1):

      # Assume the smallest element is at position i
      index_smallest = i

      # Look through the rest of the list to find the true smallest
      for j in range(i + 1, len(numbers)):
         if numbers[j] < numbers[index_smallest]:
            index_smallest = j

      # Swap the current value at i with the smallest we've found
      # This places the smallest remaining element into position i
      temp = numbers[i]
      numbers[i] = numbers[index_smallest]
      numbers[index_smallest] = temp


def selection_sort_with_counts(numbers):
   """Selection sort that also returns the number of comparisons made.

   Returns a tuple: (comparisons, swaps). This is useful for teaching
   to show how much work the algorithm does on a given input.
   """
   comparisons = 0
   swaps = 0
   # Make a copy so callers can still inspect the original if needed
   nums = list(numbers)

   for i in range(len(nums) - 1):
      index_smallest = i
      for j in range(i + 1, len(nums)):
         comparisons += 1
         if nums[j] < nums[index_smallest]:
            index_smallest = j

      # Swap and count the swap
      nums[i], nums[index_smallest] = nums[index_smallest], nums[i]
      swaps += 1

   return nums, comparisons, swaps


def main():
   # Example usage for students: a small unsorted list
   numbers = [10, 2, 78, 4, 45, 32, 7, 11]
   numbers2 = [10, 2, 78, 4, 45, 32, 7, 11]

   print("UNSORTED:")
   print(numbers)
   print()

   # Sort in place
   selection_sort(numbers)

   # Demonstration run that returns counts
   _, comps, swaps = selection_sort_with_counts(numbers2)
   print(f"(demo) comparisons={comps}, swaps={swaps}")

   print("SORTED:")
   print(numbers)


if __name__ == '__main__':
   main()