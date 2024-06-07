# DDoS Simulation Tool

A simple DDoS simulation tool built with Python and Tkinter to simulate and log DDoS attacks on a specified target IP and port.

## Features

- Input fields for target IP address and port.
- Buttons to start and stop the DDoS simulation.
- A log window to display the status of the simulation.

## Prerequisites

- Python 3.x
- Tkinter library (usually included with Python installations)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/ddos-simulation-tool.git
   cd ddos-simulation-tool
   ```

2. Run the script:

   ```sh
   python ddos_simulator.py
   ```

## Usage

1. Launch the tool by running the script:

   ```sh
   python ddos_simulator.py
   ```

2. Enter the target IP address and port in the respective fields.
3. Click the "Start Simulation" button to begin the simulation.
4. Click the "Stop Simulation" button to stop the simulation.

## Code Overview

### Main Components

- **Target Frame:** Contains input fields for the target IP and port.
- **Control Frame:** Contains buttons to start and stop the simulation.
- **Log Frame:** Contains a scrolled text widget to display log messages.

### Methods

- `start_simulation()`: Validates the input and starts the DDoS simulation in a separate thread.
- `stop_simulation()`: Stops the DDoS simulation.
- `simulation_thread(target_ip, target_port)`: Runs the simulation loop, logging messages at regular intervals.

### Logging

The `log()` method is used to append messages to the log window, ensuring the most recent messages are visible.

## Disclaimer

This tool is intended for educational purposes only. Do not use this tool for malicious activities. Unauthorized use of this tool may be illegal and unethical.
