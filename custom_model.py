##########################################################################################################################################################################
########################### Simple temperature environment that follows the gym interface. ###############################################################################
##########################################################################################################################################################################
#
#  Parameters:
#        * heat_mass_capacity:           capacity of the building's heat mass [J/K]
#        * heat_transmission:            heat transmission to the outside [W/K]
#        * maximum_cooling_power:        [W] (<= 0)
#        * maximum_heating_power:        [W] (>= 0)
#        * initial_building_temperature: building temperature at start time [℃]
#        * time_step_size:               [s]
#        * conditioned_floor_area:       [m**2]
#
# inspired from https://github.com/timtroendle/simple-simple/blob/develop/simplesimple/building.py & https://github.com/openai/gym/blob/master/gym/envs/classic_control/continuous_mountain_car.py
#
##########################################################################################################################################################################
##########################################################################################################################################################################


import gym
from gym import spaces
import numpy as np
from datetime import timedelta
import random
class Building(gym.Env):

  metadata = {'render.modes': ['human']}

  def __init__(self, target_temp):
    super(Building, self).__init__()

    self.step_counter = 0
    self.reset_counter = 0
    self.outside_counter = 0 
    # Building settings1
    self.conditioned_floor_area = 100
    self.heat_mass_capacity = 165000 * self.conditioned_floor_area
    self.heat_transmission = 200
    self.time_step_size = timedelta(minutes=10) # How many minutes into future each step.

    # Outside Settings
    self.outside_temperature = 6
    self.outside_array = [16,16,15,15,15,16,17,18,18,19,20,22,23,23,24,22,18,15,15,14,14,14,14,14]
    #[6,6,5,5,5,6,7,8,8,9,10,12,14,16,16,16,15,15,15,14,12,8,8,7]
    
    # Starting and target temperature.
    self.current_temperature = 16
    self.target_temperature = target_temp
    self.target_array = [16, 19, 21,25,37]

    # Action space with 1 variable that can vary between 0 and 1000 and stands for how much power we want to send to heating system.
    self.action_space = spaces.Box(low=0, high=1000, shape=(1,), dtype=np.float32)
    high = np.array([70,70,40])
    # Observatin space 1 variable between 0 and 70 that represents the temperature in the room.
    self.observation_space = spaces.Box(low=-high, high=high, dtype=np.float32)

  def rescale_power(self, power):
    p = power * 5000
    return p
  
  def step(self, action):
    
    
    self.step_counter += 1
    self.outside_counter +=1
    power = min(max(self.rescale_power(action[0]), 0), 10000)
    self.current_temperature = self.state[0]
    
    #Looping through the daily tempratures each hour
    if self.step_counter%6 == 0:
      if self.outside_counter >=23:
        self.outside_counter=0
      self.outside_temperature =  self.outside_array[self.outside_counter]
      self.outside_counter += 1
    
    dt_by_cm = self.time_step_size.total_seconds() / self.heat_mass_capacity

    self.next_temperature = (self.current_temperature * (1 - dt_by_cm * self.heat_transmission) + dt_by_cm * (power + self.heat_transmission * self.outside_temperature))

  
    done = bool(self.step_counter > 10000) #BYT TILL 1000 om det inte funkar igen.....
    self.state = np.array([self.next_temperature, self.target_temperature,self.outside_temperature ])
    
    # ( )² sicne it would make the network prefer small changes. If it does a big step and it's wrong it gets super big pentalty. 
    reward = -(self.next_temperature - self.target_temperature)**2
   
    
    
    
    
    return self.state, reward, done, {}
  
  def reset(self):
    self.step_counter = 0
    self.state = np.array([np.random.uniform(low=15.6, high=16.4)]) #self.current_temperature = 16
    #self.state = np.array([16])
    self.reset_counter += 1
    if self.reset_counter == 6:
      self.reset_counter = 0
    return self.state

  
  # NOT USED
  def render(self, mode='human', close=False):
    pass
