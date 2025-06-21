import gymnasium as gym
from stable_baselines3 import PPO

# Create the CartPole-v1 environment with human rendering
env = gym.make("CartPole-v1", render_mode="human")


# Initialize the PPO agent with a multilayer perceptron policy
model = PPO("MlpPolicy", env, verbose=1)

# Train the agent for 50,000 timesteps
model.learn(total_timesteps=50000)



# Evaluate the trained agent
obs, info = env.reset()


# Let the agent interact with the environment for 1000 steps
for _ in range(1000):
    
    # Predict the next action using the trained model
    action, _ = model.predict(obs)
    
    # Take the action and receive the result
    obs, reward, terminated, truncated, info = env.step(action)
    
    # Check if the episode is done
    done = terminated or truncated
    
    env.render()
    if done:
        obs, info = env.reset()

# Close the environment
env.close()

