from delivery_performace import *

# Main Program
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

print("Fastest Delivery:", fastest_delivery(delivery_time), "minutes")
print("Delayed Orders:", delayed_orders(delivery_time))
print("Average Delivery Time:", round(average_delivery_time(delivery_time), 1), "minutes")

delivery_category(delivery_time)