import numpy as np
from scipy.constants import mu_0, pi
import math
import time
import matplotlib.pyplot as plt

# Coil parameters
outer_diameter = 5.5 / 1000  # 6 mm in meters
width = 0.102 / 1000  # 0.102 mm in meters
spacing = 0.102/ 1000  # 0.102 mm in meters
rotation = 1
num_turns = 9
num_coils = 8
layer_spacing = 0.102 / 1000  # distance between coil planes

def sum_matrix(matrix):
    total_sum = 0
    for row in matrix:
        for element in row:
            total_sum += element
    return total_sum

# Function to calculate self-inductance
def calculate_self_inductance(outer_diameter, width, spacing, num_turns):
    d_inner = outer_diameter - 2 * (width + spacing) * num_turns
    d_avg = 0.5 * (outer_diameter + d_inner)
    fill_ratio = (outer_diameter - d_inner) / (outer_diameter + d_inner)

    # Constants for the inductance formula
    c = [1, 2.46, 0, 0.2]
    p = fill_ratio
    L = 0.5 * mu_0 * num_turns**2 * d_avg * c[0] * (
        math.log(c[1] / p) + c[2] * p + c[3] * p**2
    )
    return L

L = calculate_self_inductance(outer_diameter, width, spacing, num_turns)


def total_inductance(L, num_turns, num_coils, layer_spacing):
    layer_spacing_mm = layer_spacing * 1000
    mutual_inductance_matrix = np.zeros((num_coils, num_coils))
    T_scaling = 1.5625 * num_turns ** 2 / (1.67 * num_turns ** 2 - 5.84 * num_turns + 65)
    for i in range(1,num_coils+1,1):
        for j in range(1, num_coils+1, 1):
            if i != j:
                distance = layer_spacing_mm * abs(j - i)
                M = 1 / (0.184 * ((distance) ** 3) - (0.525 * distance ** 2) + (1.038 * distance) + 1.001)
                mutual_inductance_matrix[i-1,j-1] = M
    L_mutual_sum = sum_matrix(mutual_inductance_matrix)
    scale_factor = L_mutual_sum * T_scaling + num_coils
    L_total = scale_factor * L
    return float(L_total)

L_total = []
x= []
for i in range(1, num_coils+1, 1):
    all = total_inductance(L, num_turns, i, layer_spacing) * 1e6
    round(all, 9)
    L_total.append(all)
    x.append(i)

print(f'Self inductance per layer: {L*1e6: .4} uH')
print(f'Total inductance with layers (uH): {L_total} uH')

plt.plot(x, L_total, marker='o', linestyle='-', color='b', label='Inductance')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xlabel('Number of layers')
plt.ylabel('Inductance (uH)')
plt.title('Inductance vs Number of Layers')
plt.legend()

# Annotate each point with its value
for i, txt in enumerate(L_total):
    plt.annotate(f'{txt:.3f}', (x[i], L_total[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()