import numpy as np
import random
from person import Person


class Simulation(object):
    def __init__(self, simulation_length, people_no, infected_at_beginning,
                 sociability_mean, sociability_dev,
                 infection_time_mean, infection_time_dev,
                 infection_probability):
        self.simulation_length = simulation_length
        self.people_no = people_no
        self.infection_probability = infection_probability
        self.frames = []
        self.people = []
        for i in range(self.people_no):
            state = 'healthy'
            if i < infected_at_beginning:
                state = 'infected'
            sociability = np.random.normal(sociability_mean, sociability_dev)
            infection_time = np.random.normal(infection_time_mean,
                                              infection_time_dev)
            self.people.append(Person(state,
                                      max(0, int(sociability)),
                                      max(0, int(infection_time))))
        self.frames.append(self.dump())

    def simulate(self):
        for t in range(self.simulation_length):
            contacts = []
            for (i, p) in enumerate(self.people):
                p.tick()
                contacts += [i] * p.sociability
            random.shuffle(contacts)
            contacts_no = len(contacts) // 2
            infect = np.random.uniform(0.0, 1.0, size=(contacts_no,))
            infect = infect < self.infection_probability
            for c in range(contacts_no):
                c1 = 2 * c
                c2 = 2 * c + 1
                is_person1_inf = self.people[contacts[c1]].state == 'infected'
                is_person2_inf = self.people[contacts[c2]].state == 'infected'
                if infect[c] and (is_person1_inf or is_person2_inf):
                    self.people[contacts[c1]].infect()
                    self.people[contacts[c2]].infect()
            self.frames.append(self.dump())

    def dump(self):
        return ''.join(map(lambda p: p.get_state_letter(),
                       self.people))
