import os
import json

class Utils:

    @staticmethod
    def saveContentToJSON(filename: str, data: any) -> None:
        with open(filename, 'w+', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def loadContentFromJSON(filename: str) -> any:
        with open(filename, 'r+', encoding='utf-8') as f:
            data = json.load(f)
        return data

    @staticmethod
    def getAssetPath(filename: str) -> str:
        root_dir = os.path.abspath(os.curdir)
        return os.path.join(root_dir, f'assets/{filename}')
