# Simple temperature environment that follows gym interface.
#  Custom temperature env to simulate temperature changes.
#  Parameters:
#        * heat_mass_capacity:           capacity of the building's heat mass [J/K]
#        * heat_transmission:            heat transmission to the outside [W/K]
#        * maximum_cooling_power:        [W] (<= 0)
#        * maximum_heating_power:        [W] (>= 0)
#        * initial_building_temperature: building temperature at start time [℃]
#        * time_step_size:               [s]
#        * conditioned_floor_area:       [m**2]


import gym
from gym import spaces


class CustomEnv(gym.Env):

  metadata = {'render.modes': ['human']}

  def __init__(self, target_temp):
    super(CustomEnv, self).__init__()

    # Building settings
    self.heat_mass_capacity = 165000 * conditioned_floor_area,
    self.heat_transmission = 200,
    self.maximum_cooling_power = -10000,
    self.maximum_heating_power = 10000,
    self.time_step_size = timedelta(minutes=5),
    self.conditioned_floor_area = conditioned_floor_area

    # Starting and target temperature.
    self.current_temperature = 16
    self.target_temperature = target_temp

    # Action space with 1 variable that can vary between 0 and 1000 and stands for how much power we want to send to heating system.
    self.action_space = spaces.Box(low=self.0, high=1000, shape=(1,), dtype=np.float32)

    # Observatin space 1 variable between 0 and 70 that represents the temperature in the room.
    self.observation_space = spaces.Box(low=0, high=70, shape=(1,), dtype=np.float32)

  step_counter = 0
  def step(self, action):

    dt_by_cm = self.__time_step_size.total_seconds() / self.__heat_mass_capacity
    current_temperature = (self.current_temperature * (1 - dt_by_cm * self.__heat_transmission) + dt_by_cm * (heating_cooling_power + self.__heat_transmission * outside_temperature))

    self.state = np.array([current_temperature])

    return self.state, reward, done
  
  def reset(self):
    self.current_temperature = 16



  # NOT USED
  def render(self, mode='human', close=False):
    pass
