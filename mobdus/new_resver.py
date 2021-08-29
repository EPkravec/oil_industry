#!/usr/bin/python
# -*- coding: utf-8 -*-
import serial
from pymodbus.client.sync import ModbusSerialClient
import logging
import threading

FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)


import sys
import time

def gogogo(unit, port):
    while True:
        client = ModbusSerialClient(
            method="rtu",
            port=port,
            xonxoff=False,
            rtscts=False,
            baudrate=57600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.EIGHTBITS,
            timeout=1.0)

        logging.info('SENDING COMMAND')
        try:
            client.connect()
        except:
            logging.info('no connect')
        # rw1 = client.read_holding_registers(4, 6, unit=unit)
        # time.sleep(2)
        # rw2 = client.read_holding_registers(4, 1, unit=unit)
        # time.sleep(2)
        try:
            in0 = client.read_holding_registers(0x30, 0xFF, unit=unit)
            time.sleep(2)
        except:
            logging.info('no connect in0 ')
        try:
            in1 = client.read_holding_registers(0x31, 0xFF, unit=unit)
            time.sleep(2)
        except:
            logging.info('no connect in1 ')
        try:
            in2 = client.read_holding_registers(0x32, 0xFF, unit=unit)
            time.sleep(2)
        except:
            logging.info('no connect in2')
        try:
            in3 = client.read_holding_registers(0x33, 0xFF, unit=unit)
        except:
            logging.info('no connect in3')

        # if not rw1.isError():
        #     logging.info(rw1.registers)
        #     logging.error(rw1.registers[0])
        # else:
        #     logging.info(rw1)
        # if not rw2.isError():
        #     logging.info(rw2.registers)
        # else:
        #     logging.info(rw2)
        if not in0.isError():
            logging.info(in0.registers)
        else:
            logging.info(in0)
        if not in1.isError():
            logging.info(in1.registers)
        else:
            logging.info(in1)
        if not in2.isError():
            logging.info(in2.registers)
        else:
            logging.info(in2)
        if not in3.isError():
            logging.info(in3.registers)
        else:
            logging.info(in3)



        # if len(rw1.registers) == 6:
        #     logging.info('mini bybyx')
        #
        # if len(rw2.registers) == 1:
        #     logging.info('maxi bybyx')



if __name__ == '__main__':
    unit = 0xA1
    port = '/dev/ttyUSB0'
    while True:
        a = gogogo(unit, port)
        b = threading.Thread(target=a)
        b.start()
        time.sleep(7)