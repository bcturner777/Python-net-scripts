""" Simple netmiko command runner that checks the recieved and advertised
bgp routes for a list of specified ios-xe devices.
The command set sent by netmiko utilizes device alias exec commands on the devices.
Alias exec commands are useful when using long command sets directly on the device.  
However, for automation, using the full commands in automation programs is more scalable. """

import netmiko
import json
import getpass

devices = '''
172.16.217.50
172.16.217.51
'''.strip().splitlines()

device_type = 'cisco_ios'
username = input("Enter device list username: ")
password = getpass.getpass(prompt='Enter device list password: ')

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

for name in devices :
    try :
        print('-'*79)
        print('-'*79)
        print('Connecting to device', name)
        # Get socket by hostname allows hostname to IP resolution
        #device = socket.gethostbyname(name)
        connection = netmiko.ConnectHandler(ip=name, device_type=device_type, username=username, password=password)
        print('\n **************************** RECIEVED BGP ROUTES **************************** \n')
        print(connection.send_command('bgp-rec'))
        print('\n *************************** ADVERTISED BGP ROUTES *************************** \n')
        print(connection.send_command('bgp-adv'))
        connection.disconnect()
    except netmiko_exceptions as e:
        print('Failed to ', device, e)
