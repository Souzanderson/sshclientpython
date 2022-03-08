import paramiko


class SSHHost:
    def __init__(self, hostname, user, keylocation=None, pasw = None):
        self.__hostname = hostname
        self.__keylocation = keylocation
        self.__user = user
        self.__pasw = pasw
        
    @property
    def hostname(self):
         return self.__hostname
     
    @property
    def key(self):
         return self.__keylocation
    
    @property
    def user(self):
         return self.__user
    
    @property
    def password(self):
         return self.__pasw

class SSHClient:
    def __init__(self, host: SSHHost):
        self.__host = host
        self.client = paramiko.SSHClient()
        self.__commands = []
        
    def connect(self):
        try:
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname=self.__host.hostname, username = self.__host.user, password=self.__host.password, key_filename=self.__host.key)
        except Exception as e:
            print(e)
            
    def command(self, command):
        try:
            self.__commands.append(command)
        except Exception as e:
            print(e)
    
    def send_commands(self):
        try:
            stdin , stdout, stderr = self.client.exec_command(";".join(self.__commands))
            text_error = stderr.read().decode()
            if not text_error:
                text_out = stdout.readlines() 
                print("".join(text_out))
            else:
                print(text_error)
        except Exception as e:
            print(e)