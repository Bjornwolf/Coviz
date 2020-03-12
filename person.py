class Person(object):
    def __init__(self, state, sociability, infection_time):
        self.state = state
        self.sociability = sociability
        self.infection_time = infection_time

    def infect(self):
        if self.state == 'healthy':
            self.state = 'infected'

    def tick(self):
        if self.state == 'infected':
            self.infection_time -= 1
            if self.infection_time == 0:
                self.state = 'cured'

    def get_state_letter(self):
        return self.state[0]
