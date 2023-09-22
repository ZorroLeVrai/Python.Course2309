from os.path import exists


class FileLoader:
    def __init__(self, full_path: str):
        if exists(full_path):
            with open(full_path) as config_file:
                self.__configuration_content = config_file.read()
        else:
            raise FileNotFoundError(
                r"Configuration file not found: {full_path}")

    @property
    def configuration_content(self):
        return self.__configuration_content
