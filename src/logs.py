import json

LOG_FILE = 'log.json'

def init_log(filepath):
    data = load_data(filepath)
    key_list = list(data.keys())

    if key_list:
        logs_key = f'logs_{len(key_list) + 1}'
    else:
        logs_key = 'logs_1'

    data[logs_key] = []

    save_data(filepath, data)



def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data
    except OSError:
        return {}

def save_log(filepath, log):
    data = load_data(filepath)

    key_list = list(data.keys())
    log_key = key_list[-1]

    if list(log) not in data[log_key]:
        data[log_key].append(log)
        print(log, len(data[log_key]))

    save_data(filepath, data)


def print_logs(filepath):
    current_log = get_current_log(filepath)

    print(current_log)


def get_current_log(filepath):
    data = load_data(filepath)

    key_list = list(data.keys())
    log_key = key_list[-1]

    return data[log_key]










