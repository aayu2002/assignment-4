def sorted_squares(nums):

  squares = []
  for num in nums:
    squares.append(num ** 2)
  squares.sort()
  return squares


if __name__ == "__main__":
  nums = [-4, -1, 0, 3, 10]
  print(sorted_squares(nums))
