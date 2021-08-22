# import sys
#
# import modbus_tk
# import modbus_tk.defines as cst
# from modbus_tk import modbus_rtu
# import serial
#
#
# PORT = 8080
# # PORT = '/dev/ptyp5'
#
# def main():
#     """main"""
#     logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")
#
#     #Create the server
#     server = modbus_rtu.RtuServer(serial.Serial(PORT))
#
#     try:
#         logger.info("running...")
#         logger.info("enter 'quit' for closing the server")
#
#         server.start()
#
#         slave_1 = server.add_slave(1)
#         slave_1.add_block('0', cst.HOLDING_REGISTERS, 0, 100)
#         while True:
#             cmd = sys.stdin.readline()
#             args = cmd.split(' ')
#
#             if cmd.find('quit') == 0:
#                 sys.stdout.write('bye-bye\r\n')
#                 break
#
#     finally:
#         server.stop()
#
# if __name__ == "__main__":
#     main()
import serial

port = '8080'
serial_comunication = serial.Serial(port, baudrate=4800, timeout=0.75)
serial_comunication.write(b'frame')
answer = serial_comunication.read(255)
serial_comunication.close()
print (answer.decode())