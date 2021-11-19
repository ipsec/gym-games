import gym
import numpy as np

from gym import spaces


class TestObject:
    def __init__(self):
        self.name = 'test'


class FooEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.count = 0
        self.test_obj = None
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(1,), dtype=np.float32)
        self.action_space = spaces.Box(low=5, high=20, shape=(1,), dtype=np.float32)

    def step(self, action):
        self.count += 1
        done = False
        if self.count >= 10:
            done = True
        reward = 1

        return np.array([0.], dtype=np.float32), reward, done, {}

    def reset(self):
        self.count = 0
        self.test_obj = TestObject()
        return np.array([0.], dtype=np.float32)

    def render(self, mode="human"):
        print(self.count)
