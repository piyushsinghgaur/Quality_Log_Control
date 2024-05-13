# Import necessary libraries
from flask import Flask, request, jsonify
import logging
import json
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
LOG_FILES = ['log1.log', 'log2.log']  # List of log files

# Function to log data to file
def log_to_file(level, log_string, source):
    log_data = {
        "level": level,
        "log_string": log_string,
        "timestamp": datetime.utcnow().isoformat(),
        "metadata": {
            "source": source
        }
    }
    logging.basicConfig(filename=source, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(json.dumps(log_data))

# Route for logging data
@app.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    level = data['level']
    log_string = data['log_string']
    source = data['source']
    log_to_file(level, log_string, source)
    return jsonify({'message': 'Log created successfully'}), 201

# Route for searching logs
@app.route('/search', methods=['GET'])
def search_logs():
    level = request.args.get('level')
    log_string = request.args.get('log_string')
    timestamp_start = request.args.get('timestamp_start')
    timestamp_end = request.args.get('timestamp_end')
    source = request.args.get('source')

    results = []
    for log_file in LOG_FILES:
        with open(log_file, 'r') as file:
            for line in file:
                log_data = json.loads(line)
                if (level is None or log_data['level'] == level) and \
                   (log_string is None or log_string in log_data['log_string']) and \
                   ((timestamp_start is None and timestamp_end is None) or \
                   (timestamp_start <= log_data['timestamp'] <= timestamp_end)) and \
                   (source is None or log_data['metadata']['source'] == source):
                        results.append(log_data)
    return jsonify(results)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
