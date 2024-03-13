from fun import find_link_i, move_to_click


link = find_link_i()
x, y = link
x += 340
y += 220
haus = x, y
move_to_click(haus, 0)