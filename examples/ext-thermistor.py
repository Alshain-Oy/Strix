#!/usr/bin/env python3


import sys
import serial
import time
import math

import libStrix


# Computes resistance using voltage divider
# Rdiv = resistance between measurement point and ground
# Vdiv = Excitation voltage of the divider 
# Vmeas = Measured voltage
def voltage_divider_compute_resistance( Rdiv, Vdiv, Vmeas ):
    return ( Vdiv / Vmeas - 1 ) * Rdiv


# Compute temperature from thermistor resistance (B parameter)
def thermistor_temperature_B( R25, B, Rmeas ):
    invT = 1.0 / 298.15 + 1.0 / B * math.log( Rmeas / R25 )

    return 1.0 / invT

# Compute temperature from thermistor resistance (Steinhart-Hart)
def thermistor_temperature_SH( a, b, c, Rmeas ):
    invT = a + b * math.log( Rmeas ) + c * ( math.log( Rmeas ) )**3

    return 1.0 / invT

# Open connection to SMU
com = serial.Serial( sys.argv[1], 460800, timeout = 25.0 )
smu = libStrix.Strix( com, 1 )

## Settings 
smu.write( libStrix.PARAM_AVERAGES, 5 )

# set ext voltage input range as +-1 V
smu.write( libStrix.PARAM_EXT_VOLTAGE_GAIN, 1)

# Measure ext voltage
vext = smu.measure_ext()

# as an example: Divider excitation voltage = 1V, divider resistance = 10k
R = voltage_divider_compute_resistance( Rdiv = 10e3, Vdiv = 1.0, Vmeas = vext )

# thermistor params: R25 = 10k, B = 3984
T = thermistor_temperature_B( R25 = 10e3, B = 3984, Rmeas = R )

print( "Temperature: %.3f C" % (T - 273.15) )


com.close()