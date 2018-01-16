#Based on the cartpole tutorial at https://gym.openai.com/docs/
import gym
import gym_ple
from random import randint
env = gym.make('FlappyBird-v0')

NUM_EPISODES = 2

for episode in range(NUM_EPISODES):
	observation = env.reset()
	done=False
	while not done:
		env.render()
		if randint(0,10) > 8:
			action=0
		else:
			action=1
		observation, reward, done, info = env.step(action)