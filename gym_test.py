import gym
from gym import spaces
from gym import envs
print(envs.registry.all())
"""
env = gym.make('StarGunnerNoFrameskip-v4') 
print(env.action_space)
print(env.observation_space)
for i_episode in range(30):
    observation = env.reset()
    for t in range(100):
        env.render()
        #print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
"""
"""
env = gym.make('StarGunnerNoFrameskip-v4')
env.reset()
print(env.action_space)

for _ in range(5000):
    env.render()
    env.step(env.action_space.sample()) # take a random action


"""
"""
space = spaces.Discrete(8) # Set with 8 elements {0, 1, 2, ..., 7}
x = space.sample()
assert space.contains(x)
assert space.n == 8
"""
