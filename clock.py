class Clock:
    def __init__(self):
        self.second = 0
        self.tick = 0
        self.action_sec = 0
        self.action_ms = 0
        self.action_tick = 0
        self.counting_action_tick = False

    def inc_tick(self):
        self.tick += 1
        if self.counting_action_tick:
            self.action_tick += 1
            if self.action_tick % 120 == 0 and self.action_tick != 0:
                self.action_sec += 1
                self.action_ms = 0
            if self.action_tick % 12 == 0 and self.action_tick != 0:
                self.action_ms += 10
        if self.tick % 120 == 0:
            self.second += 1

    def start_counting_action_tick(self):
        self.counting_action_tick = True
