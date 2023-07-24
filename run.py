from flask import Flask, request, jsonify

from app.services.mqtt_service import MQTTService, client

app = Flask(__name__)
mqtt_service = MQTTService()


@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()

    if not data:
        return jsonify({'message': 'No data provided'}), 400

    # Process the data...
    # This will depend on the specifics of your project.
    # For example, you might want to store the data in a database, use it to update the status of a Litterbot, etc.
    print(f'Received data: {data}')

    return jsonify({'message': 'Data received'}), 200


@app.route('/command', methods=['POST'])
def send_command():
    command = request.get_json()

    if not command:
        return jsonify({'message': 'No command provided'}), 400

    # Send the command to the appropriate Litterbot...
    # This will depend on the specifics of your project.
    # For example, you might want to send the command over a network connection, use it to control a Litterbot, etc.
    print(f'Sending command: {command}')

    return jsonify({'message': 'Command sent'}), 200


@app.route('/status/<int:litterbot_id>', methods=['GET'])
def get_status(litterbot_id):
    # Get the status of the Litterbot with the given ID...
    # This will depend on the specifics of your project.
    # For example, you might want to retrieve the status from a database, compute it based on recent data, etc.
    status = f'Status of Litterbot {litterbot_id}'

    return jsonify({'status': status}), 200


if __name__ == '__main__':
    client.connect("localhost", 1883, 60)  # Connect to an MQTT broker
    app.run(host='0.0.0.0', port=65525, debug=True)
