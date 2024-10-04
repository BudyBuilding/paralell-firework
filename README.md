# paralell-firework

This Python script creates a graphical user interface (GUI) using the tkinter library to simulate fireworks. The GUI consists of three separate canvases, each demonstrating a different method of rendering fireworks: sequential processing, SIMD (Single Instruction, Multiple Data), and multithreading.

Features:
Three Firework Methods:
Sequential: Particles are drawn one after another in a single thread.
SIMD: Particles are drawn using vectorized operations with NumPy for parallel processing.
Multithreading: Particles are drawn concurrently using multiple threads.
Realistic Firework Simulation:
Each firework consists of multiple particles that move outward from the click point.
Particles have randomized angles and speeds to create a natural spread.
Colors of the particles are randomly chosen from a predefined set.
Particles gradually fade out to simulate a realistic firework effect.
Performance Metrics:
The script measures and prints the time taken for each firework method to complete.
Average times for each method are calculated and displayed periodically.
Usage:
Run the script to open the GUI window.
Click on any of the three canvases to trigger a firework display using the respective method.
Observe the console for performance metrics, including the time taken for each firework and the average times.
Example:
Python

# Run the script
python firework.py

# Click on the canvases to see the fireworks and check the console for performance metrics.
