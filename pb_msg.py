from input_parser import InputParser
from meter_telem import MeterTelem
import meter_pb2
# # files path = /usr/bin/python3.8 /home/osboxes/Embedded/yuval-tenenbaum

class PbMsg:

    def __init__(self):
        # self.bin_buffer = self.pb_encode_msg(mt)
        pass
    # convert meter telem to XMeterTelem (proto)
    def pb_convert(self,mt):
        mt_pb2 = meter_pb2.XMeterTelem()
        mt_pb2.TimeStamp = mt.TimeStamp
        mt_pb2.MeterType = mt.MeterType
        mt_pb2.PosEnergy = mt.PosEnergy
        mt_pb2.NegEnergy = mt.NegEnergy
        mt_pb2.PosActivePowerTotal = mt.PosActivePowerTotal
        mt_pb2.NegActivePowerTotal = mt.NegActivePowerTotal
        mt_pb2.CurrentA = mt.CurrentA
        mt_pb2.CurrentB = mt.CurrentB
        mt_pb2.CurrentC = mt.CurrentC
        mt_pb2.VoltageAN = mt.VoltageAN
        mt_pb2.VoltageBN = mt.VoltageBN
        mt_pb2.VoltageCN = mt.VoltageCN
        mt_pb2.Freq = mt.Freq
        mt_pb2.PosActivePowerA = mt.PosActivePowerA
        mt_pb2.PosActivePowerB = mt.PosActivePowerB
        mt_pb2.PosActivePowerC = mt.PosActivePowerC
        mt_pb2.NegActivePowerA = mt.NegActivePowerA
        mt_pb2.NegActivePowerB = mt.NegActivePowerB
        mt_pb2.NegActivePowerC = mt.NegActivePowerC
        return mt_pb2

    # serializing meter_pb2 proto to binnary string name bin_buffer
    def pb_encode_msg(self,mt):
        mt_pb2 = self.pb_convert(mt)
        with open("./meter_pb2.bin", "wb") as fd:
            bin_buffer = mt_pb2.SerializeToString()
            fd.write(bin_buffer)
            # print(bin_buffer)
        return bin_buffer

    # def pb_decode_msg(self):
    #     mt_pb2 = self.pb_convert(mt)
    #     mt_pb2.ParseFromString(self.bin_buffer)
    #     print(mt_pb2)

if __name__ == "__main__":
    mt = MeterTelem()
    msg = PbMsg()

