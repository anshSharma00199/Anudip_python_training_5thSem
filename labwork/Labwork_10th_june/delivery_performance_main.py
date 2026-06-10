from delivery_performance import *

# Main Program

# List of delivery times
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# Display fastest delivery
print("Fastest Delivery:", fastest_delivery(delivery_time), "minutes")

# Display delayed orders
print("Delayed Orders:", delayed_orders(delivery_time))

# Display average delivery time
print("Average Delivery Time:", round(average_delivery_time(delivery_time), 1), "minutes")

# Display delivery categories
delivery_category(delivery_time)