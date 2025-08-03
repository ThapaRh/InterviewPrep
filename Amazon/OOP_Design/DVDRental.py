# '''
# DVD rental system
# Requirement clarification:
# 1. Users should be able to browse from collection of dvds w/o login?
# 2. In order for them to rent, they should have acc and login?
# 3. Admins should be able to add or remove dvds from collection?
# 4. Out of stock msg id dvds are out of stock?
# 5. Confirmation message with due date when dvds are due?
# 6. there will be fine if dvds aren't returned on time?
# 7. Notification day before due?
# 8. Cash/card accepted?

# Lets clarify our actors first:
# user: rents dvd
# admin:adds,removes dvd
# rentalmanager:manages rentals and stocks

# Entities:
# User
# RentalSystem
# DVD
# PaymentProcessor
# NotificationService

# class DVD():
# - id:uuid
# - name:str
# - Pricing:class
# - is_available_for_rent:bool
# - return_date:datetime
# - rent_dvd()-update the flag
# - return_dvd()-update flag back

# class Movie(DVD):
# - name
# - genre

# class Pricing():
# - float price
# increasePrice()
# decreasePrice()

# class User():
# - id:uuid
# - age:int
# - email:str
# - DvDRental:class

# class Customer(User):
# - List<DVD> rentedDvds
# - RentDvD(user_id,dvd_name,rent_start=datetime.now,rent_end)
# - ReturnDvD(user_id,dvd_name,rent_start,rent_end:datetime.now)

# class Admin(User):
# - AddDvDs(user_id,dvd_name)
# - RemoveDvD(user_id,dvd_name)

# class DvDRental():
# - List<DvD> all_dvds
# - List<User> users
# - rent_dvd(user_id,dvd_id,start_date,return_date)
# - return_dvd(user_id,dvd_id,start_date,return_date)
# - notify_customer(user_id,due_date)
# - add_dvd(user_id,dvd_id)
# - remove_dvd(user_id,dvd_id)

# class NotificationService():

# class EmailService():

# '''
# import uuid
# from enum import Enum
# from datetime import datetime
# class Pricing():
#     def __init__(self):
#         self.price = None
    
#     def set_price(self,amount:float):
#         self.price = amount
    
#     def update_price(self,amount:float):
#         pass

# class Genre(Enum):
#     Movie = "movie"
#     Game = "game"
        
# class DVD():
#     def __init__(self,pricing:Pricing,genre:Genre,name:str,user:User):
#         self.id = uuid.uuid4()
#         self.name = name
#         self.due_date = None
#         self.pricing = pricing
#         self.is_available = True
#         self.genre = genre
#         self.user = user
    
#     def set_price(self,amount:float):
#         self.pricing.set_price(amount)
    
#     def update_price(self,amount:float):
#         pass
    
#     def rent_dvd(self,number_of_days):
#         self.is_available = False
#         self.due_date = datetime.now + number_of_days
    
#     def return_dvd(self,number_of_days):
#         self.is_available = True
#         self.due_date = None
        
# class Movie(DVD):
#     def __init__(self,director:str,pricing:Pricing,name:str):
#         super().__init__(pricing,Genre.Movie,name)
#         self.director = director

# class Game(DVD):
#     def __init__(self,level:str,pricing:Pricing,name:str):
#         super().__init__(pricing,Genre.Game,name)
#         self.level = level #pro,noobie
    
# class User:
#     def __init__(self):
#         self.id = uuid.uuid3
#         self.current_rentals = []
#         self.past_rentals = []
        
# class RentalManager():
#     #this is a service class
#     def __init__(self):
#         self.all_dvds = {}#dvdid:dvdobject
#         self.users = {}#userid:userobject
        
#     def rent_dvd(self,user_id:uuid,dvd_id,number_of_days):
#         #there can be checks and filter logic before this
#         self.all_dvds[dvd_id].rent_dvd(number_of_days) #how is user info updated then?
#         self.users[user_id].current_rentals.add(self.all_dvds[dvd_id])
        
        
from datetime import datetime, timedelta
import uuid
from enum import Enum

# ----------------------- Supporting Classes -----------------------

class Pricing:
    def __init__(self, price: float):
        self.price = price

    def set_price(self, amount: float):
        self.price = amount

    def update_price(self, amount: float):
        self.price = amount

    def get_price(self) -> float:
        return self.price

class Genre(Enum):
    MOVIE = "movie"
    GAME = "game"

# ----------------------- DVD & Subclasses -----------------------

class DVD:
    def __init__(self, name: str, pricing: Pricing, genre: Genre):
        self.id = uuid.uuid4()
        self.name = name
        self.genre = genre
        self.pricing = pricing
        self.is_available = True
        self.due_date = None
        self.user = None

    def rent_dvd(self, number_of_days: int):
        self.is_available = False
        self.due_date = datetime.now() + timedelta(days=number_of_days)

    def return_dvd(self):
        self.is_available = True
        self.due_date = None
        self.user = None

    def get_due_date(self):
        return self.due_date

    def get_price(self):
        return self.pricing.get_price()

    def __str__(self):
        return f"{self.name} ({self.genre.value})"

class Movie(DVD):
    def __init__(self, name: str, pricing: Pricing, director: str):
        super().__init__(name, pricing, Genre.MOVIE)
        self.director = director

class Game(DVD):
    def __init__(self, name: str, pricing: Pricing, level: str):
        super().__init__(name, pricing, Genre.GAME)
        self.level = level

# ----------------------- User -----------------------

class User:
    def __init__(self, email: str):
        self.id = uuid.uuid4()
        self.email = email
        self.current_rentals = []
        self.past_rentals = []

    def rent_dvd(self, dvd: DVD):
        self.current_rentals.append(dvd)

    def return_dvd(self, dvd: DVD):
        if dvd in self.current_rentals:
            self.current_rentals.remove(dvd)
            self.past_rentals.append(dvd)

    def __str__(self):
        return f"User: {self.email}"

# ----------------------- Rental Manager -----------------------

class RentalManager:
    def __init__(self):
        self.all_dvds = {}  # dvd_id -> DVD
        self.users = {}     # user_id -> User

    def add_user(self, user: User):
        self.users[user.id] = user

    def add_dvd(self, dvd: DVD):
        self.all_dvds[dvd.id] = dvd

    def rent_dvd(self, user_id: uuid.UUID, dvd_id: uuid.UUID, number_of_days: int):
        dvd = self.all_dvds.get(dvd_id)
        user = self.users.get(user_id)

        if not dvd or not user:
            return {"success": False, "message": "User or DVD not found"}

        if not dvd.is_available:
            return {"success": False, "message": f"DVD '{dvd.name}' is currently not available."}

        dvd.rent_dvd(number_of_days)
        dvd.user = user
        user.rent_dvd(dvd)

        return {
            "success": True,
            "message": f"DVD '{dvd.name}' successfully rented until {dvd.due_date.date()}",
            "due_date": dvd.due_date
        }

    def return_dvd(self, user_id: uuid.UUID, dvd_id: uuid.UUID):
        dvd = self.all_dvds.get(dvd_id)
        user = self.users.get(user_id)

        if not dvd or not user:
            return {"success": False, "message": "User or DVD not found"}

        if dvd not in user.current_rentals:
            return {"success": False, "message": "This DVD is not currently rented by the user."}

        dvd.return_dvd()
        user.return_dvd(dvd)

        return {
            "success": True,
            "message": f"DVD '{dvd.name}' returned successfully."
        }

# ----------------------- Simulated Flow -----------------------

if __name__ == "__main__":
    # Create system
    rental_manager = RentalManager()

    # Create a user
    user = User("alice@example.com")
    rental_manager.add_user(user)

    # Create a DVD
    pricing = Pricing(5.0)
    movie = Movie("Inception", pricing, "Christopher Nolan")
    rental_manager.add_dvd(movie)

    # Rent the DVD
    rent_result = rental_manager.rent_dvd(user.id, movie.id, 7)
    print(rent_result)

    # Return the DVD
    return_result = rental_manager.return_dvd(user.id, movie.id)
    print(return_result)
  
    