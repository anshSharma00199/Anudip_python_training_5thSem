'Count seats whether it is available or booked'
def count_seats(seats):
    booked = seats.count("Booked")
    available = seats.count("Available")
    return booked, available

'Returns the seat number of the first available seat.'
def first_available(seats):
    for i in range(len(seats)):
        if seats[i]=="Available":
            return i+1
        
        return -1

'Returns the percentage of occupied seats.'
def occupancy_percentage(seats):
    booked = seats.count("Booked")
    return (booked / len(seats)) * 100

'Displays all available seat numbers.'
def display_available_seats(seats):
    print("Available Seat Numbers:", end=" ")
    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1, end=" ")
    print()
        

 