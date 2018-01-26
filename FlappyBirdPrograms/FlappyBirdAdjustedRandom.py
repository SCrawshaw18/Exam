#Based on the cartpole tutorial at https://gym.openai.com/docs/
import gym
import gym_ple
from random import randint
env = gym.make('FlappyBird-v0')

NUM_EPISODES = 100
def writeToFile(score):
		file=open("scoreSheetAdjRand.txt","a")
		file.write(str(score) + "\n")
		file.close()
for episode in range(NUM_EPISODES):
	observation = env.reset()
	done=False
	score=0
	while not done:
		env.render()
		if randint(0,10) > 8:
			action=0
		else:
			action=1
		observation, reward, done, info = env.step(action)
		score=score+reward
		if done:
			writeToFile(score+5)