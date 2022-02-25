#!/usr/bin/env python3

import sys
import serial
import time
import json
import libStrix

import numpy as np

com = serial.Serial( sys.argv[1], 460800, timeout = 25.0 )

smu = libStrix.Strix( com, 1 )


### Voltage drive and measurement calibration



# Convinience function for peforming voltage sweep for voltage drive & measurement calibration
def do_voltage_sweep( smu ):
    # Disable heaters to minimise noise
    smu.write( libStrix.PARAM_THERMAL_MODE, libStrix.MODE_HEATER_OFF )
    time.sleep(0.25)


    # Measurements
    Vdmm = []
    Vmeas = []
    Vdrive = []

    
    # go through set of excitation voltages:
    for v_test in [-2, -1, 0, 1, 2]:

        print( "Setting Vdrive to %.1fV" % v_test )

        smu.set_drive_voltage( v_test )

        # Store drive voltage
        Vdrive.append( v_test )

        # Allow some settling time
        time.sleep(1.0)

        # Measure voltage
        V = smu.measure_voltage()
        Vmeas.append( V )

        

        # Ask user to read voltage from DMM
        
        V = float( input("Voltage? -> ") )
        Vdmm.append( V  ) 
        
        
        print( "")
    
    smu.set_drive_voltage( 0.0 )

    # Enable heaters
    smu.write( libStrix.PARAM_THERMAL_MODE, libStrix.MODE_HEATER_AUTO )
    
    return Vdrive, Vmeas, Vdmm 







# For calibration, use manual ranging
smu.write( libStrix.PARAM_AUTORANGING, libStrix.AUTORANGING_OFF )

# To smooth out unnecessary noise
smu.write( libStrix.PARAM_AVERAGES, 32 )

# Voltage ranges:
# 1  -> ±20V 
# 8  -> ±2.5V 
# 64 -> ±300mV 

# Set voltage range to be calibrated
smu.write( libStrix.PARAM_ADC_VOLTAGE_GAIN, 8 ) # ±2.5V 



# for other ranges, please change compensation parameter labels to match accordingly


# Calibration should be done to non-compensated values
print( "Setting compensation to unity...")
smu.write_float( libStrix.PARAM_COMP_VDRIVE_1X_0, 0 )
smu.write_float( libStrix.PARAM_COMP_VDRIVE_1X_1, 1 )
smu.write_float( libStrix.PARAM_COMP_VDRIVE_1X_2, 0 )
smu.write_float( libStrix.PARAM_COMP_VDRIVE_1X_3, 0 )

smu.write_float( libStrix.PARAM_COMP_VMEAS_8X_0, 0 )
smu.write_float( libStrix.PARAM_COMP_VMEAS_8X_1, 1 )
smu.write_float( libStrix.PARAM_COMP_VMEAS_8X_2, 0 )
smu.write_float( libStrix.PARAM_COMP_VMEAS_8X_3, 0 )



print( "Performing voltage sweep and measurements..")

Vdrive, Vmeas, Vdmm = do_voltage_sweep( smu )

print( "Results:" )
for i in range( len( Vdrive ) ):
    print( "Vdrive: %+.3e V\t Vmeas: %+.3e V\t Vdmm: %+.3e V" % (Vdrive[i], Vmeas[i], Vdmm[i]) )
print( "" )

print( "Voltage sweep completed, computing polynomial fit..." )

compensation_order = 1 # Compensation polynomial order, 1 = linear, 2 = quadratic, 3 = cubic
drive_coeffs = np.polyfit( Vdrive, Vdmm, compensation_order ) 
meas_coeffs = np.polyfit( Vmeas, Vdmm, compensation_order ) 

# reverse coeffs to match Strix internal representation
drive_coeffs = list( reversed( drive_coeffs ) ) 
meas_coeffs = list( reversed( meas_coeffs ) ) 

# Pad coeff list if less than 3rd order polynomial used
if len( drive_coeffs ) < 4:
    drive_coeffs.extend( [0.0]*(4 - len(drive_coeffs) ) )

if len( meas_coeffs ) < 4:
    meas_coeffs.extend( [0.0]*(4 - len(meas_coeffs) ) )


print( "Vdrive(x) = %.3e + %.3e x + %.3e x^2 + %.3e x^3" % tuple( drive_coeffs ) )
print( "Vmeas(x)  = %.3e + %.3e x + %.3e x^2 + %.3e x^3" % tuple( meas_coeffs ) )


print( "" )
response = input( "Write params to device? (y/n): ")

# if negative, stop here
if "n" in response.lower():
    sys.exit(0)

print( "" )
print( "Writing params to device...")
smu.write_float( libStrix.PARAM_COMP_VDRIVE_1X_0, drive_coeffs[0] )
smu.write_float( libStrix.PARAM_COMP_VDRIVE_1X_1, drive_coeffs[1] )
smu.write_float( libStrix.PARAM_COMP_VDRIVE_1X_2, drive_coeffs[2] )
smu.write_float( libStrix.PARAM_COMP_VDRIVE_1X_3, drive_coeffs[3] )

smu.write_float( libStrix.PARAM_COMP_VMEAS_8X_0, meas_coeffs[0] )
smu.write_float( libStrix.PARAM_COMP_VMEAS_8X_1, meas_coeffs[1] )
smu.write_float( libStrix.PARAM_COMP_VMEAS_8X_2, meas_coeffs[2] )
smu.write_float( libStrix.PARAM_COMP_VMEAS_8X_3, meas_coeffs[3] )


print( "" )
response = input( "Verify new params? (y/n): ")


# if negative, stop here
if "n" in response.lower():
    sys.exit(0)


print( "Performing voltage sweep and measurements..")

Vdrive, Vmeas, Vdmm = do_voltage_sweep( smu )

print( "Results:" )
for i in range( len( Vdrive ) ):
    print( "Vdrive: %+.3e V\t Vmeas: %+.3e V\t Vdmm: %+.3e V\t dVdrive: %+.3e V\t dVmeas %+.3e V" % (Vdrive[i], Vmeas[i], Vdmm[i], Vdrive[i] - Vdmm[i], Vmeas[i] - Vdmm[i]) )
print( "" )

print( "Voltage sweep completed, computing polynomial fit..." )
drive_coeffs_2 = np.polyfit( Vdrive, Vdmm, compensation_order ) 
meas_coeffs_2 = np.polyfit( Vmeas, Vdmm, compensation_order ) 

# reverse coeffs to match Strix internal representation
drive_coeffs_2 = list( reversed( drive_coeffs_2 ) ) 
meas_coeffs_2 = list( reversed( meas_coeffs_2 ) ) 

# Pad coeff list if less than 3rd order polynomial used
if len( drive_coeffs_2 ) < 4:
    drive_coeffs_2.extend( [0.0]*(4 - len(drive_coeffs_2) ) )

if len( meas_coeffs_2 ) < 4:
    meas_coeffs_2.extend( [0.0]*(4 - len(meas_coeffs_2) ) )


print( "Vdrive(x) = %.3e + %.3e x + %.3e x^2 + %.3e x^3" % tuple( drive_coeffs_2 ) )
print( "Vmeas(x)  = %.3e + %.3e x + %.3e x^2 + %.3e x^3" % tuple( meas_coeffs_2 ) )


print( "" )
print( "Compensation params:", json.dumps( {"1x": drive_coeffs, "vmeas_8x": meas_coeffs})[1:-1] )




