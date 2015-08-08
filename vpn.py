# This script will work on Ubuntu and Debian systems 
# leveraging Python 2.6.7 at this directory: /usr/bin/env python.

# Ensure that the proper libraries are installed by looking at the 
# 'import' statements below. In this case, you'll need: gobject, dbus

import sys
import traceback

import gobject

import dbus
import dbus.decorators
import dbus.mainloop.glib

import os

def catchall_signal_handler(*args, **kwargs):
    print ("Caught signal: "
           + kwargs['member'])
    if args[0] >= 6: #vpn disconnect (6) or failure (7)
        print ("Killing network connectivity...")
   
     # Replace eth0 to the name of your network adapter
        os.system('ifconfig eth0 down')
    raw_input("Press any key to enable your network adapter.")
    
    # Replace eth0 to the name of your network adapter
    os.system('ifconfig eth0 up')
    print ("Your network adapter has been enabled.")    

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    print ("Monitoring the VPN connection.")
    bus = dbus.SystemBus()
    bus.add_signal_receiver(catchall_signal_handler, signal_name='VpnStateChanged', interface_keyword='dbus_interface', member_keyword='member')
    loop = gobject.MainLoop()
    loop.run()
