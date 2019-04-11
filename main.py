import gym
import custom_model
import numpy as np

from stable_baselines.common.vec_env import DummyVecEnv

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines import PPO2


env = DummyVecEnv([lambda: custom_model.Building(22)])
model = PPO2(MlpPolicy, env, verbose=1, learning_rate = 0.0007)
model.learn(total_timesteps=25000)

#model.save("ppo2_cartpole")
#del model # remove to demonstrate saving and loading
#model = PPO2.load("ppo2_cartpole")


DIR = "\Logs" 
Graph_id = '1'
path = DIR + Graph_id


obs = env.reset()

temperatures = []
actions = []
steps = []

step = 0
while True:
    step += 1
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    #env.render()
    #print('action: ' + str(action[0][0]*500))
    #print('states: ' + str(obs))
    #print('reward: ' + str(rewards))
    #print('count: ' + str(step))
    #print(' ')

    temperatures.append(obs[0][0])
    actions.append(action[0][0]*5000)
    steps.append(step) 
    
    if(step == 3000):
        print('Done')
        break


np.savetxt("temperatures.csv", np.array(temperatures), delimiter=",")
np.savetxt("actions.csv", np.array(actions), delimiter=",")
np.savetxt("steps.csv", np.array(steps), delimiter=",")

