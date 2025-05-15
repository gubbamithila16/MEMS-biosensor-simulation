# Author: Mithila Gubba
# Project: Simulation of MEMS-Based Biosensor for Dengue Detection

import numpy as np
import matplotlib.pyplot as plt
import random

length = 200e-6  # 200 micrometers
width = 30e-6
thickness = 1e-6
youngs_modulus = 160e9  # For silicon, in Pascals

def calculate_deflection(force_n):
    moment_of_inertia = (width * thickness ** 3) / 12
    deflection = (force_n * length ** 3) / (3 * youngs_modulus * moment_of_inertia)
    return deflection * 1e9  # convert to nanometers

def generate_sample_data(num_samples=50):
    data = []
    for _ in range(num_samples):
        if random.random() < 0.3:  # 30% chance virus is present
            force = random.uniform(0.8, 1.5) * 1e-9  # 0.8–1.5 nN
        else:
            force = random.uniform(0.1, 0.4) * 1e-9  # noise/false
        data.append(force)
    return np.array(data)

forces = generate_sample_data()
deflections = np.array([calculate_deflection(f) for f in forces])

plt.figure(figsize=(10, 5))
plt.plot(deflections, label='Deflection (nm)', color='blue')
plt.axhline(y=5, color='red', linestyle='--', label='Detection Threshold')
plt.title('Simulated MEMS Biosensor Deflection (Dengue Detection)')
plt.xlabel('Sample Index')
plt.ylabel('Cantilever Deflection (nm)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
