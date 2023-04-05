
def load_file(filename: str = "level1/level1-1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def get_rectangle_coordinates(data: list[str]) -> list[float]:
    coordinates = data[0].split(",")
    coordinates = [float(coordinate) for coordinate in coordinates]
    return coordinates

def is_car_in_rect(rect_coordinates: list, car_pos: tuple) -> bool:
    if rect_coordinates[2] <= car_pos[0] <= rect_coordinates[0] and rect_coordinates[3] <= car_pos[1] <= rect_coordinates[1]:
        return True
    return False

def convert_input(data: list[str]):
    cars = []
    for car in data:
        id, time, lat, long = car.split(",")
        lat = float(lat)
        long = float(long)
        
        cars.append((id, time, lat, long))
    return cars


def check_cars_pos(rect, cars):
    cars_in_rect = []
    for car in cars:
        if is_car_in_rect(rect, (car[2],car[3])) and car[0] not in cars_in_rect:
            cars_in_rect.append(car[0])

    sorted_cars = sorted(cars_in_rect, key=lambda x: (x[0], int(x[2:])))
    print(",".join(sorted_cars))



def main(file:str):
    data = load_file(file)
    rect = get_rectangle_coordinates(data)
    cars = convert_input(data[2:])

    check_cars_pos(rect,cars)

if __name__ == "__main__":
    main("level3/level3/level3-test.in")
    for i in range(1, 4):
        main(f"level3/level3/level3-{i}.in")
