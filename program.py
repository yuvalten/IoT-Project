import mqtt_client_listener
import meter_sim

class Main:
    def main(self):
        mqtt_clnt_lstnr = mqtt_client_listener
        decode_msg = mqtt_clnt_lstnr.Sniffer("Meter","/home/osboxes/Embedded/yuval-tenenbaum/parse.json")
        mtr_sm = meter_sim.MeterSim()
        mtr_sm.meter_sim_run()

        return print(decode_msg)

