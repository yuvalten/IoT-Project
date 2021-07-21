from meter_sim import MeterSim
import mqtt_client_listener
import threading

class program:
# Create instance of meter_sim
    def __init__(self):
        self.meter_sim = MeterSim()

    def main(self):
# Create meter_sim thread
        runs_meter_sim = threading.Thread(target=self.meter_sim.meter_sim_run)
# Running meter_sim thread
        runs_meter_sim.start()
# Create instance of mqtt_client_listener, by that running Sniffer thread
        mqtt_client_listener.Sniffer()

if __name__ == "__main__":
    program().main()