class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return self.name + ' menu available from ' \
               + str(self.start_time) + ' to ' + str(self.end_time)

    def calculate_bill(self, purchased_items):
        total_price = 0
        for value in purchased_items:
            total_price += self.items[value]
        return total_price

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        available_menus = []
        for item in self.menus:
            if time >= item.start_time and\
                time <= item.end_time:
                available_menus.append(item)
        return available_menus

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

#BRUNCH
brunch_menu = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00,
                         'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
                         'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu('brunch', brunch_menu, 1100, 1600)

#EARLY_BIRD
early_bird_menu = {'salumeria plate': 8.00,
                   'salad and breadsticks (serves 2, no refills)': 14.00,
                   'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
                   'mushroom ravioli (vegan)': 13.50,
                   'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu('early_bird', early_bird_menu, 1500, 1800)

#DINNER
dinner_menu = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00,
                'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50,
                'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00,
                'espresso': 3.00}
dinner = Menu('dinner', dinner_menu, 1700, 2300)

#KIDS
kids_menu = {'chicken nuggets': 6.50,
             'fusilli with wild mushrooms': 12.00,
             'apple juice': 3.00}
kids = Menu('kids', kids_menu, 1100, 2100)

#AREPA
arepas_menu = {'arepa pabellon': 7.00, 'pernil arepa': 8.50,
              'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepa = Menu('arepa', arepas_menu, 1000, 2000)

#ALL_MENU
menu = [brunch, early_bird, dinner, kids, arepa]

#FRANCHISE
flagship_store = Franchise('1232 West End Road', menu)
new_installment = Franchise('12 East Mulberry Street', menu)
arepas_place = Franchise('189 Fitzgerald Avenue', menu)

#BUSINESS
name_business = "Basta Fazoolin' with my Heart"
name_business_2 = "Take a' Arepa"
franchises_list = [flagship_store, new_installment, arepas_place]
business = Business(name_business, franchises_list)
business_2 = Business(name_business_2, franchises_list)

#TESTS
# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
# print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
# print(flagship_store)
# print(flagship_store.available_menus(1700))
print(business.name)
print(business.franchises[1])
print(business.franchises[0].menus[:])



