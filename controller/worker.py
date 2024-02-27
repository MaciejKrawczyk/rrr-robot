import time

from Vector3 import Vector3Cartesian


def worker_process(queue, robot):
    while True:
        if not queue.empty():
            command = queue.get()
            print(f"Processing command: {command}")
            time.sleep(1)  # Simulate a task
            robot.move_to_position(Vector3Cartesian(1, 1, 1))
            print(f"finished processing command {command}")
        else:
            time.sleep(0.1)  # Reduce CPU usage
