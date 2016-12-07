import netmiko
import json
import getpass

devices = '''
wvwangw0a-loopback0.mentorg.com
wvwangw0b-loopback0.mentorg.com
'''.strip().splitlines()

device_type = 'cisco_ios'
username = raw_input("Enter device list username: ")
password = getpass.getpass(prompt='Enter device list password: ')

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

for name in devices :
    try :
        print('-'*79)
        print('Connecting to device', name)
        device = socket.gethostbyname(name)
        connection = netmiko.ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
        print(connection.send_command('bgp-sum-v4'))
        print(connection.send_command('bgp-adv-v4'))
        connection.disconnect()
    except netmiko_exceptions as e:
        print('Failed to ', device, e)
