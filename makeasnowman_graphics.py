# Constants representing the radius of the top, middle,
# and bottom snowball.
BOTTOM_RADIUS = 100
MID_RADIUS = 60
TOP_RADIUS = 30


circ = Circle(BOTTOM_RADIUS)
circ.set_color(Color.gray)
circ.set_position(get_width()/2, get_height()-BOTTOM_RADIUS)
add(circ)

circ = Circle(MID_RADIUS)
circ.set_color(Color.gray)
circ.set_position(get_width()/2, get_height() - 2 * BOTTOM_RADIUS + MID_RADIUS)
add(circ)


#circ = Circle(BOTTOM_RADIUS)
#circ.set_color(Color.gray)
#circ.set_position(get_width()/2, get_height()-TOP_RADIUS)
#add(circ)
