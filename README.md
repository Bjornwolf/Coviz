# Coviz
A barebones simulation of disease spreading in society.
The simulation is intended to underline the importance of social distancing.

## Model
Each person has a sociability number, i.e. the number of interactions
with other people each day. If one of two people interacting is infected,
the other is infected (with set probability). Similarly, each person has a set
duration of infection.

Sociability and duration of infection are given as normal distributions with 
adjustible mean and deviation.

Interactions are randomized each day so, unlike in real life,
there are no natural clusters of people (such as towns).

After a person is cured, they can no longer be infected.
