class Solution:

    def calculate_time_between_floor(self, floor1: int, floor2: int) -> int:
        return abs(floor1 - floor2)

    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        sum = 0
        elevator_position = 0

        for i in range(len(requests)):
            sum += self.calculate_time_between_floor(elevator_position, requests[i])
            elevator_position = requests[i]

        return sum

if __name__ == "__main__":
    n = 5
    requests = [2, 1, 4, 3]

    solution = Solution()
    answer = solution.elevatorRequests(n=n, requests=requests)
    print(answer)