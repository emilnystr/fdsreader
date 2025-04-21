import fdsreader
import matplotlib.pyplot as plt


plt.rcParams['figure.figsize'] = (10, 20)    

path_to_data = 'C:/fdsreader test'
sim = fdsreader.Simulation(path_to_data)
devc = sim.devices


fig, axs = plt.subplots(5, 1, figsize=(10, 20))

 
axs[0].plot(sim.hrr['Time'], sim.hrr['HRR'], label='HRR från branden')
axs[0].set_xlabel('Tid (s)')
axs[0].set_ylabel('Effekt (kW)')
axs[0].legend()
axs[0].grid(True)

 
for i in devc:
    if not i.id.startswith('Koldioxid'):
        continue
    axs[1].plot(devc["Time"].data, i.data*100, label="Koldioxidkoncentration")
axs[1].axhline(y=5, color='red', linestyle='--', label='Gränsvärde')
axs[1].set_xlabel('Tid (s)')
axs[1].set_ylabel('CO₂ (%)')
axs[1].legend()
axs[1].grid(True)

 
for i in devc:
    if not i.id.startswith('kolmonoxid'):
        continue
    axs[2].plot(devc["Time"].data, i.data*100, label="Kolmonoxidkoncentration")
axs[2].axhline(y=2, color='red', linestyle='--', label='Gränsvärde')
axs[2].set_xlabel('Tid (s)')
axs[2].set_ylabel('CO (%)')
axs[2].legend()
axs[2].grid(True)

 
for i in devc:
    if not i.id.startswith('syrg'):
        continue
    axs[3].plot(devc["Time"].data, i.data*100, label="Syrgaskoncentration")
axs[3].axhline(y=15, color='red', linestyle='--', label='Gränsvärde')
axs[3].set_xlabel('Tid (s)')
axs[3].set_ylabel('O₂ (%)')
axs[3].legend()
axs[3].grid(True)

 
for i in devc:
    if not i.id.startswith('S'):
        continue
    axs[4].plot(devc["Time"].data, i.data, label='Rökdetektor')
axs[4].set_xlabel('Tid (s)')
axs[4].set_ylabel('Värde')
axs[4].legend()
axs[4].grid(True)

plt.tight_layout()  
plt.show()

slc = sim.slices.filter_by_quantity('TEMPERATURE').get_nearest(x=3, y=0)


slc_data = slc[0].data
print(slc_data)

it = sim.slices[0].get_nearest_timestep(300)
fig_count=0
for slc in sim.slices:
    plt.imshow(slc[0].data[it].T,
               origin='lower', 
               extent=slc.extent.as_list())
    q = slc.quantity.quantity
    u = slc.quantity.unit
    plt.xlabel(f'{slc.extent_dirs[0]} / m')
    plt.ylabel(f'{slc.extent_dirs[1]} / m')
    plt.colorbar(label=f"{q} / {u}")
    plt.show()

