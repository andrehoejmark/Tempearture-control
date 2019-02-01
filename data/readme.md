Information about the dataset
data from 07.01.2018 to 10.12.2018, 4-5min per point.
two radiator circuits that send heated water to the room.                     (dataset supplies not sure which one goes to this room)
two ventilations valves that the air flow though.                             (dataset supplier thinks both of the valves go to this room)
if (pressure air-ch.1 = 0) { No air flow }
there are some gaps in the data which is probably because communication was down or because the values don't update contionously, only when the value changes.
heat control signal COL: D is the control signal for heating the radiator.
cooling control signal COL: E is a measurement of how much cooled air is being sent from a vent that with cooling paste. The temp is around 14-16 degrees c.

Temperature(inside, outside) range from -20 to 40 (deg C)
Temperature(water, radiator) range from 0 to 100 (deg C)
Control signals(heat control signal, cooling control signal) range from 0 to 100%
Pressures(pressure air-ch) range from 0 to 1000(Pa)
