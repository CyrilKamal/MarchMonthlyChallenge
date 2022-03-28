
class Solution:
  def getFactors(self, n: int) -> List[List[int]]:
    result = []

    def defineFactors(n: int, s: int, container: List[int]) -> None:
      if n <= 1:
        if len(container) > 1:
          result.append(container.copy())
        return

      for i in range(s, n + 1):
        if n % i == 0:
          container.append(i)
          defineFactors(n // i, i, container)
          container.pop()

    defineFactors(n, 2, [])  # requirements state *factors should be in the range [2,n-1].
    return result