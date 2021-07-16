'''Write a class train which has method to book a ticket ,get status (no of seat )
and get fare information of train running under nepal railway'''


class Train:
    ticket = "Book a ticker"

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is: {self.name} ")
        print(f"The seat availblein the train are: {self.seats} ")

    def getFare(self):
        print(f"The price of the ticket is: Rs.{self.fare} ")

    def bookTicket(self):
        if(self.seats > 0):
            print(
                f"Your ticket has been booked!You seat number is {self.seats}")
            self.seats = self.seats-1
        else:
            print("Sorry this train is full")
info = Train("Janakpur Express:4003", 95, 10)
info.getStatus()
info.getFare()
info.bookTicket()
info.bookTicket()
info.getStatus()
