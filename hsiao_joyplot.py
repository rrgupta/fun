#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import sncosmo
plt.style.use('dark_background') # whoaaaa!
"""
Create a joyplot of the Hsiao supernova template
"""
source = sncosmo.get_source('hsiao', version='3.0')
model = sncosmo.Model(source=source)
phases = np.arange(-15, 25, 0.5) # 0.5 day time resolution
wave = np.linspace(1000, 11000, 1000) # wavelength array (Angstroms)
flux = model.flux(phases, wave) # 2D array of SN fluxes
n_wave_ext_pts = 25 # extend wavelength axis to make plot more symmetric
wave_ext = np.append(np.linspace(-1400, 1000, n_wave_ext_pts), wave)
# add Gaussian random noise to simulate flux for the new wavelengths
flux_ext = np.append(np.random.normal(0., 2e-11, (len(phases), n_wave_ext_pts)),
                     flux, axis=1)
# shuffle the phases for dramatic effect
np.random.seed(3); np.random.shuffle(flux_ext)
xshift = np.random.normal(0., 300, len(phases)) # shift in wavelength for effect

fig = plt.figure(figsize=(4.5, 6))
ax = fig.add_subplot(111)
for i in range(len(phases)):
    ax.plot(wave_ext + xshift[i], flux_ext[i]*1e9 - i, c='w', zorder=i)
    ax.fill(wave_ext + xshift[i], flux_ext[i]*1e9 - i, 'k', zorder=i)
plt.title('PHYSICS DIVISION', y=0.95, size=31)
plt.xlabel('HSIAO TEMPLATE', size=28.5, fontweight='bold', labelpad=-10)
ax.set_xlim(-400, 10000)
ax.set_frame_on(False)
plt.tick_params(bottom='off', left='off', labelleft='off', labelbottom='off') 
fig.tight_layout()
fig.savefig('Hsiao_joyplot.png', dpi=500)
fig.savefig('Hsiao_joyplot.pdf')
