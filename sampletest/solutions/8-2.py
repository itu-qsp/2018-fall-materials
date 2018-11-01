# 8-2.py
import os
import sys

class Unit():

    def __init__(self, unit_text):
        """Creates a Unit from a text that describes the unit in singular and
        plural like so: 'cup(s)' or 'kg'
        """
        # strip() removes unnecessary white space
        unit_list = unit_text.strip().split('(')
        # The first element is guaranteed to be the unit
        self.singular = unit_list[0]
        if len(unit_list) > 1: # Only assign plural if it exists
            # Here I take the first element (singular) and adds
            # the second element (plural) stripped from the trailing ')'
            # Example: cups = cup + s
            self.plural = unit_list[0] + unit_list[1].replace(')','')
        else: # Here we know that the unit is only singular
            self.plural = self.singular
        # Initially leave the conversions empty
        self.conversions = {}

    def add_conversion_rate(self, unit_to, rate):
        """Adds a conversion rate from this unit to the given unit"""
        self.conversions[unit_to] = rate

    def conversion_rate(self, unit_to):
        """Reports the conversion rate to the given unit, if any"""
        # Note: This will fail if the conversion hasn't been recorded
        #       Which is fine, because then we don't know how to convert
        return self.conversions[unit_to]

    def from_quantity(self, quantity):
        """Returns the unit determined by the given quantity"""
        if quantity == 1:
            return self.singular
        else:
            return self.plural

class Ingredient():

    def __init__(self, quantity, item, unit = None, preposition = None):
        """Creates an ingredient with a quantity, item of goods, unit of
        measurement (if applicable) and possibly a preposition like 'of'"""
        self.quantity = quantity
        self.item = item
        self.unit = unit
        if not preposition:
            self.prefix = ""
        else:
            self.prefix = preposition + " "

    def scale(self, scale_factor):
        """Scales the ingredient with a factor and returns
        a string with the correct plural/singular form"""
        new_quantity = self.quantity * scale_factor
        if (self.unit):
            unit_text = self.unit.from_quantity(new_quantity) + " "
        else:
            unit_text = ""
        return str(new_quantity) + " " + unit_text + self.prefix + self.item

class Recipe():
    def __init__(self, ingredients):
        """Instantiates a new recipe from a list of Ingredients"""
        self.ingredients = ingredients

    def find_items(self, item):
        items = []
        for ingredient in self.ingredients:
            # Only accumulate if we have the same ingredient
            if ingredient.item == item:
                items.append(ingredient)
        return items

    def scale(self, scale_factor):
        """Scales all ingredient with the new scale factor and returns a 
        string that lists all the scaled ingredients"""
        ingredient_list = []
        for ingredient in self.ingredients:
            ingredient_list.append(ingredient.scale(scale_factor))
        return ingredient_list

def read_units(filename):
    """Reads units from the given file and returns a dictionary 
    where the keys are both singular and plural versions of the
    unit, and the values are the actual units that can be converted
    into singular or plural form"""
    units = {}
    with open(filename, 'r') as file_pointer:
        for line in file_pointer.readlines():
            unit = Unit(line)
            # Assign singular and plural to the dictionary
            units[unit.from_quantity(1)] = unit
            units[unit.from_quantity(2)] = unit
    return units

def read_ingredient_file(filename, units):
    """Reads a list of ingredients from a file and a dictionary of possible
    units and returns a Recipe
    
    Arguments:
    filename -- The file to read the ingredients from
    units -- A dictionary that maps singular and plural unit names to units that
             can be scaled up or down
    
    Returns:
    A Recipe object that contains a list of Ingredients
    """
    ingredients = []
    with open(filename, 'r') as file_pointer:
        for line in file_pointer.readlines():
            split_line = line.split(' ')
            quantity = int(split_line[0])
            # If we only have two items, then the second must 
            # be the food item, without any unit!
            if len(split_line) == 2:
                item = split_line[1].strip()
                unit = None
                preposition = None
            else:
                unit_text = split_line[1]
                if split_line[2] == 'of':
                    item = ' '.join(split_line[3:]).strip()
                    preposition = "of"
                else:
                    item = ' '.join(split_line[2:]).strip()
                    preposition = None
                item = item.strip() # Removes unnecessary newlines
                # Here I am assigning a unit from our existing units
                # - this will crash if the unit is not known, which
                #   is good, because that means we cannot work with 
                #   the unit in the future when we need to scale it
                unit = units[unit_text]
            ingredient = Ingredient(quantity, item, unit, preposition)
            ingredients.append(ingredient) 
    return Recipe(ingredients)

def read_conversions(filename, units):
    with open(filename, 'r') as file_pointer:
        for line in file_pointer.readlines():
            if len(line) < 3: # Don't parse lines that are empty
                continue
            text_from, text_to = line.split(' = ')
            unit_from_name = text_from[2:] # Remove the prepended '1 '
            unit_from = units[unit_from_name]
            rate, unit_to_name = text_to.strip().split(' ')
            rate = int(rate)
            # We risk that the conversion unit it not in our
            # dictionary of units, so if it isn't we have to 
            # add it
            if unit_to_name not in units:
                units[unit_to_name] = Unit(unit_to_name)
            unit_to = units.get(unit_to_name)
            # Register the conversion with the rate
            unit_from.add_conversion_rate(unit_to, rate)

def read_recipes_from_directory(directory, units):
    recipes = []
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        recipes.append(read_ingredient_file(file_path, units))
    return recipes

if __name__ == '__main__':
    # First read in all the arguments
    unit_file = sys.argv[1]
    conversion_file = sys.argv[2]
    ingredient_list_directory = sys.argv[3]

    # Then read the units
    units = read_units(unit_file)
    # Then read the conversions
    conversions = read_conversions(conversion_file, units)
    # Then read all the recipes
    recipes = read_recipes_from_directory(ingredient_list_directory, units)
    
    # Finally we can ask the user for ingredient he/she is looking for
    ingredient_name = input('What ingredient are you looking for? ')

    # Collect all the ingredients from all our recipes
    ingredients = []
    for recipe in recipes:
        recipe_ingredients = recipe.find_items(ingredient_name)
        for ingredient in recipe_ingredients:
            ingredients.append(ingredient)

    if ingredients == []:
        print("No ingredients by the name of " + ingredient_name)
    else:
        # Use the first unit as a point of reference
        first_ingredient = ingredients[0]
        first_unit = first_ingredient.unit
        total_amount = first_ingredient.quantity
        # Sum up the remaining ingredients
        for ingredient in ingredients[1:]:
            if ingredient.unit == first_unit:
                total_amount += ingredient.quantity
            else:
                total_amount += ingredient.quantity * first_unit.conversion_rate(ingredient.unit) 
        # In the case of 'duck' or 'apple' the unit is None, so it does not make
        # sense to print it
        if first_unit: 
            suffix = ' ' + first_unit.from_quantity(total_amount)
        else:
            suffix = ''
        print("Total amount of " + str(total_amount) + suffix + " " +
                ingredient_name)

