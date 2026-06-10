# Function to find the fastest delivery time
def fastest_delivery(times):
    return min(times)

# Function to find all delayed orders (more than 45 minutes)
def delayed_orders(times):
    delayed = []
    for i in times:
        if i > 45:
            delayed.append(i)
    return delayed

# Function to calculate the average delivery time
def average_delivery_time(times):
    return sum(times) / len(times)

# Function to display the category of each delivery
def delivery_category(times):
    print("Categories:")
    for i in times:
        if i <= 30:
            print(i, "-> Fast")
        elif i <= 45:
            print(i, "-> Normal")
        else:
            print(i, "-> Delayed")
