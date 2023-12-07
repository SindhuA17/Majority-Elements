# Majority-Elements

Logic and algorithm :

1. Initialization:

person1, person2: Two potential persons for  elements. Initialized to float('inf') as placeholders.
countOne, countTwo: Counters for the respective persons, initialized to 0.

2. First Pass: Finding Potential persons:

Iterate through the array (nums).
If the current number is equal to person1, increment countOne.
If the current number is equal to person2, increment countTwo.
If countOne becomes 0, update person1 to the current number and reset countOne to 1.
If countTwo becomes 0, update person2 to the current number and reset countTwo to 1.
If none of the above conditions is met, decrement both countOne and countTwo.

3. Reset Counters:

Reset countOne and countTwo to 0.

4. Second Pass: Count Actual Occurrences:

Iterate through the array again.
Count the occurrences of person1 and person2.

5. Check for  Elements:

If the count of person1 is greater than ⌊ n/3 ⌋, add it to the result list.
If the count of person2 is greater than ⌊ n/3 ⌋, add it to the result list.

6. Return Result:

Return the list of elements.
