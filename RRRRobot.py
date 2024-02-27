import time
from functools import wraps
from multiprocessing import Process, Queue

from flask import request

from Motor import Motor
from Vector3 import Vector3Configuration, Vector3Cartesian


def worker_process(queue: Queue):
    """Function run by the worker process"""
    while True:
        if not queue.empty():
            command = queue.get()
            print(f"Processing command: {command}")
            # Here you can add logic to process your command
            time.sleep(1)  # Simulate a task
            print(f"finished processing command {command}")
        else:
            time.sleep(0.1)  # Polling interval


def check_if_initialized(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self._is_initialized is not True:
            raise Exception('Robot must be initialized first!!! run "robot.initialize()"')
        return func(self, *args, **kwargs)

    return wrapper


commands_queue = Queue()


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

    def _run_flask_server(self):
        from flask import Flask, jsonify

        print("Starting local server...")

        host = '0.0.0.0'
        port = 5000

        app = Flask(__name__)

        @app.route('/send-command', methods=['POST'])
        def send_command():
            """Endpoint to receive commands and send them to the worker process"""
            data = request.json
            command = data.get('command')
            if command:
                commands_queue.put(command)
                return jsonify({"message": "Command received"}), 200
            else:
                return jsonify({"error": "No command provided"}), 400

        @app.route('/initialize', methods=['POST'])
        def initialize_robot():
            print("Robot is being initialized via Flask endpoint")
            return jsonify({"message": f"Robot initialized, listening on {host}:{port}"}), 200

        @app.route('/move_to_position', methods=['POST'])
        def move_to_position():
            return jsonify({"message": "Moving to position"}), 200

        @app.route('/move_to_angles', methods=['POST'])
        def move_to_angles():
            return jsonify({"message": "Moving to angles"}), 200

        @app.route('/move_angle1', methods=['POST'])
        def move_angle1():
            return jsonify({"message": "a1"})

        @app.route('/move_angle2', methods=['POST'])
        def move_angle2():
            return jsonify({"message": "a2"})

        @app.route('/move_angle3', methods=['POST'])
        def move_angle3():
            return jsonify({"message": "a3"})

        @app.route('/sleep', methods=['POST'])
        def sleep():
            return jsonify({"message": "sleeping"})

        app.run(host=host, port=port)

    def initialize(self):
        # process = Process(target=self._run_flask_server)
        # process.start()
        worker = Process(target=worker_process, args=(commands_queue,))
        worker.start()
        self._run_flask_server()
        worker.join()

    @check_if_initialized
    def sleep(self, seconds: float):
        end_time = time() + seconds
        while time() < end_time:
            pass

    @check_if_initialized
    def move_to_position(self, position: Vector3Cartesian):
        pass

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
