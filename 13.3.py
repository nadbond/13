class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг ресторана: {self.rating}/10")
        print()

    def update_rating(self, new_rating):
        self.rating = new_rating

restaurant1 = Restaurant("Евразия", "Европейская и азиатская кухня", "8.5")
restaurant2 = Restaurant("Шаверлэнд", "Ближневосточная кухня", "8.6")
restaurant3 = Restaurant("Такояки", "Японская кухня", "10,0")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant1.update_rating(7.9)
restaurant2.update_rating(6.2)
restaurant3.update_rating(9.0)

print("\nОбновлённые рейтинги:\n")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
