import fdsreader
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (6, 4)

import numpy as np


path_to_data = 'C:/fdstest'

sim = fdsreader.Simulation(path_to_data)

devc = sim.devices



plt.plot(sim.hrr['Time'], sim.hrr['HRR'], label='HRR från branden')



plt.xlabel('time / s')
plt.ylabel('heat flow rate / kW')
plt.legend()
plt.grid()


plt.show()

for i in devc:
    if not i.id.startswith('t'): 
        continue
    
    plt.plot(devc["Time"].data, i.data, label=i.id)

plt.legend()
plt.xlabel("time / s")
plt.ylabel('temperature / $^\circ$C')
plt.grid()
plt.show()

for i in devc:
    if not i.id.startswith('S'): 
        continue
    
    plt.plot(devc["Time"].data, i.data, label=i.id)

plt.legend()
plt.xlabel("time / s")
plt.ylabel('procent / $^\circ$C')
plt.grid()
plt.show()

for i in devc:
    if not i.id.startswith('k'): 
        continue
    
    plt.plot(devc["Time"].data, i.data, label=i.id)

plt.axhline(y=0.015, color='red', linestyle='--', label='gräns')
plt.legend()
plt.xlabel("time / s")
plt.ylabel('ppm / $^\circ$C')
plt.grid()
plt.show()

for i in devc:
    if not i.id.startswith('s'):
        continue
    
    plt.plot(devc["Time"].data, i.data, label=i.id)


plt.axhline(y=0.15, color='red', linestyle='--', label='gräns')


plt.legend()
plt.xlabel("time / s")
plt.ylabel('ppm / $^\circ$C')
plt.grid()


plt.show()
