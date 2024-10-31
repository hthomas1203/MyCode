RECT_WIDTH = 30
RECT_HEIGHT = 50
# Draw a circle at x, y
def draw_rect(x, y):
    rect = Rectangle(RECT_WIDTH + 15, RECT_HEIGHT - 25)
    rect.set_position(x, y)
    add(rect)

# link to the mouse click event
add_mouse_click_handler(draw_rect)
