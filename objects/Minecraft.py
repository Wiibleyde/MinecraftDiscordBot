import mcstatus
import os
from objects.Config import Config

class Minecraft:
    def __init__(self):
        self.config = Config(os.path.join(os.path.dirname(__file__), "../config.yml"))
        self.server = mcstatus.JavaServer.lookup(f"{self.config.get_minecraft_server()}:{self.config.get_minecraft_port()}")
    
    def get_status(self):
        return self.server.status()
    
    def is_online(self):
        if self.server.status() is None:
            return False
        else:
            return True
    
    def get_players(self):
        return self.server.status().players.online
    
    def get_max_players(self):
        return self.server.status().players.max
    
    def get_motd(self):
        return self.server.status().description
    
    def get_version(self):
        return self.server.status().version.name
    
    def get_favicon(self):
        return self.server.status().favicon
    
    def get_ping(self):
        return self.server.ping()
