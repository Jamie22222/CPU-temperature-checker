# import packages
import subprocess as sp
import re as re


def check_cpu_temp():

    # wmic command for getting the cpu temperature in tenths of a kelvin
    command = sp.getoutput(r'wmic/namespace:\\root\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature')

    # variable for output format
    pattern = r'[Current Temperature  /n/n                /n/n/n]'

    # formatting the output to return celcius
    output = re.sub(pattern, '', command)
    # convert the string output to int to do arithmetic on it
    int_output = int(output)
    processed_output = int_output / 10 - 273
    processed_output = int(processed_output)
    string_output = str(processed_output)

    return "Current CPU Temp: " + string_output + "°C"


def main():
    check_cpu_temp()


# driver code
if __name__ == '__main__':
    main()
