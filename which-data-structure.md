# Which Data Structure Should You Use?

1. **Question:** You are checking guests into a party and each wristband code must be unique. Which data structure should you use?
   **Answer:** set  
   **Why:** A set automatically prevents duplicates and gives fast membership checks.

2. **Question:** You need to store exactly 7 daily temperatures for one week and access by day index. Which data structure fits best?
   **Answer:** array  
   **Why:** An array is great for fixed-size, index-based storage.

3. **Question:** A train app keeps adding new cars to the front of a chain. Which data structure should you use?
   **Answer:** singly-linked list  
   **Why:** Front insertions are O(1) when you only need to update the head pointer.

4. **Question:** You store `student_id -> final_grade` and need fast lookups by ID. Which data structure is best?
   **Answer:** dictionary  
   **Why:** Dictionaries are built for key-value lookup by key.

5. **Question:** You want to store a fixed GPS coordinate `(latitude, longitude)` that should not change. Which data structure should you use?
   **Answer:** tuple  
   **Why:** A tuple is immutable and ideal for fixed records.

6. **Question:** Your reading list grows over time, order matters, and duplicates are allowed. Which data structure should you use?
   **Answer:** list  
   **Why:** A list is dynamic, ordered, and allows repeated values.

7. **Question:** You only care whether a username has been seen before, and duplicates are useless. Which data structure fits best?
   **Answer:** set  
   **Why:** Sets store unique items and support fast `in` checks.

8. **Question:** You need to store 12 fixed monthly sales slots and update by month index. Which data structure should you use?
   **Answer:** array  
   **Why:** Arrays work well for fixed-length, position-based data.

9. **Question:** You are building a simple contact book with `name -> phone number`. Which data structure should you use?
   **Answer:** dictionary  
   **Why:** Contact info is naturally key-value data.

10. **Question:** You keep a queue of tasks where new urgent tasks are inserted at the front very often. Which data structure is best?
	**Answer:** singly-linked list  
	**Why:** Frequent head insertions are efficient in a singly-linked list.  
	**Other candidates:** list

11. **Question:** You want to store a player's immutable profile `(username, level, class_type)`. Which data structure should you use?
	**Answer:** tuple  
	**Why:** A tuple protects fixed profile fields from accidental changes.

12. **Question:** You are keeping a playlist where order matters and songs can repeat. Which data structure should you use?
	**Answer:** list  
	**Why:** Lists preserve order and allow duplicates.

13. **Question:** You need to track which badges a user has earned, with no duplicates. Which data structure fits best?
	**Answer:** set  
	**Why:** A set enforces uniqueness automatically.

14. **Question:** You need `word -> count` for a paragraph analysis tool. Which data structure should you use?
	**Answer:** dictionary  
	**Why:** Counting frequencies maps each key to a numeric value.

15. **Question:** You need a fixed-size board with exactly 64 squares addressed by index. Which data structure is best?
	**Answer:** array  
	**Why:** Fixed size plus direct indexing matches array strengths.

16. **Question:** You frequently remove the first item and insert a new first item in a sequence. Which data structure should you use?
	**Answer:** singly-linked list  
	**Why:** Head updates are O(1) for insert/remove operations.

17. **Question:** You want a permanent list of days of the week that should never be edited. Which data structure should you use?
	**Answer:** tuple  
	**Why:** Tuples are immutable and ideal for constant ordered values.  
	**Other candidates:** array

18. **Question:** You maintain a shopping cart where items are added in order and can repeat. Which data structure should you use?
	**Answer:** list  
	**Why:** Lists are dynamic and preserve insertion order.

19. **Question:** You want to test if an email is in a blocked list as fast as possible, and duplicates do not matter. Which data structure fits best?
	**Answer:** set  
	**Why:** Sets are optimized for fast membership checks.

20. **Question:** You are storing configuration settings like `"theme" -> "light"` and `"timeout" -> 30`. Which data structure should you use?
	**Answer:** dictionary  
	**Why:** Settings are named fields, which map directly to keys.

21. **Question:** You have exactly 24 hourly buckets in a day and always access by hour number. Which data structure should you use?
	**Answer:** array  
	**Why:** Fixed-size indexed access is an array use case.

22. **Question:** You model a scavenger hunt path where each clue points to the next clue. Which data structure is best?
	**Answer:** singly-linked list  
	**Why:** A singly-linked list naturally represents one-way next links.

23. **Question:** You return a function result `(min_value, max_value)` that should be treated as one immutable pair. Which data structure should you use?
	**Answer:** tuple  
	**Why:** Tuples cleanly package small, fixed return records.

24. **Question:** You store comments in posting order and allow identical messages. Which data structure should you use?
	**Answer:** list  
	**Why:** Lists keep order and allow duplicate elements.

25. **Question:** You need to collect unique hashtags from a stream of posts. Which data structure fits best?
	**Answer:** set  
	**Why:** Sets deduplicate automatically while ingesting data.

26. **Question:** You need `country_code -> country_name` lookups in a travel app. Which data structure should you use?
	**Answer:** dictionary  
	**Why:** Dictionary keys provide fast direct lookups.

27. **Question:** Your game has exactly 10 inventory slots addressed as 0 through 9. Which data structure should you use?
	**Answer:** array  
	**Why:** The size is fixed and index access is required.  
	**Other candidates:** list

28. **Question:** You store steps in a process where each step points only to the next one and you often insert at the start. Which data structure is best?
	**Answer:** singly-linked list  
	**Why:** It supports pointer-based chaining and efficient head insertion.

29. **Question:** You want to store a person's fixed birth record `(year, month, day)` without modification. Which data structure should you use?
	**Answer:** tuple  
	**Why:** A tuple is ideal for fixed, immutable grouped values.

30. **Question:** You are caching API responses by endpoint URL for quick reuse. Which data structure should you use?
	**Answer:** dictionary  
	**Why:** Caching is a key-value lookup problem (`url -> response`).

31. **Question:** An online store needs a fast way to check whether a coupon code was already redeemed. Which data structure should you use?
	**Answer:** set  
	**Why:** A set gives fast membership checks and naturally keeps coupon codes unique.

32. **Question:** A payroll system stores `employee_id -> net_pay` for each pay cycle. Which data structure should you use?
	**Answer:** dictionary  
	**Why:** Payroll lookups are key-value lookups by employee ID.

33. **Question:** A retail dashboard always tracks sales for exactly 12 months in the current fiscal year. Which data structure should you use?
	**Answer:** array  
	**Why:** The size is fixed and monthly positions can be accessed by index.

34. **Question:** A customer support ticket chain always adds escalations to the front for immediate processing. Which data structure should you use?
	**Answer:** singly-linked list  
	**Why:** Frequent front insertions are efficient with head-pointer updates.

35. **Question:** A logistics app stores a package checkpoint as `(warehouse_id, timestamp)` and should not mutate it later. Which data structure should you use?
	**Answer:** tuple  
	**Why:** A tuple is ideal for fixed, immutable pairs.

36. **Question:** A CRM system keeps an ordered activity feed where duplicate event types are allowed. Which data structure should you use?
	**Answer:** list  
	**Why:** Lists preserve order and allow repeated entries.

37. **Question:** A fraud tool stores unique device fingerprints seen today. Which data structure should you use?
	**Answer:** set  
	**Why:** Fingerprints should be unique and checked quickly for prior appearance.

38. **Question:** An invoicing service stores `invoice_number -> status`. Which data structure should you use?
	**Answer:** dictionary  
	**Why:** Invoice number is a natural key for fast status retrieval.

39. **Question:** A manufacturing line has exactly 8 stations and needs slot-by-slot status updates. Which data structure should you use?
	**Answer:** array  
	**Why:** A fixed number of stations maps cleanly to indexed positions.

40. **Question:** An incident response process prepends urgent remediation steps to the start of the workflow chain. Which data structure should you use?
	**Answer:** singly-linked list  
	**Why:** Adding to the front is O(1) in a singly-linked list.

41. **Question:** A finance app returns a locked exchange quote `(currency_pair, rate)` from a pricing API. Which data structure should you use?
	**Answer:** tuple  
	**Why:** The quote is a fixed small record that should remain unchanged.

42. **Question:** A hiring pipeline stores candidate stages in order and allows multiple candidates in the same stage. Which data structure should you use?
	**Answer:** list  
	**Why:** Lists preserve sequence and allow duplicate stage values.

43. **Question:** A marketing platform needs a unique collection of active campaign tags for the day. Which data structure should you use?
	**Answer:** set  
	**Why:** A set deduplicates tags automatically.

44. **Question:** A SaaS app stores feature flags as `flag_name -> enabled`. Which data structure should you use?
	**Answer:** dictionary  
	**Why:** Feature flags are key-value settings keyed by name.

45. **Question:** A call center tracks exactly 24 hourly call-volume buckets each day. Which data structure should you use?
	**Answer:** array  
	**Why:** This is fixed-size, index-addressable time-series data.

46. **Question:** A banking workflow links each approval step to exactly one next step and often inserts a new first review step. Which data structure should you use?
	**Answer:** singly-linked list  
	**Why:** One-direction chaining with fast head insertion matches singly-linked lists.

47. **Question:** An e-commerce order key is always represented as `(store_id, order_id)` and should stay immutable. Which data structure should you use?
	**Answer:** tuple  
	**Why:** A tuple cleanly models an immutable composite key.

48. **Question:** A project tool stores sprint tasks in the order they were added, even if names repeat. Which data structure should you use?
	**Answer:** list  
	**Why:** Ordered sequences with duplicates are list-friendly.

49. **Question:** A compliance team records which policy IDs each employee acknowledged and each ID should appear once. Which data structure should you use?
	**Answer:** set  
	**Why:** Sets enforce one-time inclusion per policy ID.  
	**Other candidates:** list

50. **Question:** A POS system stores `sku -> current_price` for instant register lookups. Which data structure should you use?
	**Answer:** dictionary  
	**Why:** SKU-based lookups are classic key-value access.
