import serial
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

client = ModbusClient(port='COM2',
                      bytesize=serial.EIGHTBITS,
                      parity=serial.PARITY_NONE,
                      stopbits=serial.STOPBITS_TWO,
                      timeout=0.3,
                      method='rtu',
                      baudrate=9600)
connection = client.connect()
print('status connection - ', connection)

value = client.read_input_registers(2)
print(value)

client.close()
