import json


class Spec:

    def __init__(self):
        self.specs: list = None
        self.current_specs = None
        self.specs_index = 0

    def load_specs(self):
        self.specs = json.load(open('map.json', ))
        self.current_specs = self.specs[0]

    def increment_spec_index(self):
        self.specs_index += 1
        self.current_specs = self.specs[self.specs_index]

    def reset_spec_index(self):
        self.specs_index = 0
        self.current_specs = self.specs[self.specs_index]

    def get_specs_length(self):
        return len(self.specs)


spec = Spec()
