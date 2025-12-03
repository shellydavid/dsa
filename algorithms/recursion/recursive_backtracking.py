
# Ex: Subsets problem
# Find all possible subsets of a given input array

def subsets(nums: list[int]) -> list[list[int]]:
	res, sol = [], []  # Global variables res/sol
	n = len(nums)

	def backtrack(i):
		if i == n:  # Base case
			res.append(sol[:])
			return

		else:
			# Don't pick nums[i]
			backtrack(i + 1)

			# Pick nums[i]
			sol.append(nums[i])
			backtrack(i + 1)
			sol.pop()  # undo/backtrack

	backtrack(0)
	return res


result = subsets([1, 2, 3])
print(result)
