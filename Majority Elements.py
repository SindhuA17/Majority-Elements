#medium 2

def Element(nums):
    if not nums:
        return []

    person1, person2, countOne, countTwo = float('inf'), float('inf'), 0, 0

    for num in nums:
        if num == person1:
            countOne += 1
        elif num == person2:
            countTwo += 1
        elif countOne == 0:
            person1, countOne = num, 1
        elif countTwo == 0:
            person2, countTwo = num, 1
        else:
            countOne -= 1
            countTwo -= 1

    countOne = countTwo = 0

    for num in nums:
        if num == person1:
            countOne += 1
        elif num == person2:
            countTwo += 1

    result = []
    if countOne > len(nums) // 3:
        result.append(person1)
    if countTwo > len(nums) // 3:
        result.append(person2)

    return result


input_str = input("Enter comma-separated integers: ")
nums = list(map(int, input_str.split(',')))
print(Element(nums))