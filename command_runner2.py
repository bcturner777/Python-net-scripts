import netmiko
import json
import socket
import getpass

device_group = raw_input("Enter device list seperated by space: ")

device_type = 'cisco_ios'
username = raw_input("Enter device list username: ")
password = getpass.getpass(prompt='Enter device list password: ')

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

for name in device_group.split():
    name = name.strip()
    device = socket.gethostbyname(name)
    try :
        print('-'*79)
        print('Connecting to device', device, name)
        connection = netmiko.ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
        print(connection.send_command('show clock'))
        connection.disconnect()
    except netmiko_exceptions as e:
        print('Failed to ', device, e)
