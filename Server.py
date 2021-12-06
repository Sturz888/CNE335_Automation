import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        response = os.system("ping " + self.server_ip)
        return response

    def updat(self):
        pwd = ""
        svr = self.server_ip
        remote = paramiko.SSHClient()
        remote.load_system_host_keys()
        remote.connect(hostname=svr, username="ubuntu", password=pwd)
        if remote.get_transport() is not None:
            active = remote.get_transport().is_active()
            print('transportactive:', active)

        cmd = 'sudo apt-get update -y'
        first, out, err = remote.exec_command(cmd)
        first.flush()
        data = out.read().splitlines()
        for line in data:
            print(line)
        cmd = 'sudo apt-get upgrade -y'
        first, out, err = remote.exec_command(cmd)
        first.flush()
        data = out.read().splitlines()
        for line in data:
            print(line)
        remote.close()

