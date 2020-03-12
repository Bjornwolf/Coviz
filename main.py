from simulation import Simulation
import matplotlib.pyplot as plt


sim1 = Simulation(90, 1000000, 5,
                  10, 5,
                  10, 2,
                  0.1)
sim1.simulate()
infected_over_time_1 = list(map(lambda st: st.count('i'), sim1.frames))


sim2 = Simulation(90, 1000000, 5,
                  5, 2.5,
                  10, 2,
                  0.1)
sim2.simulate()
infected_over_time_2 = list(map(lambda st: st.count('i'), sim2.frames))

sim3 = Simulation(90, 1000000, 5,
                  2.5, 1.25,
                  10, 2,
                  0.1)
sim3.simulate()
infected_over_time_3 = list(map(lambda st: st.count('i'), sim3.frames))

plt.plot(infected_over_time_1, label='bez ograniczenia kontaktow społecznych')
plt.plot(infected_over_time_2, label='ograniczamy kontakty spoleczne o 50%')
plt.plot(infected_over_time_3, label='ograniczamy kontakty spoleczne o 75%')
plt.legend(loc='upper right')
plt.show()
