def max_integer_count(m, n, ops):
  max_integer = 0
  count = 0
  for ai, bi in ops:
    for i in range(ai):
      for j in range(bi):
        if M[i][j] > max_integer:
          max_integer = M[i][j]
        elif M[i][j] == max_integer:
          count += 1
  return count


if __name__ == "__main__":
  m = 3
  n = 3
  ops = [[2, 2], [3, 3]]
  print(max_integer_count(m, n, ops))
