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
        try:
            if self.server.status() is None:
                return False
            return True
        except:
            return False
    
    def get_players(self):
        try:
            return self.server.status().players.online
        except:
            return -1
    
    def get_max_players(self):
        try:
            return self.server.status().players.max
        except:
            return -1
    
    def get_motd(self):
        try:
            return self.server.status().description
        except:
            return False
    
    def get_version(self):
        try:
            return self.server.status().version.name
        except:
            return False
    
    def get_favicon(self):
        try:
            return self.server.status().favicon
        except:
            return False
    
    def get_ping(self):
        try:
            return self.server.ping()
        except:
            return -1
    
    def get_players_list(self):
        try:
            return self.server.status().players.sample
        except:
            return False
