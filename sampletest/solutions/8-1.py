# 8-1.py
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

if __name__ == '__main__':
    # First read in all the arguments
    unit_file = sys.argv[1]
    ingredient_file = sys.argv[2]
    scale = int(sys.argv[3])
    # Then read the units
    units = read_units(unit_file)
    # Then read the actual recipe 
    recipe = read_ingredient_file(ingredient_file, units)
    # Finally we can scale and print the recipe
    scaled_recipe = recipe.scale(scale)
    for line in scaled_recipe:
        print(line)


