# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MPL3115A2
# This code is designed to work with the MPL3115A2_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/products

import smbus
import time
import logging

logging.basicConfig(level=logging.DEBUG)



def alt_data_parser(data):
    """
    Extract and convert the data stream to actual numbers using Altimeter mode
    """
    # Convert the data to 20-bits
    tHeight = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
    temp = ((data[4] * 256) + (data[5] & 0xF0)) / 16
    altitude = tHeight / 16.0
    cTemp = temp / 16.0
    fTemp = cTemp * 1.8 + 32
    return (tHeight,temp,altitude,cTemp,fTemp)


def pres_data_parser(data):
    """
    Extract and convert the data stream from pressure mode.
    """
    # Convert the data to 20-bits
    pres = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
    pressure = (pres / 4.0) / 1000.0
    return (pres,pressure)




def readData(mode=1):
    """
    Extracts data in Altitude mode,
    The current sensor is broken so I can't get data on 
    Parameters : 
        mode : Int, 1 : Temperature and Altitude mode, 2: Pressure  mode.
    """

    # Get I2C bus
    bus = smbus.SMBus(1)

    I2addr = 96 # MPL3115A2 address, 0x60(96)
    control_register = 38 # Select control register, 0x26(38)
    alti_active_mode = 185 #0xB9(185)	Active mode, Altimeter_mode 
    otro_active_mode = 184
    OSR = 128  #OSR = 128, Altimeter mode
    data_conf_reg = 19  # Select data configuration register, 0x13(19)
    dre_alt_pres_temp = 7  #Data ready event enabled for altitude, pressure, temperature
    read_data_back_from_addr = 0  # Read data back from 0x00(00), 6 bytes
    alt_n_bytes = 6

    ## According to figure 7 from : https://www.nxp.com/docs/en/data-sheet/MPL3115A2.pdf
    if int(mode) == 1 :
        logging.info("Reading in altimeter mode")
        ## Set to altimeter
        bus.write_byte_data(I2addr,control_register,otro_active_mode)
        ## Enable data flags
        bus.write_byte_data(I2addr,data_conf_reg,dre_alt_pres_temp)
        ## Altimeter
        bus.write_byte_data(I2addr,control_register,alti_active_mode)
        time.sleep(1)
        # status, tHeight MSB1, tHeight MSB, tHeight LSB, temp MSB, temp LSB
        data_alt = bus.read_i2c_block_data(I2addr,read_data_back_from_addr,alt_n_bytes)
        tHeight, temp, altitude, cTemp, fTemp = alt_data_parser(data_alt)
        data = {"Temperature" : cTemp, "Altitude":altitude}
    elif int(mode) == 2:
        logging.info("Reading in barimeter mode")
        ## BAROMETER MODE
        #0xB9(57)	Active mode, 
        bar_active_mode = 57  #	0x39(57) Active mode, OSR = 128, Barometer mode
        bus.write_byte_data(I2addr,data_conf_reg, bar_active_mode)
        time.sleep(1)
        # Read data back from 0x00(00), 4 bytes
        pres_n_bytes = 4
        # status, pres MSB1, pres MSB, pres LSB
        data_pres = bus.read_i2c_block_data(I2addr,read_data_back_from_addr,pres_n_bytes)
        pres, pressure = pres_data_parser(data_pres)
        data = {"Pressure" : pressure}
    else :
        raise ValueError("Wrong selection of mode. See documentation.")
    return data



def main():
    d = readData(mode=1)
    p = readData(mode=2)
    # Output data to screen
    print "Pressure : %.2f kPa" %p['Pressure']
    print "Altitude : %.2f m" %d['Altitude']
    print "Temperature in Celsius  : %.2f C" %d['Temperature']

if __name__ == '__main__':
    main()


