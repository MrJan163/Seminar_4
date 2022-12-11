# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.



import random
nums = []
for el in range(30):
    nums.append(random.randint(0,30))
print(nums)
for el in range(len(nums)):
    min_index = el
    for j in range(el, len(nums)):
        if nums[j] < nums[min_index]: min_index = j
    nums[el], nums[min_index] = nums[min_index], nums[el]
print(nums)
print(len(nums))