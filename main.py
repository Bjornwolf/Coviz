from simulation import Simulation
import matplotlib.pyplot as plt


sim1 = Simulation(90, 10000, 5,
                  10, 5,
                  10, 2,
                  0.1)
sim1.simulate()
infected_over_time_1 = list(map(lambda st: st.count('i'), sim1.frames))
cured_over_time_1 = list(map(lambda st: st.count('c'), sim1.frames))
healthy_over_time_1 = list(map(lambda st: st.count('h'), sim1.frames))


sim2 = Simulation(90, 10000, 5,
                  5, 2.5,
                  10, 2,
                  0.1)
sim2.simulate()
infected_over_time_2 = list(map(lambda st: st.count('i'), sim2.frames))
cured_over_time_2 = list(map(lambda st: st.count('c'), sim2.frames))
healthy_over_time_2 = list(map(lambda st: st.count('h'), sim2.frames))

sim3 = Simulation(90, 10000, 5,
                  2.5, 1.25,
                  10, 2,
                  0.1)
sim3.simulate()
infected_over_time_3 = list(map(lambda st: st.count('i'), sim3.frames))
cured_over_time_3 = list(map(lambda st: st.count('c'), sim3.frames))
healthy_over_time_3 = list(map(lambda st: st.count('h'), sim3.frames))

plt.plot(infected_over_time_1, label='bez ograniczenia kontaktow społecznych')
plt.plot(infected_over_time_2, label='ograniczamy kontakty spoleczne o 50%')
plt.plot(infected_over_time_3, label='ograniczamy kontakty spoleczne o 75%')
plt.legend(loc='upper right')
plt.show()

print(len(infected_over_time_1))
print(len(cured_over_time_1))
print(len(healthy_over_time_1))
print(len(infected_over_time_2))
print(len(cured_over_time_2))
print(len(healthy_over_time_2))
print(len(infected_over_time_3))
print(len(cured_over_time_3))
print(len(healthy_over_time_3))

labels = ['zarażeni', 'wyleczeni', 'niezarażeni']
plt.stackplot(list(range(91)), infected_over_time_1, cured_over_time_1,
              healthy_over_time_1, labels=labels)
plt.legend(loc='upper left')
plt.title("Bez ograniczenia kontaktów")
plt.show()

labels = ['zarażeni', 'wyleczeni', 'niezarażeni']
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
ax1.stackplot(list(range(91)), infected_over_time_1, cured_over_time_1,
              healthy_over_time_1, labels=labels)
ax1.legend(loc='upper left')
# ax1.title("Bez ograniczenia kontaktów")
ax2.stackplot(list(range(91)), infected_over_time_2, cured_over_time_2,
              healthy_over_time_2, labels=labels)
ax2.legend(loc='upper left')
# ax2.title("Z ograniczeniem 50%")
ax3.stackplot(list(range(91)), infected_over_time_3, cured_over_time_3,
              healthy_over_time_3, labels=labels)
ax3.legend(loc='upper left')
# ax3.title("Z ograniczeniem 75%")
plt.show()
