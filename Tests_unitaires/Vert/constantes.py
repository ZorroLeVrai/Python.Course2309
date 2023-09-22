import pathlib

JSON_PATH = "../config.json"


def getFileDirectory() -> str:
    return pathlib.Path(__file__).parent.resolve()


MAIN_DIRECTORY = getFileDirectory()
