import numpy as np


class Cloth:
    nx = 30
    ny = 30
    dx = 0.1
    dy = 0.1

    positions = None

    def init():
        positions = 0
        return
    
    def step(dt=0.01):
        return
    
    def get_positions():
        return
    
    def get_connections():
        return



n_particles = 1000
#positions = np.random.rand(n_particles, 3) - 0.5
positions = np.zeros([n_particles, 3])
velocity = np.zeros_like(positions)
g = 0.0

def initialize():
    global positions, velocity
#    positions[:] = np.random.rand(n_particles, 3) - 0.5
    positions[:] = 0.5 * np.random.normal(size=[n_particles, 3])
    velocity[:] = 0

def step(dt=0.016):
    global positions, velocity
#    velocity[:,2] -= g * dt
    velocity[:] += g * np.random.normal(size=[n_particles, 3])
    positions[:] += velocity * dt

def set_gravity(value):
    global g
    g = value

def get_positions():
    return positions