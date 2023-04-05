

def load_file(filename: str = "level1/level1/level1-1.in") -> list:
    with open(filename, "r") as file:
        file.readline()
        return [line.strip() for line in file.readlines()]


def convert_input(data: list[str]):
    cars = []
    for car in data:
        id, time, lat, long = car.split(",")
        lat = float(lat)
        long = float(long)
        
        cars.append((id, time, lat, long))
    return cars

def sort_by_north(cars: list[tuple]):  
    sorted_cars = sorted(cars, key=lambda x: x[2], reverse=True)
    return sorted_cars

def sort_by_east(cars: list[tuple]):
    sorted_cars = sorted(cars, key= lambda x: x[3], reverse=True)
    return sorted_cars

def get_output(sorted_north, sorted_east):
    north_car = sorted_north[0]
    east_car = sorted_east[0]

    print(f"{north_car[0]},{north_car[1]},{east_car[0]},{east_car[1]}")


def main(file:str):
    data = load_file(file)
    cars = convert_input(data)
    sorted_by_north = sort_by_north(cars)
    sorted_by_east = sort_by_east(cars)

    get_output(sorted_by_north, sorted_by_east)


if __name__ == "__main__":
    main("level2/level2/level2-test.in")
    for i in range(1, 5):
        main(f"level2/level2/level2-{i}.in")
