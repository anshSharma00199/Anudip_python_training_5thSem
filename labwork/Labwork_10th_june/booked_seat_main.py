from booked_seat import *
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

booked, available = count_seats(seats)

print("Booked Seats:", booked)
print("Available Seats:", available)

print("\nFirst Available Seat:", first_available(seats))

percentage = occupancy_percentage(seats)
print("\nOccupancy Percentage:", round(percentage), "%")

display_available_seats(seats)