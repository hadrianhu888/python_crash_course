sandwich_orders = ['tuna', 'egg', 'pastrami', 'bacon', 'pastrami', 'sausage', 'cheese', 'pastrami']
finished_sandwiches = []
while sandwich_orders: 
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    for sandwich in finished_sandwiches: 
        print(f"I finished making the '{sandwich} sandwich.'")

print(finished_sandwiches)

