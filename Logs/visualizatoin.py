import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temperatures = pd.read_csv('temperatures.csv')
actions = pd.read_csv('actions.csv')
steps = pd.read_csv('steps.csv')


print(len(actions))
print(len(steps))

fig = plt.figure()
plt.subplot(1, 2, 1)
plt.plot(steps, temperatures)
plt.plot(steps, [22]*len(steps))

plt.subplot(1, 2, 2)
plt.plot(steps, actions)



plt.show()
