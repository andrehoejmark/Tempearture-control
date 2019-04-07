import gym
import custom_model

from stable_baselines.common.vec_env import DummyVecEnv

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines import PPO2


# multiprocess environment
n_cpu = 4
#env = SubprocVecEnv([lambda: gym.make('CartPole-v1') for i in range(n_cpu)])
env = DummyVecEnv([lambda: custom_model.Building(22)])

model = PPO2(MlpPolicy, env, verbose=1, learning_rate = 0.002)
model.learn(total_timesteps=25000)
#model.save("ppo2_cartpole")

#del model # remove to demonstrate saving and loading

#model = PPO2.load("ppo2_cartpole")

# Enjoy trained agent
obs = env.reset()
count = 10
while True:
    count += 10
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    #env.render()
    print('action: ' + str(action[0][0]*500))
    print('states: ' + str(obs))
    print('reward: ' + str(rewards))
    print('count: ' + str(count/60))
    print(' ')

'''
import gym
import custom_model
import time

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines import A2C

from stable_baselines.common.vec_env import DummyVecEnv


# multiprocess environment
n_cpu = 4
#env = SubprocVecEnv([lambda: gym.make('CartPole-v1') for i in range(n_cpu)])
env = DummyVecEnv([lambda: custom_model.Building(22)])


model = A2C(MlpPolicy, env, verbose=1, learning_rate=0.002)
model.learn(total_timesteps=180000) #25000 # 2500000
model.save("a2c_cartpole")

#del model # remove to demonstrate saving and loading

#model = A2C.load("a2c_cartpole")

obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    #env.render()

    print('action: ' + str(action))
    print('states: ' + str(obs))
    print('reward: ' + str(rewards))
    print(' ')

    time.sleep(0.01)

'''








'''
import gym
import numpy as np
import custom_model
from stable_baselines.common.vec_env import DummyVecEnv

from stable_baselines.ddpg.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.ddpg.noise import NormalActionNoise, OrnsteinUhlenbeckActionNoise, AdaptiveParamNoiseSpec
from stable_baselines import DDPG

#env = gym.make('MountainCarContinuous-v0')
#env = DummyVecEnv([lambda: env])
env = DummyVecEnv([lambda: custom_model.Building(22)])


# the noise objects for DDPG
n_actions = env.action_space.shape[-1]
param_noise = None
action_noise = OrnsteinUhlenbeckActionNoise(mean=np.zeros(n_actions), sigma=float(0.5) * np.ones(n_actions))

model = DDPG(MlpPolicy, env, verbose=1, param_noise=param_noise, action_noise=action_noise)
model.learn(total_timesteps=20)
model.save("ddpg_mountain")

del model # remove to demonstrate saving and loading

model = DDPG.load("ddpg_mountain")

obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
'''
