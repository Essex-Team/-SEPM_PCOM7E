import os
import json

class Utils:

    @staticmethod
    def saveContentToJSON(filename: str, data: any) -> None:
        temp_dir = os.path.join(os.getcwd(), 'temp')

        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        with open(os.path.join(temp_dir, filename), 'w+', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def loadContentFromJSON(filename: str) -> any:
        temp_dir = os.path.join(os.getcwd(), 'temp')
        
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        with open(os.path.join(temp_dir, filename), 'r+', encoding='utf-8') as f:
            data = json.load(f)
        return data

    @staticmethod
    def getAssetPath(filename: str) -> str:
        root_dir = os.path.abspath(os.curdir)
        return os.path.join(root_dir, f'assets/{filename}')
