import math

def calculate_panels(room_length, room_width, panel_length, panel_width, panels_per_package):
    room_area = (room_length * room_width) * 1.1
    panel_area = panel_length * panel_width
    panels_needed = math.ceil(room_area / panel_area)
    packages_needed = math.ceil(panels_needed / panels_per_package)
    return packages_needed

#Na przykład:
room_length = 12
room_width = 6
panel_length = 2
panel_width = 0.4
panels_per_package = 12

packages_needed = calculate_panels(room_length, room_width, panel_length, panel_width, panels_per_package)

print("Panel boxes needed: ", packages_needed)