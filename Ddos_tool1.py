import tkinter as tk
from tkinter import scrolledtext
import threading
import time

class DDOSSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("DDoS Simulation Tool")

        # Target Frame
        self.target_frame = tk.Frame(root)
        self.target_frame.pack(pady=10)

        tk.Label(self.target_frame, text="Target IP:").grid(row=0, column=0, padx=5)
        self.target_ip = tk.Entry(self.target_frame)
        self.target_ip.grid(row=0, column=1, padx=5)

        tk.Label(self.target_frame, text="Port:").grid(row=1, column=0, padx=5)
        self.target_port = tk.Entry(self.target_frame)
        self.target_port.grid(row=1, column=1, padx=5)

        # Control Frame
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)

        self.start_button = tk.Button(self.control_frame, text="Start Simulation", command=self.start_simulation)
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(self.control_frame, text="Stop Simulation", command=self.stop_simulation)
        self.stop_button.grid(row=0, column=1, padx=10)

        # Log Frame
        self.log_frame = tk.Frame(root)
        self.log_frame.pack(pady=10)

        self.log_text = scrolledtext.ScrolledText(self.log_frame, width=50, height=15)
        self.log_text.pack()

        self.simulating = False

    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def start_simulation(self):
        target_ip = self.target_ip.get()
        target_port = self.target_port.get()

        if not target_ip or not target_port:
            self.log("Please enter target IP and port.")
            return

        try:
            target_port = int(target_port)
        except ValueError:
            self.log("Port must be a number.")
            return

        self.simulating = True
        self.log("Starting DDoS simulation on {}:{}".format(target_ip, target_port))

        # Start a separate thread for simulation
        threading.Thread(target=self.simulation_thread, args=(target_ip, target_port)).start()

    def stop_simulation(self):
        self.simulating = False
        self.log("Stopped DDoS simulation.")

    def simulation_thread(self, target_ip, target_port):
        while self.simulating:
            self.log("Simulating attack on {}:{}".format(target_ip, target_port))
            time.sleep(1)  # Simulate time delay between attacks

if __name__ == "__main__":
    root = tk.Tk()
    app = DDOSSimulator(root)
    root.mainloop()