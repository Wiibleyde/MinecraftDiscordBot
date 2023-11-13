import mcrcon
import os
from objects.Config import Config

class MinecraftRcon:
    def __init__(self):
        self.config = Config(os.path.join(os.path.dirname(__file__), "../config.yml"))
        self.rcon = mcrcon.MCRcon(self.config.get_minecraft_server(), self.config.get_minecraft_rcon_password(), self.config.get_minecraft_rcon_port())

    def send_command(self, command):
        self.rcon.connect()
        resp = self.rcon.command(command)
        self.rcon.disconnect()
        return resp
    