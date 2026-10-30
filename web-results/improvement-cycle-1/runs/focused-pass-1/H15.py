# Offline lifecycle illustration only; these are not HTTP wire schemas.
class MockTasks:
    def __init__(self):
        self.by_request = {}
        self.states = {}

    def post(self, authorization, request_id):
        if not authorization or not request_id:
            raise ValueError('mock requires Authorization and request_id')
        if request_id not in self.by_request:
            task_id = 'task-' + str(len(self.by_request) + 1)
            self.by_request[request_id] = task_id
            self.states[task_id] = 'pending'
        return 202, self.by_request[request_id]

    def get(self, task_id):
        return self.states[task_id]

api = MockTasks()
status, task_id = api.post('example-credential', 'build-001')
assert status == 202 and api.get(task_id) == 'pending'
assert api.post('example-credential', 'build-001')[1] == task_id
api.states[task_id] = 'completed'  # Simulated worker completion, not an endpoint.
assert api.get(task_id) == 'completed'
print('Accepted is distinct from completion; duplicate identity is preserved.')
