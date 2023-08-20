class Temperature:
    def __init__(self, value):
        self.value = value

    def __getattr__(self, name):
        match name:
            case 'celsius':
                return self.value
            case 'fahrenheit':
                return self.value * 1.8 + 32
            case _:
                super().__getattr__(name)
    
    def __setattr__(self, name, value):
        match name:
            case 'celsius':
                self.value = value
            case 'fahrenheit':
                self.value = (value - 32) / 1.8
            case _:
                super().__setattr__(name, value)


ma_temperature = Temperature(37.5)
print(ma_temperature.fahrenheit) #99.5
ma_temperature.celsius = 25
print(ma_temperature.fahrenheit) #77.0