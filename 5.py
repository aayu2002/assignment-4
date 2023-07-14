def staircase_rows(n):

  current_row = 1
  complete_rows = 0
  while n >= current_row:
    complete_rows += 1
    n -= current_row
    current_row += 1
  return complete_rows


if __name__ == "__main__":
  n = 5
  print(staircase_rows(n))
