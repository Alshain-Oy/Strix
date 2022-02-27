# Strix
Alshain Strix SMU Scripts & user guide

- [Wiki](https://github.com/Alshain-Oy/Strix/wiki) for user guide & specifications.
- [Examples](https://github.com/Alshain-Oy/Strix/tree/main/examples) folder for measurement scripts.
- [Labview library](https://github.com/Alshain-Oy/Strix/tree/main/Labview) is now also available.

## Quickstart

1) Connect usb data cable to _Data in_ port
2) Connect power adapter to Strix

```python
import libStrix
import serial

# replace "COM3" with corresponding port on your computer
com = serial.Serial( "COM3", 460800, timeout = 10.0 )

# Connect to SMU with address = 1 (default)
smu = libStrix.Strix( com, 1 )

# Measure both voltage and current
voltage, current = smu.measure()
```

## Snippets

### Basic usage
```python
# Measure both voltage and current
voltage, current = smu.measure()

# Measure voltage
voltage = smu.measure_voltage()

# Measure current
current = smu.measure_current()

# Measure ext voltage
vext = smu.measure_ext()

# Set drive voltage (eg. to 1V)
smu.set_drive_voltage( 1.0 )

# Set drive current (eg. to 1mA)
smu.set_drive_current( 1e-3 )
```

### Parameters
```python
# Number of averages per measurement -> Integration time = Navg / samplerate
smu.write( libStrix.PARAM_AVERAGES, 5 ) # eg. 5 averages per measurement

# Autoranging on/off
smu.write( libStrix.PARAM_AUTORANGING, libStrix.AUTORANGING_ON )
smu.write( libStrix.PARAM_AUTORANGING, libStrix.AUTORANGING_OFF )

# Set compliance voltage
smu.write_float( libStrix.PARAM_COMPLIANCE_VOLTAGE, 20.0 ) # set compliance voltage to 20V

# Set compliance current
smu.write_float( libStrix.PARAM_COMPLIANCE_CURRENT, 10e-3 ) # set compliance current to 10mA

# Set 4-wire mode on/off
smu.write( libStrix.PARAM_4WIRE_MODE, libStrix.ENABLE_4WIRE_MODE )
smu.write( libStrix.PARAM_4WIRE_MODE, libStrix.DISABLE_4WIRE_MODE )

# Select guard output reference (guard follows either Drive+ or Sense+)
smu.write( libStrix.PARAM_GUARD_MODE, libStrix.GUARD_MODE_DRIVE )
smu.write( libStrix.PARAM_GUARD_MODE, libStrix.GUARD_MODE_SENSE )

# Set voltage input fixed range
# valid gains are 1, 8, 64
# * 1  -> ±20V 
# * 8  -> ±2.5V 
# * 64 -> ±300mV 
smu.write( libStrix.PARAM_ADC_VOLTAGE_GAIN, 1 ) 

# Set current input fixed range
# valid gains are 1, 2, 3, 4
# * 1 -> ±10mA
# * 2 -> ±100µA
# * 3 -> ±1µA
# * 4 -> ±10nA
smu.write( libStrix.PARAM_LARGE_CURRENT_GAIN, 1 ) 

# Set ext voltage input fixed range
# valid gains are 1, 8, 64
# * 1  -> ±1V 
# * 8  -> ±125mV 
# * 64 -> ±15mV 
smu.write( libStrix.PARAM_EXT_VOLTAGE_GAIN, 1 ) 

# Set adc samplerate
# valid rates are 20, 45, 90, 175, 330, 600, 1000 
# 20sps (default) has integrated 50/60Hz filter so it is advisable to use that if possible
smu.write( libStrix.PARAM_ADC_SAMPLERATE, 20 ) 

# Set internal temperature stabilization on/off
# Strix has heaters to keep its internals at a constant temperature, heaters are turned off 
# during measurements to reduce any noise introduced to measurement, but they can be also
# turned off programmatically.
smu.write( libStrix.PARAM_THERMAL_MODE, libStrix.MODE_HEATER_OFF )
smu.write( libStrix.PARAM_THERMAL_MODE, libStrix.MODE_HEATER_AUTO )

# Set powerline cycle sync mode ie. synchronize measurements to start at a constant powerline phase
# Valid values:
# MODE_PLC_SYNC_NONE
# MODE_PLC_SYNC_50HZ (default)
# MODE_PLC_SYNC_60HZ
smu.write( libStrix.PARAM_PLC_SYNC_MODE, libStrix.MODE_PLC_SYNC_50HZ ) 

```

