
import time


def load_file(filename: str = "level1/level1-1.in") -> list:
    polygon1 = []
    polygon2 = []
    with open(filename, "r") as file:
        points_for_1 = int(file.readline())
        for i in range(points_for_1):
            polygon1.append(file.readline().strip())
        
        points_for_2 = int(file.readline())
        for i in range(points_for_2):
            polygon2.append(file.readline().strip())

        file.readline()
        cars = [line.strip() for line in file.readlines()]

        return polygon1, polygon2, cars


def convert_to_seconds(time: str):
    time = [int(x) for x in time.split(":")]
    return time[0] * 3600 + time[1] * 60 + time[2]


def convert_input(data: list[str]):
    cars = []
    for car in data:
        id, time, lat, long = car.split(",")
        lat = float(lat)
        long = float(long)
        
        cars.append((id, time, lat, long))
    return cars


def get_polygon_coordinates(data: list[str]) -> list[float]:

    coordinates = []
    for coordinate in data:
        x,y = coordinate.split(",")
        pos = (float(x),float(y))
        coordinates.append(pos)
    return coordinates


def is_point_in_polygon(polygon, point):
    count = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1) % len(polygon)]
        if ((y1 > point[1]) != (y2 > point[1])) and \
            (point[0] < (x2 - x1) * (point[1] - y1) / (y2 - y1) + x1):
            count += 1
    return count % 2 == 1


def check_start(cars, polygon1):
    possible_cars: dict[str,list] = {}

    for car in cars:
        if convert_to_seconds("09:30:00") < convert_to_seconds(car[1]) < convert_to_seconds("10:45:00") and is_point_in_polygon(polygon1, (car[2],car[3])):
            
            if not car[0] in possible_cars:
                possible_cars.update( {car[0]: [convert_to_seconds(car[1])]} )

            else:
                possible_cars[car[0]].append(convert_to_seconds(car[1]))

    return possible_cars


def check_end(cars_to_check, possible_cars: dict[str,list[int]], polygon2):
    arrived_cars = []
    for car in cars_to_check:
        if convert_to_seconds("09:30:00") < convert_to_seconds(car[1]) < convert_to_seconds("10:45:00") \
        and is_point_in_polygon(polygon2, (car[2],car[3])) and car[0] not in arrived_cars and car[0] in possible_cars:
            for time in possible_cars[car[0]]:
                time_to_check = convert_to_seconds(car[1])
                if time_to_check > time:
                    arrived_cars.append(car[0])
                    break

    arrived_cars = sorted(arrived_cars, key=lambda x: (x[0], x[2:]))
    return arrived_cars


def main(file:str):
    start_time = time.time()
    polygon1, polygon2, cars = load_file(file)
    polygon1 = get_polygon_coordinates(polygon1)
    polygon2 = get_polygon_coordinates(polygon2)
    cars = convert_input(cars)

    possible_cars = check_start(cars, polygon1)  

    arrived_cars = check_end(cars, possible_cars, polygon2)

    print(",".join(arrived_cars))
    print(f"time_needed: {round(time.time()-start_time,2)}s")
    print("\n")


if __name__ == "__main__":
    start_time = time.time()
    for i in range(1, 5):
        main(f"level5/level5/level5-{i}.in")

    print(f"total time: {round(time.time()-start_time,2)}s")
