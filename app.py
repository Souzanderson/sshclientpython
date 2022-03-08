from config import HOST, KEY_FILE, PASSWORD, USER
from sshclient import SSHHost, SSHClient

host = SSHHost(HOST, USER, KEY_FILE, PASSWORD)
client = SSHClient(host)

client.connect()
client.command("dir")
client.command("cd handdetection")
client.command("dir")
client.send_commands()