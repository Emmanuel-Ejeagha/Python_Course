# class Boy:
#     """Explains about a boy"""
#
#     def __init__(self, name, age):
#         """Initializes the boy's name and age"""
#         self.name = name
#         self.age = age
#
#     def boy_games(self):
#         """Games that boys love most"""
#         print(f"{self.name.title()} loves to play football.")
#
#     def boy_food(self):
#         """Food that boys loves to eat"""
#         print(f"{self.name.title()} loves fufu")
#
# my_boy = Boy('Chuks', 2)
# your_boy = Boy('vincent', 7)
#
# print(f"My name is {my_boy.name}")
# print(f"{my_boy.name} is {my_boy.age} years old")
# my_boy.boy_games()
# my_boy.boy_food()
#
# print(f"\n\nMy name is {your_boy.name.title()}")
# print(f"{your_boy.name.title()} boy is {your_boy.age} years old")
# your_boy.boy_games()
# your_boy.boy_food()


# class Restaurant:
#     """This a class of restaurant"""
#
#     def __init__(self, restaurant_name, cuisine_type, city):
#         """Initalize the restaurant attributes"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.city = city
#
#     def describe_restaurant(self):
#         """This describes a restaurant"""
#         print(f"The name of this restaurant is {self.restaurant_name.title()}")
#         print(f"The type of cuisine of this restaurant is {self.cuisine_type.title()}")
#         print(f"{self.restaurant_name.title()} is in {self.city.title()}")
#
#     def open_restaurant(self):
#         """informs that the restaurant is open"""
#         print(f"{self.restaurant_name.title()} is open!")
#
# restaurant = Restaurant('mega chicken', 'french food', 'lagos')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# print(f"it deals with all kinds of {restaurant.cuisine_type.title()}")
# print(f"{restaurant.restaurant_name.title()} is located in {restaurant.city.title()}")
# print(help(Restaurant))

class User:
    """Describes a user"""

    def __init__(self, first_name, last_name, age, gender, nationality):
        """Initialises the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.nationality = nationality

    def describe_user(self):
        """Data of the user"""
        print(f"User's first name: {self.first_name.title()}")
        print(f"User's last namw: {self.last_name.title()}")
        print(f"User's age: {self.age}")
        print(f"User's gender: {self.gender}")
        print(f"User's nationality {self.nationality.title()}")

    def greet_user(self):
        """Greet the user"""
        my_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Hello, {my_name}")


user = User('emmanuel', 'izrael', 21, 'Male', 'biafran')
user.describe_user()
user.greet_user()
