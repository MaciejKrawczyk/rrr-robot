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
