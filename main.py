import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########
# Triangle(3), square(4), pentagon(5), hexagon(6), heptagon(7), octagon(8), nonagon(9), and decagon(10)
# Random color per shape (https://trinket.io/docs/colors)
# Sides 100 length

colors = ["light pink", "aquamarine", "medium turquoise", "medium spring green", "light cyan", "medium blue", "violet", "thistle", "peach puff", "dark sea green"]


def draw_shape(num_sides):
  for _ in range(num_sides):
    angle = 360 / num_sides
    tim.forward(100)
    tim.right(angle)

for shape_side_n in range (3, 11):
  tim.color(random.choice(colors))
  draw_shape(shape_side_n)


