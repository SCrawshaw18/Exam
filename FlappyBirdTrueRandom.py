import gym
import gym_ple
from random import randint
env = gym.make('FlappyBird-v0')

NUM_EPISODES = 10

for episode in range(NUM_EPISODES):
	observation = env.reset()
	done=False
	while not done:
		env.render()
		action = randint(0,1)
		observation, reward, done, info = env.step(action)