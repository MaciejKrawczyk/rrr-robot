import time
from functools import wraps
from multiprocessing import Process, Queue

from Motor import Motor
from Vector3 import Vector3Configuration, Vector3Cartesian
from controller.server import run_server
from controller.worker import worker_process


def check_if_initialized(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self._is_initialized is not True:
            raise Exception('Robot must be initialized first!!! run "robot.initialize()"')
        return func(self, *args, **kwargs)

    return wrapper


class RRRRobot:
    def __init__(
            self,
            motor1: Motor,
            motor2: Motor,
            motor3: Motor,
            arm_length1: float,
            arm_length2: float,
            arm_length3: float
    ):
        self.motor1 = motor1
        self.motor2 = motor2
        self.motor3 = motor3
        self.arm_length1 = arm_length1
        self.arm_length2 = arm_length2
        self.arm_length3 = arm_length3
        self._is_initialized = False
        self.commands_queue = Queue()

    def initialize(self):
        self._is_initialized = True
        Process(target=worker_process, args=(self.commands_queue, self)).start()
        Process(target=run_server, args=(self.commands_queue,)).start()

    @check_if_initialized
    def sleep(self, seconds: float):
        time.sleep(seconds)

    @check_if_initialized
    def move_to_position(self, position: Vector3Cartesian):
        print("started moving to position", position.__str__())
        time.sleep(1)
        print("moved to position successfully", position.__str__())

    @check_if_initialized
    def move_to_angles(self, angles: Vector3Configuration):
        pass

    @check_if_initialized
    def move_angle1(self, angle: float):
        pass

    @check_if_initialized
    def move_angle2(self, angle: float):
        pass

    @check_if_initialized
    def move_angle3(self, angle: float):
        pass
