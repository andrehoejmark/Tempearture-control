##########################################################################################################################################################################
############################################# Simple temperature environment that follows the gym interface. #############################################################
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

class Building(gym.Env):

  metadata = {'render.modes': ['human']}

  def __init__(self, target_temp):
    super(Building, self).__init__()

    self.step_counter = 0
    
    # Building settings
    self.conditioned_floor_area = 100
    self.heat_mass_capacity = 165000 * self.conditioned_floor_area
    self.heat_transmission = 200
    self.outside_temperature = 19
    self.time_step_size = timedelta(minutes=5) # How many minutes into future each step.

    # Starting and target temperature.
    self.current_temperature = 16
    self.target_temperature = target_temp

    # Action space with 1 variable that can vary between 0 and 1000 and stands for how much power we want to send to heating system.
    self.action_space = spaces.Box(low=0, high=1000, shape=(1,), dtype=np.float32)

    # Observatin space 1 variable between 0 and 70 that represents the temperature in the room.
    self.observation_space = spaces.Box(low=0, high=70, shape=(1,), dtype=np.float32)
  
  def step(self, action):
    self.step_counter += 1
    print(action)
    power = min(max(action[0], 0), 1000)
    current_temperature = self.state[0]
    
    dt_by_cm = self.time_step_size.total_seconds() / self.heat_mass_capacity
    next_temperature = (self.current_temperature * (1 - dt_by_cm * self.heat_transmission) + dt_by_cm * (power + self.heat_transmission * self.outside_temperature))

    # Potentially change since it may go over the temperature, but it should stay at target temp :)
    # Better to maybe test x steps lets say 150steps. And reward maximized when on target temp.
    done = bool((next_temperature > (self.target_temperature-1)) and (next_temperature < (self.target_temperature+1)))  
    self.state = np.array([current_temperature])

    # ( )² sicne it would make the network prefer small changes. If it does a big step and it's wrong it gets super big pentalty. 
    reward = -(next_temperature - self.target_temperature)**2
    
    return self.state, reward, done, {}
  
  def reset(self):
    self.step_counter = 0
    self.state = np.array([np.random.uniform(low=15.6, high=16.4)]) #self.current_temperature = 16
    self.action = np.array([np.random.uniform(low=0, high=50)])

    return self.state

  
  # NOT USED
  def render(self, mode='human', close=False):
    pass
