class Art:
    def __init__(self, artist, title, medium, year):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year

    def __repr__(self):
        return self.artist + '. "' + self.title + '". ' + str(self.year) + ', ' + self.medium + "."

class Marketplace:
    def __init__(self):
        self.listing = []

    def add_listing(self, new_listing):
        self.listing.append(new_listing)
    
    def remove_listing(self, rem_listing):
        self.listing.remove(rem_listing)

    def show_listing(self):
        for item in self.listing:
            print(item)

class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum



artist = 'Picasso, Pablo'
title = 'Girl with Mandolin (Fanny Tellier)'
year = 1910
medium = 'oil on canvas'

girl_with_mandolin = Art(artist, title, medium, year)
veneer = Marketplace()
veneer.show_listing()

edytta = Client('Edytta Halpirt', '', False)
moma = Client('The MOMA', 'New York', True)


