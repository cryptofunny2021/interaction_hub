contract InteractionHub:

    def __init__(self):
        self.logs = []

    def call_contract(self, name, method, payload):
        self.logs.append({
            "contract": name,
            "method": method,
            "payload": payload
        })
        return "executed"

    def get_logs(self):
        return self.logs

def log_event(self, event_type, data):
    self.logs.append({
        "type": event_type,
        "data": data
    })
