from mockClass import MyMock

mock = MyMock({"print": lambda x: print(x)})
mock.print("Hello World!")
