#!/usr/bin/env python3

import sys
import serial
import time
import json
import libStrix

import numpy as np

com = serial.Serial( sys.argv[1], 460800, timeout = 25.0 )

smu = libStrix.Strix( com, 1 )


### Current measurement calibration



# Convinience function for peforming voltage sweep for current measurement calibration
def do_voltage_sweep( smu ):
    # Disable heaters to minimise noise
    smu.write( libStrix.PARAM_THERMAL_MODE, libStrix.MODE_HEATER_OFF )
    time.sleep(0.25)


    # Measurements
    Iref = []
    Imeas = []

    # Shunt resistor value (if used)
    R_ref = 269.7

    # go through set of excitation voltages:
    for v_test in [-2, -1, 0, 1, 2]:

        print( "Setting Vdrive to %.1fV" % v_test )

        smu.set_drive_voltage( v_test )

        # Allow some settling time
        time.sleep(1.0)

        # Measure current
        I = smu.measure_current()
        Imeas.append( I )

        # Ask user to read voltage drop over shunt resistor
        # Replace this with whatever other means of determining current you have

        V = float( input("Voltage? -> ") )
        Iref.append( V / R_ref ) 
        
        
        print( "")
    
    smu.set_drive_voltage( 0.0 )

    # Enable heaters
    smu.write( libStrix.PARAM_THERMAL_MODE, libStrix.MODE_HEATER_AUTO )
    
    return Imeas, Iref 







# For calibration, use manual ranging
smu.write( libStrix.PARAM_AUTORANGING, libStrix.AUTORANGING_OFF )

# To smooth out unnecessary noise
smu.write( libStrix.PARAM_AVERAGES, 32 )

# Current ranges:
# 1 -> ±10mA
# 2 -> ±100µA
# 3 -> ±1µA
# 4 -> ±100nA

# Voltage ranges:
# 1  -> ±20V 
# 8  -> ±2.5V 
# 64 -> ±300mV 

# Set voltage range for driving the reference resistor
smu.write( libStrix.PARAM_ADC_VOLTAGE_GAIN, 1 ) # ±20V 

# Set current range
smu.write( libStrix.PARAM_LARGE_CURRENT_GAIN, 1 ) # ±10mA

# for other ranges, please change compensation parameter labels to match accordingly


# Calibration should be done to non-compensated values
print( "Setting compensation to unity...")
smu.write_float( libStrix.PARAM_COMP_IMEAS_1_0, 0 )
smu.write_float( libStrix.PARAM_COMP_IMEAS_1_1, 1 )
smu.write_float( libStrix.PARAM_COMP_IMEAS_1_2, 0 )
smu.write_float( libStrix.PARAM_COMP_IMEAS_1_3, 0 )



print( "Performing voltage sweep and measurements..")

Imeas, Iref = do_voltage_sweep( smu )

print( "Results:" )
for i in range( len( Imeas ) ):
    print( "Imeas: %+.3e A\t Iref: %+.3e A" % (Imeas[i], Iref[i]) )
print( "" )

print( "Voltage sweep completed, computing polynomial fit..." )

compensation_order = 1 # Compensation polynomial order, 1 = linear, 2 = quadratic, 3 = cubic
coeffs = np.polyfit( Imeas, Iref, compensation_order ) 

# reverse coeffs to match Strix internal representation
coeffs = list( reversed( coeffs ) ) 

# Pad coeff list if less than 3rd order polynomial used
if len( coeffs ) < 4:
    coeffs.extend( [0.0]*(4 - len(coeffs) ) )


print( "I(x) = %.3e + %.3e x + %.3e x^2 + %.3e x^3" % tuple( coeffs ) )

print( "" )
response = input( "Write params to device? (y/n): ")

# if negative, stop here
if "n" in response.lower():
    sys.exit(0)

print( "" )
print( "Writing params to device...")
smu.write_float( libStrix.PARAM_COMP_IMEAS_1_0, coeffs[0] )
smu.write_float( libStrix.PARAM_COMP_IMEAS_1_1, coeffs[1] )
smu.write_float( libStrix.PARAM_COMP_IMEAS_1_2, coeffs[2] )
smu.write_float( libStrix.PARAM_COMP_IMEAS_1_3, coeffs[3] )

print( "" )
response = input( "Verify new params? (y/n): ")


# if negative, stop here
if "n" in response.lower():
    sys.exit(0)


print( "Performing voltage sweep and measurements..")

Imeas, Iref = do_voltage_sweep( smu )

print( "Results:" )
for i in range( len( Imeas ) ):
    print( "Imeas: %+.3e A\t Iref: %+.3e A\t dI: %+.3e A" % (Imeas[i], Iref[i], Iref[i] - Imeas[i]) )
print( "" )

print( "Voltage sweep completed, computing polynomial fit..." )

coeffs_2 = np.polyfit( Imeas, Iref, compensation_order )

# reverse coeffs to match Strix internal representation
coeffs_2 = list( reversed( coeffs_2 ) ) 

# Pad coeff list if less than 3rd order polynomial used
if len( coeffs_2 ) < 4:
    coeffs_2.extend( [0.0]*(4 - len(coeffs_2) ) )


print( "I(x) = %.3e + %.3e x + %.3e x^2 + %.3e x^3" % tuple( coeffs_2 ) )

print( "" )
print( "Compensation params:", json.dumps( {"imeas_1": coeffs})[1:-1] )




