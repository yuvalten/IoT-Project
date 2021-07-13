import meter_telem
import meter_pb2

class PbMsg:

    def __init__(self):
        # self.bin_buffer = bin_buffer
        self.MeterTelem = meter_telem.MeterTelem()

    def pb_encode_msg(self):
         MeterTelem = meter_pb2.XMeterTelem
         with open("./meter_pb2.py", "wb") as fd:
             bin_buffer = fd.write(MeterTelem.SerializeToString())
         # print(bin_buffer)

         return bin_buffer
         # self.bin_buffer.SerializeToString()
         # self.bin_buffer = meter_pb2.SerializeToString

if __name__ == "__main__":
    msg = PbMsg()
    msg.pb_encode_msg()


