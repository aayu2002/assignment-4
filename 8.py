def reorder_array(nums):
  result = []
  for i in range(0, len(nums), 2):
    result.append(nums[i])
    result.append(nums[i + 1])
  return result


if __name__ == "__main__":
  nums = [2, 5, 1, 3, 4, 7]
  print(reorder_array(nums))
