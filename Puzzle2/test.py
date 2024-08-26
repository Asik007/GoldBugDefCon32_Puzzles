import numpy as np

# Test the function
grid_string = "FHXJQVZTFIUSUVXRLHOSQQVITCOQTHLDNEUAUOJZVHDEOSOQYLZJHELEDJIEPZAP"
coordinate_string = "A7B5D4F5G3E4G5F3E5G4E3D5F4"

grid_list = np.array(list(grid_string))
grid = np.reshape(grid_list, (8,8))
print(grid)

coord_list = np.array(list(coordinate_string))
X_coords = coord_list[::2]
X_ascii = [ord(x)-65 for x in X_coords]
Y_coords = coord_list[1::2]
Y_coords = [int(y) for y in Y_coords]
coords = zip(X_ascii, Y_coords)
final = []
for coord in coords:
    selected_cell = str(grid[coord])

    final.append(selected_cell)



print("".join(final))