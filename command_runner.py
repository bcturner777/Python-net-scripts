import netmiko
import json

devices = '''
172.16.217.50
172.16.217.51
'''.strip().splitlines()

device_type = 'cisco_ios'
username = input("Enter device list username: ")
password = input("Enter device list password: ")

for device in devices :
    connection = netmiko.ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
    print(connection.send_command('show clock'))
    connection.disconnect()
