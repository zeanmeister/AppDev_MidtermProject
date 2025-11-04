def check_budget(item, budget):
    if item["price"] <= budget:
        print(" Within budget")
    else:
        print("Over budget")

item = {"name": "Cabbage", "price": 60}
check_budget(item, 50)  # Set breakpoint here to inspect variables
