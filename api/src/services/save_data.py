from .hash_data import hash_data


def save_data_state(subscribers, config, state):
    data_hash = hash_data(config["city"], config["currency"], config["banks"])
    subscribers[data_hash]["state"] = state
