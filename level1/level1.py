

def load_file(filename: str = "level1/level1-1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def get_rectangle_coordinates(data: list[str]) -> list:
    coordinates = data[0].split(",")
    coordinates = [float(coordinate) for coordinate in coordinates]
    return coordinates

def get_car_pos(data: list[str]) -> list:
    cars_pos = []
    for car in data[2:]:
        car_pos = car.split(",")
        car_pos = (float(car_pos[0]), float(car_pos[1]))
        cars_pos.append(car_pos)
    return cars_pos

def is_car_in_rect(rect_coordinates: list, car_pos: tuple) -> bool:
    if rect_coordinates[2] <= car_pos[0] <= rect_coordinates[0] and rect_coordinates[3] <= car_pos[1] <= rect_coordinates[2]:
        return True
    return False
    
def main(file:str):
    car_counter = 0
    data = load_file(file)
    rectangle_coordinates = get_rectangle_coordinates(data)
    cars = get_car_pos(data)
    
    for car in cars:
        if is_car_in_rect(rectangle_coordinates, car):
            car_counter += 1

    print(car_counter)
    print()
    

if __name__ == "__main__":
    for i in range(1, 5):
        main(f"level1/level1-{i}.in")

    