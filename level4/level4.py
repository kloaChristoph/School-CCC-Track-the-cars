
def load_file(filename: str = "level1/level1-1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def convert_input(data: list[str]):
    start_index = int(data[0]) + 2
    cars = []
    for car in data[start_index:]:
        lat, long = car.split(",")
        lat = float(lat)
        long = float(long)
        
        cars.append((lat,long))
    return cars


def get_polygon_coordinates(data: list[str]) -> list[float]:
    point_count = int(data[0])
    coordinates = []
    for i in range(1,point_count+1):
        x,y = data[i].split(",")
        pos = (float(x),float(y))
        coordinates.append(pos)
    return coordinates


def is_point_in_polygon(polygon, point):
    # point: (x, y)
    # polygon: list of (x, y) tuples
    
    # Check if point is inside polygon
    count = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1) % len(polygon)]
        if ((y1 > point[1]) != (y2 > point[1])) and \
            (point[0] < (x2 - x1) * (point[1] - y1) / (y2 - y1) + x1):
            count += 1
    return count % 2 == 1


def check_cars_pos(polygon, cars):
    car_in_polygon = 0
    for car in cars:
        if is_point_in_polygon(polygon, (car[0],car[1])):
            car_in_polygon += 1

    print(car_in_polygon)


def main(file:str):
    data = load_file(file)
    polygon = get_polygon_coordinates(data)
    cars = convert_input(data)

    check_cars_pos(polygon, cars)


if __name__ == "__main__":
    #main("level4/level4/level4-test.in")
    for i in range(1, 5):
        main(f"level4/level4/level4-{i}.in")
