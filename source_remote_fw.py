#!/usr/bin/python

import socket

hostname=socket.gethostname()
slavehost = hostname + "s.local"

COMMANDS.append(
 Command('ssh %s dvsource-firewire'%slavehost)
)

"""
# everything hardcoded, it just works.  Don't forget to fill in the X.
COMMANDS.append(
 Command('ssh 10.0.0.x1 dvsource-firewire')
)

# magic woo try and fiure it out hope it works it never does.
import socket

hostname=socket.gethostname()
# master = "--host %s.local" % (hostname)
master = "--host %s" % (hostname)
port = "--port %s" % args.port if args.port else ''
hostport = ' '.join([master,port])

slave = 'juser@10.0.0.2'
# slave = 'juser@kasp'

COMMANDS.append(
 Command('ssh %s dvsource-firewire -c 0 %s' % (slave, hostport,))
)
"""

