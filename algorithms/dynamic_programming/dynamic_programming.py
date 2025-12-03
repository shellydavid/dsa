
# Example using Fibonacci sequence


"""Naive recursive solution"""
# Time: O(2^n)
# Lots of sub-problems overlap here
def fibonacci(n: int) -> int:
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))


"""Top-Down (memoization)"""
# Time: O(n) - it just goes down the height of the tree, instead of all possible branches of the tree
# Space: O(n) - call stack will also only store height of tree
def fib_memo(n: int) -> int:
	memo = {0: 0, 1: 1}
	if n in memo:
		return memo[n]
	else:
		result = fib_memo(n-1) + fib_memo(n-2)
		memo[n] = result
	return result

"""
alternative write-up:
def fib(n):
	memo = {0:0, 1:1}
	def f(x):
		if x in memo:
			return memo[x]
		else:
			memo[x] = f(x-1) + f(x-2)
			return memo[x]
	return f(n)
"""

print(fib_memo(10))




"""Bottom-Up (tabulation)"""
# Time: O(n)
# Space: O(n)
def fib_tab(n: int) -> int:
	# Keep these to avoid array indexing errors
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		results = [0] * (n+1)
		results[0] = 0  # this is redundant since it was already 0, but just for demonstration of instantiating the base cases
		results[1] = 1
		for i in range(2, n+1):
			results[i] = results[i-1] + results[i-2]
		return results[n]

print(fib_tab(10))



"""Bottom-Up w/Constant Space"""
# Time: O(n)
# Space: O(1)
def fib_tab_2(n: int) -> int:

	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		prev, curr = 0, 1
		for i in range(2, n+1):
			prev, curr = curr, prev+curr
		return curr

print(fib_tab_2(10))
