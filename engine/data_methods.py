import os
import json

class DataMethods:
    
    def __init__(self):
        pass
    
    def load_data(self, file_name):
        
        current_dir = os.path.dirname(__file__)  # Gets the directory of the current file
        file_path = os.path.join(current_dir, '..', 'game_data', file_name)

        # Load details from JSON file
        with open(file_path) as file:
            data = json.load(file)
        
        return data
