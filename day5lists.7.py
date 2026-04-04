nums = [5,2,9,1,7]
nums.append(0)
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
print("maximum:",max(nums))
print("Average:",sum(nums)/len(nums))