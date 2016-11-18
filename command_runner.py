import netmiko
import json

devices = '''
tahwangw1
tahwanex1
'''.strip().splitlines()

device_type = 'cisco_ios'
username = raw_input("Enter device list username: ")
password = raw_input("Enter device list password: ")

for device in devices :
    connection = netmiko.ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
    print(connection.send_command('show clock'))
    connection.disconnect()
