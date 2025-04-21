import pandas as pd
from stable_baselines3 import A2C
from env import PortfolioEnv

# Load the data
data = pd.read_csv("stocks.csv", index_col=0)

# Prepare environment
env = PortfolioEnv(data.values)

# Create and train the model
model = A2C("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

# Save the trained model
model.save("a2c_portfolio_model")

print("✅ Training complete and model saved!")
