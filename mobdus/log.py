import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import serial
import time

modbusServ = modbus_rtu.RtuServer(serial.Serial('USB0'), baudrate=19200,
                                  bytesize=8, parity='N', stopbits=1, xonxoff=0)
print("start")

modbusServ.start()

slave_1 = modbus_tk.modbus.Slave(1)

slave_1.add_block("1", modbus_tk.defines.HOLDING_REGISTERS, 1, 5)

aa = (1, 2, 3, 4, 5)  # data in the register

while True:
    slave_1.set_values("1", 1, aa)
    time.sleep(0.5)
