
def solve(meal_cost, tip_percent, tax_percent):
	actual_tip = meal_cost * (tip_percent / 100)
	actual_tax = meal_cost * (tax_percent / 100)
	total_cost = meal_cost + actual_tax + actual_tip
	print(round(total_cost))


if __name__ == "__main__":
	meal_cost = float(input())
	tip_percent = int(input())
	tax_percent = int(input())

	solve(meal_cost, tip_percent, tax_percent)
