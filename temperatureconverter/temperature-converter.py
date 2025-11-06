import converterfunctions

welcome_text = r"""                                                                                           
 _____                           _                                          _              _____ ___     ___ 
|_   _|___ _____ ___ ___ ___ ___| |_ _ _ ___ ___    ___ ___ ___ _ _ ___ ___| |_ ___ ___   |  |  |_  |   |   |
  | | | -_|     | . | -_|  _| .'|  _| | |  _| -_|  |  _| . |   | | | -_|  _|  _| -_|  _|  |  |  |_| |_ _| | |
  |_| |___|_|_|_|  _|___|_| |__,|_| |___|_| |___|  |___|___|_|_|\_/|___|_| |_| |___|_|     \___/|_____|_|___|
                |_|                                                                                          """

converter_is_on = True
valid_units = ["°C" , "°K","°R","°F"]
unit_indexes = [0,1,2,3]
converted_temperature = 0


while converter_is_on:
    # Get starting temperature unit
    from_unit = int(input("What unit do you want to convert from ?? :\n0:°C\n1:°K\n2:°R\n3:°F \n"))

    # Get target temperature unit
    to_unit = int(input("What unit do you want to convert to ?? :\n0:°C\n1:°K\n2:°R\n3:°F \n"))



    if from_unit in unit_indexes and to_unit in unit_indexes and not to_unit == from_unit :
        temperature = float(input("What is the value ??"))

        #convert
        if from_unit == 0 and to_unit == 1:  # °C → °K
            converted_temperature = converterfunctions.celsius_to_kelvin(temperature)
        elif from_unit == 1 and to_unit == 0:  # °K → °C
            converted_temperature = converterfunctions.kelvin_to_celsius(temperature)
        elif from_unit == 0 and to_unit == 3:  # °C → °F
            converted_temperature = converterfunctions.celsius_to_fahrenheit(temperature)
        elif from_unit == 3 and to_unit == 0:  # °F → °C
            converted_temperature = converterfunctions.fahrenheit_to_celsius(temperature)
        elif from_unit == 3 and to_unit == 1:  # °F → °K
            converted_temperature = converterfunctions.fahrenheit_to_kelvin(temperature)
        elif from_unit == 1 and to_unit == 3:  # °K → °F
            converted_temperature = converterfunctions.kelvin_to_fahrenheit(temperature)
        elif from_unit == 0 and to_unit == 2:  # °C → °R
            converted_temperature = converterfunctions.celsius_to_rankine(temperature)
        elif from_unit == 2 and to_unit == 0:  # °R → °C
            converted_temperature = converterfunctions.rankine_to_celsius(temperature)
        elif from_unit == 3 and to_unit == 2:  # °F → °R
            converted_temperature = converterfunctions.fahrenheit_to_rankine(temperature)
        elif from_unit == 2 and to_unit == 3:  # °R → °F
            converted_temperature = converterfunctions.rankine_to_fahrenheit(temperature)
        elif from_unit == 1 and to_unit == 2:  # °K → °R
            converted_temperature = converterfunctions.kelvin_to_rankine(temperature)
        elif from_unit == 2 and to_unit == 1:  # °R → °K
            converted_temperature = converterfunctions.rankine_to_kelvin(temperature)

            # Display result
        print(f"\n{temperature}{valid_units[from_unit]} = {converted_temperature:.2f}{valid_units[to_unit]}\n")

    elif from_unit in unit_indexes and to_unit in unit_indexes and to_unit == from_unit:
        print("value")
    elif from_unit not in unit_indexes or to_unit not in unit_indexes:
        print("Invalid choice")





    # Get input from the user

    # Convert to desired unit
