import os.path as path


class FullPath:
    def __init__(self, root_path: str):
        self.root_path = root_path

    def get_full_path_from_relative_path(self, relative_path: str) -> str:
        return path.abspath(path.join(self.root_path, relative_path))
