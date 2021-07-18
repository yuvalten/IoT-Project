import mqtt_client_listener
import meter_sim


FILE_PATH = "/usr/bin/python3.8 /home/osboxes/Embedded/yuval-tenenbaum"

class Main:
    def __init__(self):
        self.mqtt_clnt_lstnr = mqtt_client_listener.Sniffer(("Meter", FILE_PATH))

    def main(self):
        self.decode_msg = self.mqtt_clnt_lstnr
        mtr_sm = meter_sim.MeterSim()
        mtr_sm.meter_sim_run()

        return print(self.decode_msg)

