
if __name__ == "__main__":
	# Read test case input from stdin
	T = int(input())

	# For each test case
	for i in range(T):

		# Read input from stdin
		s = input()

		# Placeholders
		even_string, odd_string = "", ""

		# Compute strings
		for j in range(len(s)):
			if j % 2 == 0:
				even_string += s[j]
			else:
				odd_string += s[j]

		print(f"{even_string} {odd_string}")
