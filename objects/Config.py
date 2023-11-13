import yaml
import os

class Config:
    def __init__(self, path):
        self.defaultConfig = {
            "minecraft": {
                "server": "",
                "port": 25565
            },
            "rcon": {
                "password": "",
                "port": 25575
            },
            "discord": {
                "token": "",
                "prefix": "!",
                "owner": "wiibleyde"
            }
        }
        self.path = path
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.path):
            self.create_config()
        with open(self.path, "r") as f:
            return yaml.load(f, Loader=yaml.FullLoader)
        
    def create_config(self):
        with open(self.path, "w") as f:
            yaml.dump(self.defaultConfig, f, default_flow_style=False)

    def get_config(self):
        return self.config
    
    def get_minecraft_server(self):
        return self.config["minecraft"]["server"]
    
    def get_minecraft_port(self):
        return self.config["minecraft"]["port"]
    
    def get_discord_token(self):
        return self.config["discord"]["token"]
    
    def get_discord_prefix(self):
        return self.config["discord"]["prefix"]
    
    def get_discord_owner(self):
        return self.config["discord"]["owner"]
    
    def get_minecraft_rcon_password(self):
        return self.config["rcon"]["password"]
    
    def get_minecraft_rcon_port(self):
        return self.config["rcon"]["port"]
    
    def set_minecraft_server(self, server):
        self.config["minecraft"]["server"] = server
        self.save_config()

    def set_minecraft_port(self, port):
        self.config["minecraft"]["port"] = port
        self.save_config()

    def set_discord_token(self, token):
        self.config["discord"]["token"] = token
        self.save_config()

    def set_discord_prefix(self, prefix):
        self.config["discord"]["prefix"] = prefix
        self.save_config()

    def set_discord_owner(self, owner):
        self.config["discord"]["owner"] = owner
        self.save_config()

    def set_minecraft_rcon_password(self, password):
        self.config["rcon"]["password"] = password
        self.save_config()

    def set_minecraft_rcon_port(self, port):
        self.config["rcon"]["port"] = port
        self.save_config()

    def save_config(self):
        with open(self.path, "w") as f:
            yaml.dump(self.config, f, default_flow_style=False)
