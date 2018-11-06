class ColourChanger:
    def __init__(self):
        self.colour_replacement = {'red': 'black', 'green': 'white'}

    def make_readable(self, colours):
        result = []
        for col in colours:
            if col in self.colour_replacement:
                result.append(self.colour_replacement[col])
            else:
                result.append(col)
        return result


c = ColourChanger()
print(c.make_readable(['red', 'green', 'white', 'pink', 'yellow', 'red']))
