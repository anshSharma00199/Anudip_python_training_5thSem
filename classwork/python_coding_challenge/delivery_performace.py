delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# Fastest, Slowest, Average
print("Fastest Delivery:", min(delivery_times), "minutes")
print("Slowest Delivery:", max(delivery_times), "minutes")
print("Average Delivery Time:", sum(delivery_times) / len(delivery_times), "minutes")

# Delayed Orders
delayed_orders = []
fast = 0
normal = 0
delayed = 0

for time in delivery_times:
    if time <= 30:
        fast += 1
    elif time <= 45:
        normal += 1
    else:
        delayed += 1
        delayed_orders.append(time)

print("Delayed Orders:", delayed_orders)

print("Fast Deliveries:", fast)

print("Normal Deliveries:", normal)

print("Delayed Deliveries:", delayed)
