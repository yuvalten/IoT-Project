import mqtt_client_listener
import meter_sim
class Main:
    def main(self):
        self.Mqtt_Client_Listener = mqtt_client_listener.Sniffer("Meter","/home/osboxes/Embedded/yuval-tenenbaum/parse.json",)
        self.Meter_Sim = meter_sim.MeterSim()


        return(mqtt_client_listener.data)