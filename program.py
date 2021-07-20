import mqtt_client_listener
import meter_sim
import threading
import time


FILE_PATH = "/usr/bin/python3.8 /home/osboxes/Embedded/yuval-tenenbaum"

class Main:
    def __init__(self):
        self.mqtt_client_listener = mqtt_client_listener.Sniffer(("Meter", FILE_PATH))
        self.meter_sim_run = meter_sim.MeterSim()
        self.publish_rate = 5
        self.runs_mqtt_client_listener = threading.Thread(target=self.mqtt_client_listener)
        self.runs_meter_sim = threading.Thread(target=self.meter_sim_run)

    def main(self):
        self.decode_msg = self.mqtt_client_listener
        time.sleep(self.publish_rate)
        self.meter_sim_run.meter_sim_run(publish_rate=5)
        time.sleep(self.publish_rate)
        return print(self.decode_msg)

