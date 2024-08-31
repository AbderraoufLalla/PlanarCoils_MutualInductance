# Multi-Layer Coil Inductance Calculator (Developed from Biot-Savart Law)

This Python script calculates and visualizes the inductance of a multi-layer coil using the Biot-Savart law to compute both self and mutual inductance. It allows you to determine how the inductance changes with the number of layers based on coil dimensions and spacing.

## Features

- **Self-Inductance Calculation**: Computes the self-inductance of a single-layer coil.
- **Total Inductance Calculation**: Determines the total inductance for multiple layers, accounting for mutual inductance between layers.
- **Visualization**: Plots how inductance varies with the number of layers.

## Parameters

- **Outer Diameter**: Diameter of the coil (in meters).
- **Width**: Width of the coil wire (in meters).
- **Spacing**: Spacing between turns (in meters).
- **Number of Turns**: Total number of turns in the coil.
- **Number of Coils**: Number of coil layers.
- **Layer Spacing**: Distance between coil planes (in meters).

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AbderraoufLalla/PlanarCoils_MutualInductance.git

## Output

   - **Self Inductance**: Displays the self-inductance value in microhenries (uH).
   - **Total Inductance**: Shows the total inductance for varying numbers of layers.


## Acknowledgments

Utilizes Biot-Savart law for inductance calculations.
Incorporates SciPy for constants and mathematical operations, and Matplotlib for plotting.

## Licence

This project is licensed under the MIT License. See the LICENSE file for details.

