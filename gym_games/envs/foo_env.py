import gym
from numpy import np


class FooEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.count = 0

    def step(self, action):
        self.count += 1
        done = False if self.count <= 10 else done = True
        reward = 1

        return np.array([[0]], dtype=np.float32), reward, done, {}

    def reset(self):
        self.count = 0
        np.array([[0]], dtype=np.float32)

    def render(self, mode="human"):
        ...
