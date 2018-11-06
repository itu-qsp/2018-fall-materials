class Mario():
    def __init__(self, star):
        self.mario_x = 0
        self.mario_y = 0

        self.star_x = star[0]
        self.star_y = star[1]

        self.points = 0

    def up(self):
        self.mario_y += 1
        if (self.mario_x == self.star_x and self.mario_y == self.star_y):
            self.points += 1


m = Mario((0, 2))

print(m.points)
m.up()
m.up()
print(m.points)
