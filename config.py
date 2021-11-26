from yaml import safe_load


class Config:
    def __init__(self):
        self.read()

    def read(self):
        #read yaml config file
        with open("conf.yml", 'r') as stream:
            config = safe_load(stream)

        print(config)
        self.toggle_key = config['toggle']
        self.bg_color = config['bg']
        self.border = config['border_px']
        self.border_color = config['border_color']


