# Import the connect handler module
from netmiko import ConnectHandler
# Create a dictionary representing the device.
testrouter = {
'device_type': 'cisco_ios',
'ip':   '134.86.133.30',
'username': 'cisco',
'password': 'cisco',
'secret': 'cisco',
}
# Connect to the device
net_connect = ConnectHandler(**testrouter)
# Elevate to enable mode
net_connect.enable()
# Import all configured routes into a variable
output = net_connect.send_command('show run | include ip route')
# Print the results for the variable "output"
print output
# exit enable mode
net_connect.exit_enable_mode()
# close the ssh session
net_connect.disconnect()
# end of the program
# stored at /usr/bin/route_scrape
