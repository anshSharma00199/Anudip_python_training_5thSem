from booked_seat import *

#Seats Available and booked
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

#To count the seat whether it is booked or available
booked, available = count_seats(seats)

#To print the booked and Avaiblbe Seats
print("Booked Seats:", booked)
print("Available Seats:", available)

#print Available Seats
print("\nFirst Available Seat:", first_available(seats))

#To print the rounded percentage of Booked seats
percentage = occupancy_percentage(seats)
print("\nOccupancy Percentage:", round(percentage), "%")

display_available_seats(seats)