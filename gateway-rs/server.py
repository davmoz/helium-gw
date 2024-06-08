from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Path to settings.toml file
settings_path = '/app/settings.toml'

@app.route('/start_gateway', methods=['POST'])
def start_gateway():
    try:
        # Start the helium_gateway with the specified config file
        subprocess.Popen(['./helium_gateway', '-c', settings_path, 'server'])
        return jsonify({"message": "helium_gateway started successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_info', methods=['GET'])
def get_info():
    try:
        # Get info from the helium_gateway
        result = subprocess.run(['./helium_gateway', '-c', settings_path, 'key', 'info'], capture_output=True, text=True)
        return jsonify({"info": result.stdout}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add_gateway', methods=['POST'])
def add_gateway():
    data = request.get_json()
    owner = data.get('owner')
    payer = data.get('payer')
    mode = data.get('mode')

    if not owner or not payer or not mode:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        # Run the helium_gateway add command with the provided arguments
        result = subprocess.run([
            './helium_gateway', '-c', settings_path, 'add',
            '--owner', owner,
            '--payer', payer,
            '--mode', mode
        ], capture_output=True, text=True)

        if result.returncode == 0:
            return jsonify({"message": "Command executed successfully", "output": result.stdout}), 200
        else:
            return jsonify({"error": "Command failed", "output": result.stderr}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)