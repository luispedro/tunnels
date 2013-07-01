import optparse
from tunnels_version import __version__

_usage_simple = 'register-new-tunnel'
parser = optparse.OptionParser(usage=_usage_simple, version=__version__)
parser.add_option(
            '--final',
            action='store',
            dest='final',
            help='Destination host (IP or hostname)')
parser.add_option(
            '--final-name',
            action='store',
            dest='final_name',
            help='Name to use to connect (defaults to the same as ``final`` option)')
parser.add_option(
            '--intermediate',
            action='store',
            dest='intermediate',
            help='Intermediate host (IP or hostname)')
parser.add_option(
            '--intermediate-user',
            action='store',
            dest='intermediate_user',
            help='Intermediate user name (defaults to local username)')
parser.add_option(
            '--final-user',
            action='store',
            dest='final_user',
            help='Intermediate user name (defaults to intermediate username)')
parser.add_option(
            '--final-port',
            action='store',
            dest='final_port',
            default=22,
            help='Final port to reach (defaults to 22)')
options,args = parser.parse_args()

final = options.final
final_name = options.final_name
if final_name is None:
    final_name = final
intermediate = options.intermediate
local_port = 1223
final_port = options.final_port
final_user = options.final_user
if final_user is None:
    import getpass
    final_user = getpass.getuser()
intermediate_user = options.intermediate_user
if intermediate_user is None:
    intermediate_user = final_user

print('''
Host {NAME}
    User {FINAL_USER}
    Hostname 127.0.0.1
    Port {LOCAL_PORT}

Host {NAME}-tunnel
    User {INTERMEDIATE_USER}
    LocalForward {LOCAL_PORT} {FINAL}:{FINAL_PORT}
    HostName {INTERMEDIATE}
    ServerAliveInterval 120
'''.format(
        NAME=final_name,
        FINAL=final,
        INTERMEDIATE=intermediate,
        INTERMEDIATE_USER=intermediate_user,
        FINAL_USER=final_user,
        LOCAL_PORT=local_port,
        FINAL_PORT=final_port,
        ))

