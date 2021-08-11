# Strix
Alshain Strix SMU Scripts & user guide

- [Wiki](https://github.com/Alshain-Oy/Strix/wiki) for user guide & specifications.
- [Examples](https://github.com/Alshain-Oy/Strix/tree/main/examples) folder for measurement scripts.
 

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

# Set drive voltage (eg. to 1V)
smu.set_drive_voltage( 1.0 )

# Set drive current (eg to 1mA )
smu.set_drive_current( 1e-3 )
```
