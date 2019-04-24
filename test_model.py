import gym
import custom_model
import numpy as np
import os
import matplotlib.pyplot as plt

from stable_baselines.common.vec_env import DummyVecEnv

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines import PPO2

PATH = "/home/rickardgyll/Documents/Temp_control/Tempearture-control-master/Logs/ppo2/"
#PATH = "/home/rickardgyll/Documents/Temp_control/Tempearture-control-master/ANDRETEST/"

files = os.listdir(PATH)
files = [s for s in os.listdir(PATH) if s.endswith('.pkl')]

env = DummyVecEnv([lambda: custom_model.Building(27)])

for i in range(len(files)):

    file = PATH + files[i]
    model = PPO2.load(file[:-4], env=env)

    temperatures = []
    actions = []
    steps = []
    rewardss = []
    step = 0
    obs = env.reset()
    while True:
        step += 1
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        
        rewardss.append(rewards)
        temperatures.append(obs[0][0])
        actions.append(action[0][0]*5000)
        steps.append(step)
        
        if(step == 7000):
            plt.plot(steps, temperatures)
            plt.xlabel('steps')
            plt.ylabel('temp')
            
            #print(files)
            print(PATH + "/plots/" +  files[i][:-4] + '.png')
            plt.savefig(PATH + "/plots/" +  files[i][:-4] + '.png')
            plt.clf()
            #print(file[:-4] + '.png')
            
            break
    
