import gym
import custom_model
import numpy as np
import os
import matplotlib.pyplot as plt

from stable_baselines.common.vec_env import DummyVecEnv

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines import PPO2

PATH = "/home/andrehoejmark/projects/Tempearture-control/Logs/ppo2/"

files = os.listdir(PATH)
files = [s for s in os.listdir(PATH) if s.endswith('.pkl')]

env = DummyVecEnv([lambda: custom_model.Building(22)])
for i in range(len(files)):

    file = PATH + files[i]
    model = PPO2.load(file[:-4], env=env)

    temperatures = []
    actions = []
    steps = []

    step = 0
    obs = env.reset()
    while True:
        step += 1
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)

        temperatures.append(obs[0][0])
        actions.append(action[0][0]*3000)
        steps.append(step)
        
        if(step == 15000):
            plt.plot(steps, temperatures)
            plt.xlabel('steps')
            plt.ylabel('temp')
            
            #print(files)
            print(PATH + "/plots/" +  files[i][:-4] + '.png')
            plt.savefig(PATH + "/plots/" +  files[i][:-4] + '.png')
            plt.clf()
            #print(file[:-4] + '.png')
            
            break
    
