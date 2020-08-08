class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return self.artist + '. "' + self.title + '". ' + str(self.year) + ', ' + self.medium + ". "\
        + self.owner.name + ', ' + self.owner.location + '.'

class Marketplace:
    def __init__(self):
        self.listing = []

    def add_listing(self, new_listing):
        self.listing.append(new_listing)
    
    def remove_listing(self, rem_listing):
        self.listing.remove(rem_listing)

    def show_listings(self):
        for item in self.listing:
            print(item)

class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.is_museum = is_museum
        if is_museum:
            self.location = location
        else:
            self.location = 'Private Collection'

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            art_listing = None
            for listing in veneer.listing:
                if listing.art == artwork:
                    art_listing = listing
                    break
            if art_listing != None:
                art_listing.art.owner = self
                veneer.remove_listing(art_listing)

class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return '%s, %s.' % (self.art.title, self.price)

artist = 'Picasso, Pablo'
title = 'Girl with Mandolin (Fanny Tellier)'
year = 1910
medium = 'oil on canvas'

edytta = Client('Edytta Halpirt', None, False)
moma = Client('The MOMA', 'New York', True)

girl_with_mandolin = Art(artist, title, medium, year, edytta)
print(girl_with_mandolin)
veneer = Marketplace()
edytta.sell_artwork(girl_with_mandolin, '6M USD')
veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()

