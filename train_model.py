import gym
import custom_model
import numpy as np

from stable_baselines.common.vec_env import DummyVecEnv

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines import PPO2

LR = [0.00001]
TS = [150000]

j = 0
for i in range(len(LR)):
    for j in range(len(TS)):
        env = DummyVecEnv([lambda: custom_model.Building(22)])
        model = PPO2(MlpPolicy, env, verbose=1, learning_rate = LR[i])
        model.learn(total_timesteps=TS[j])
        model.save("/home/andrehoejmark/projects/Tempearture-control/Logs/ppo2/" + "LR" + str(i) + "_TS" + str(j))
    

    
