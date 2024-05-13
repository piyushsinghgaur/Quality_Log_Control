from flask import Flask, request, jsonify
import logging
import json
from datetime import datetime

app = Flask(__name__)
LOG_FILES = ['log1.log', 'log2.log']  # List of log files

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

@app.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    level = data['level']
    log_string = data['log_string']
    source = data['source']
    log_to_file(level, log_string, source)
    return jsonify({'message': 'Log created successfully'}), 201

@app.route('/search', methods=['GET'])
def search_logs():
    level = request.args.get('level')
    log_string = request.args.get('log_string')
    start_timestamp = request.args.get('start_timestamp')
    end_timestamp = request.args.get('end_timestamp')
    source = request.args.get('source')

    result = []
    for log_file in LOG_FILES:
        with open(log_file, 'r') as file:
            for line in file:
                log_data = json.loads(line)
                if (level is None or log_data['level'] == level) and \
                   (log_string is None or log_data['log_string'] == log_string) and \
                   (start_timestamp is None or log_data['timestamp'] >= start_timestamp) and \
                   (end_timestamp is None or log_data['timestamp'] <= end_timestamp) and \
                   (source is None or log_data['metadata']['source'] == source):
                    result.append(log_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)