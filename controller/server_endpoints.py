from flask import request, jsonify


def setup_routes(app, commands_queue):
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

    # @app.route('/initialize', methods=['POST'])
    # def initialize_robot():
    #     print("Robot is being initialized via Flask endpoint")
    #     return jsonify({"message": f"Robot initialized, listening on {host}:{port}"}), 200
    #
    # @app.route('/move_to_position', methods=['POST'])
    # def move_to_position():
    #     return jsonify({"message": "Moving to position"}), 200
    #
    # @app.route('/move_to_angles', methods=['POST'])
    # def move_to_angles():
    #     return jsonify({"message": "Moving to angles"}), 200
    #
    # @app.route('/move_angle1', methods=['POST'])
    # def move_angle1():
    #     return jsonify({"message": "a1"})
    #
    # @app.route('/move_angle2', methods=['POST'])
    # def move_angle2():
    #     return jsonify({"message": "a2"})
    #
    # @app.route('/move_angle3', methods=['POST'])
    # def move_angle3():
    #     return jsonify({"message": "a3"})
    #
    # @app.route('/sleep', methods=['POST'])
    # def sleep():
    #     return jsonify({"message": "sleeping"})
