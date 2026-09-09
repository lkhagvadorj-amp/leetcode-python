from dataclasses import dataclass


@dataclass
class Coordinate:
    x: int
    y: int


@dataclass
class Drone:
    coordinate: Coordinate
    range: int


class Solution:
    def calculate_manhattan_distance(
        self, position: Coordinate, target: Coordinate
    ) -> int:
        return abs(position.x - target.x) + abs(position.y - target.y)

    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        drones_position = []
        target_position = Coordinate(x=target[0], y=target[1])

        for drone in drones:
            drones_position.append(
                Drone(coordinate=Coordinate(x=drone[0], y=drone[1]), range=drone[2])
            )

        print(drones_position)
        print(target_position)

        min_drone_position = -1
        min_manhattan_distance = float("inf")

        for i in range(len(drones_position)):
            manhattan_distance = self.calculate_manhattan_distance(
                position=drones_position[i].coordinate, target=target_position
            )
            if (manhattan_distance <= drones_position[i].range and manhattan_distance < min_manhattan_distance):
                min_drone_position = i
                min_manhattan_distance = manhattan_distance

        return min_drone_position

if __name__ == "__main__":

    drones = [[4, 4, 5]]
    target = [8, 6]

    solution = Solution()
    answer = solution.nearestDrone(drones=drones, target=target)
    print(answer)