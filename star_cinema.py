class Star_cinema(): 
    hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        Star_cinema.entry_hall(self)

    
    def entry_show(self, id, movie_name, time):
        self.id = id
        self.movie_name = movie_name
        self.time = time
        info = (id, movie_name, time)
        self.show_list.append(info)        

        sitting = [['0' for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[self.id] = sitting;

    def book_seats(self, id, num_of_seats):
        if id not in self.seats:
            return
        
        booked_seats = []
        for i in range(num_of_seats): 
            while True:
                row = int(input("Enter the row number: "))
                col = int(input("Enter the col number: "))

                if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                    print("Invalid Seat Number")
                    continue

                if self.seats[id][row][col] == '1':
                    print("This seat is already booked")
                else:
                    self.seats[id][row][col] = '1'
                    booked_seats.append((row, col))
                    break
            
        if num_of_seats > 1:
            print(f"{booked_seats} are booked successfully \n")
        else:
            print(f"The seat number {booked_seats} booked succesfully \n")

    def view_show_list(self):
        for show in self.show_list:
            print(f"Show Id : {show[0]}, Movie Name : {show[1]}, Time : {show[2]}")

    def view_available_seats(self, id):
        if id not in self.seats:
            print(f"Show Id :{id} is not found")
            return
        print(f"available seats for the show id : {self.id} :")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[id][row][col] == '0':
                    print("[✔]", end=" ")
                else:
                    print("[X]", end=" ")
            print()
    

Hall1 = Hall(10, 4, 1)
Hall1.entry_show("100", "Rangbazz", "3.30 PM")
Hall1.entry_show("101", "Tufaan", "5.40 PM")

Hall2 = Hall(8, 4, 2)
Hall2.entry_show("200", "Dunki", "2.00 PM")
Hall2.entry_show("201", "Jawan", "5.00 PM")
                    
        
print("Welcome to the Largest Cinema Hall in Bangladesh\n")

while True:
    print("1. Check The Today's Show")
    print("2. View the avilability of seat")
    print("3. Book Ticket")
    print("4. Exit")

    choice = input("Enter Your choice : ")

    if choice == '1':
        for hall in Star_cinema.hall_list:
            hall.view_show_list()
    elif choice == '2':
        show_id = input("Enter the show id: ")
        for hall in Star_cinema.hall_list:
            hall.view_available_seats(show_id)
    elif choice == '3':
        show_id = input("Enter the show id: ")
        number_of_seats = int(input("Enter the Number of seats you want to book: "))
        for hall in Star_cinema.hall_list:
            hall.book_seats(show_id, number_of_seats)
    elif choice == '4':
        print("Thank You for giving us a chance to serve you")
        break
    else:
        print(f"You choice is {choice}, which is Invalid")

