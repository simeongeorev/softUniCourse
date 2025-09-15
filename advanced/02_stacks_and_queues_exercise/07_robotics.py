from collections import deque


class Robot:
    def __init__(self, name, processing_time):
        self.name = name
        self.processing_time = processing_time
        self.availability = True
        self.time_to_finish = 0

    def work(self, current_time):
        if self.availability:
            self.time_to_finish = current_time + self.processing_time
            self.availability = False

    def is_free(self, current_time):
        if current_time >= self.time_to_finish:
            self.availability = True
        return self.availability

def format_seconds(seconds):
    seconds = seconds % (24 * 3600) # done by AI
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

robots_details = input().split(";")
robots_list = []

for robot_details in robots_details:
    robot_details = robot_details.split("-")
    robots_list.append(Robot(robot_details[0], int(robot_details[1])))

starting_time_raw = input().split(":")
time = int(starting_time_raw[0]) * 3600 + int(starting_time_raw[1]) * 60 + int(starting_time_raw[2])

products_queue = deque()

while (addition := input()) != "End":
    products_queue.append(addition)

while products_queue:
    time += 1

    for robot in robots_list: # done by AI
        robot.is_free(time)

    free_robot = False

    for robot in robots_list:
        if robot.availability:
            robot.work(time)
            free_robot = True
            print(f"{robot.name} - {products_queue.popleft()} [{format_seconds(time)}]")
            break

    if not free_robot:
        products_queue.rotate(-1)


