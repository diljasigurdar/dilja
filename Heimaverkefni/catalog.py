class Item():
    def __init__(self, name, category):
        self.__name = name
        self.__category = category
    
    def __str__(self):
        return "Name: {}, Category: {}".format(self.__name, self.__category)

    def set_name(self, name):
        self.__name = name

    def set_category(self, category):
        self.__category = category
    
    def get_name(self):
        return self.__name


class Catalog():
    def __init__(self, catalog=''):
        self.__name = catalog
        self.__collection = []
    
    def add(self, item):
        self.__collection.append(item)
        return self.__collection
    
    def remove(self, item):
        self.__collection.remove(item)
        return self.__collection

    def set_name(self, name):
        self.__name = name
    
    def __str__(self):
        self.result_str = "Catalog {}".format(self.__name)
        for item in self.__collection:
            self.result_str += "\n\t{}".format(item)
        return self.result_str

    def find_item_by_name(self, name):
        for item in self.__collection:
            if name == item.get_name():
                index = self.__collection.index(item)
                return self.__collection[index]

    def clear(self):
        self.__collection = []

item1 = Item("Green Book", "Biography")
print(item1)

item2 = Item("The God", "Crime")
print(item2)
item2.set_name("The Godfather")
print(item2)

item3 = Item("Schindler's List", "Biography")
print(item3)
item3.set_category("Drama")
print(item3)

catalog = Catalog('Films')
catalog.add(item1)
catalog.add(item2)
catalog.add(item3)
print(catalog)

catalog.remove(item2)
print(catalog)

catalog.set_name("Favorite Movies")
print(catalog)

print(catalog.find_item_by_name("Green Book"))
print(catalog.find_item_by_name("The Godfather"))

catalog.clear()
print(catalog)
'''
Name: Green Book, Category: Biography
Name: The God, Category: Crime
Name: The Godfather, Category: Crime
Name: Schindler's List, Category: Biography
Name: Schindler's List, Category: Drama
Catalog Films:
        Name: Green Book, Category: Biography
        Name: The Godfather, Category: Crime
        Name: Schindler's List, Category: Drama
Catalog Films:
        Name: Green Book, Category: Biography
        Name: Schindler's List, Category: Drama
Catalog Favorite Movies:
        Name: Green Book, Category: Biography
        Name: Schindler's List, Category: Drama
Name: Green Book, Category: Biography
None
Catalog Favorite Movies:'''