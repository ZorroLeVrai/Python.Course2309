class MyMock:
    def __init__(self, expected_value_dico: dict[str, any]):
        self.__expected_value_dico = expected_value_dico

    def __getattr__(self, name):
        return self.__expected_value_dico.get(name)
