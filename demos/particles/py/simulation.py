import numpy as np

n_particles = 200
positions = np.random.rand(n_particles, 3) - 0.5
velocity = np.zeros_like(positions)
g = 0.0

def initialize():
    global positions, velocity
    positions[:] = np.random.rand(n_particles, 3) - 0.5
    velocity[:] = 0

def step(dt=0.016):
    global positions, velocity
    velocity[:,1] -= g * dt
    positions[:] += velocity * dt

def set_gravity(value):
    global g
    g = value

def get_positions():
    return positions