main_box = [1, [2, 3], 4, [5, [6, 7]]] ## represents a main box with other boxes that contain keys

def search_for_key(box):
    for item in box:
        if isinstance(item, list):
            print("Found box!")
            search_for_key(item)

        elif isinstance(item, int):
            print("Found key!")

search_for_key(main_box)