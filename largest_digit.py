"""
File: largest_digit.py
Name: 溫孟哲
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: The integer to find the largest digit in.
	:return: The largest digit found in the integer.
	"""
	# convert negative n into positive
	if n < 0:
		n = -n
	# base case
	if n < 10:
		return n
	else:
		last_digit = n % 10
		remain_digit = n // 10
		max_digit = find_largest_digit(remain_digit)
		if last_digit > max_digit:
			return last_digit
		return max_digit


if __name__ == '__main__':
	main()
