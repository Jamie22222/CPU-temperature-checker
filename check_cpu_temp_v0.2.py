import subprocess as sp
import re as re


def check_cpu_temp():
    command = sp.getoutput(r'wmic/namespace:\\root\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature')
    pattern = r'[Current Temperature  /n/n                /n/n/n]'

    output = re.sub(pattern, '', command)
    int_output = int(output)
    processed_output = int_output / 10 - 273
    processed_output = int(processed_output)
    string_output = str(processed_output)

    return "Current CPU Temp: " + string_output + "°C"


def main():

    prompt = input("Press enter to check cpu temperature")
    if prompt == "":
        check_cpu_temp()


if __name__ == '__main__':
    main()

