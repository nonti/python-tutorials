class TemperatureConverter:
    def __init__(self, celsius: float):
        # Initialize the temperature in Celsius
        self.__celsius = celsius

    def set_temperature(self, celsius: float):
        # Update the temperature in Celsius
        self.__celsius = celsius

    def get_temperature(self):
        # Retrieve the temperature in Celsius
        return self.__celsius

# Create an instance of TemperatureConverter with an initial temperature of 25.0
temp_converter = TemperatureConverter(25.0)

# Update the temperature to 30.0
temp_converter.set_temperature(30.0)

# Print the current temperature
print(temp_converter.get_temperature())