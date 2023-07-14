def find_distinct_integers(nums1, nums2):

  result = [[], []]
  seen = set()
  for num in nums1:
    if num not in seen:
      result[0].append(num)
      seen.add(num)
  for num in nums2:
    if num not in seen:
      result[1].append(num)
      seen.add(num)
  return result


if __name__ == "__main__":
  nums1 = [1, 2, 3]
  nums2 = [2, 4, 6]
  print(find_distinct_integers(nums1, nums2))
