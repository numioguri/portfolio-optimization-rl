import gym
from gym import spaces
import numpy as np

class PortfolioEnv(gym.Env):
    def __init__(self, prices):
        self.prices = prices
        self.n_assets = prices.shape[1]
        self.action_space = spaces.Box(0, 1, shape=(self.n_assets,), dtype=np.float32)
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(self.n_assets,), dtype=np.float32)
        self.current_step = 0

    def reset(self):
        self.current_step = 0
        return self.prices[self.current_step]

    def step(self, action):
        self.current_step += 1
        done = self.current_step >= len(self.prices) - 1
        reward = np.dot(action, self.prices[self.current_step])  # portfolio return
        return self.prices[self.current_step], reward, done, {}
