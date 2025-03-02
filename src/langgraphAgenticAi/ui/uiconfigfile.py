from configparser import ConfigParser

class Config:
    
    def __init__(self,config_file=".src\langgraphAgenticAi\ui\uiconfig.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)
        
    def get_llm_option(self):
        return self.config['DEFAULT'].get("LLM_OPTIONS").split(",")
    
    def get_usecase_option(self):
        return self.config['DEFAULT'].get("LLM_OPTIONS").split(",")
    
    def get_groqmodel_option(self):
        return self.config['DEFAULT'].get("LLM_OPTIONS").split(",")
    
    
    