# 1 Zainstaluj bibliotekę PyVISA - pip install pyvisa i visa

import pyvisa
import visa

try:
    # obiekt VISA ResourceManager, który będzie zarządzał dostępem do urządzeń VISA.
    rm = pyvisa.ResourceManager()

    # Znajdź adres GPIB kalibratora i przypisz go do zmiennej.
    fluke5100b_address = 'GPIB0::7::INSTR'  # adres GPIB kalibratora

    # Następnie otwórz połączenie z kalibratorem za pomocą metody "open_resource" obiektu ResourceManager,
    # podając jako argument adres GPIB kalibratora.
    fluke5100b = rm.open_resource(fluke5100b_address)
except:
    print("Błąd komunikacji")
    pass

if __name__ == "__main__":

    # "list_resources" obiektu ResourceManager, aby wyświetlić dostępne urządzenia VISA na Twoim komputerze.
    devices = rm.list_resources()
    print(devices)

    fluke5100b.write('CC')
    fluke5100b.write('J')
    fluke5100b.write('1V60H,')
    fluke5100b.write('S')
    fluke5100b.write('CC')

    # fluke5100b.write('G')
    #fluke5100b.write("1V,")
    # response = fluke5100b.query('V?')
    response = fluke5100b.query('?')
    print(response)
    response2 = fluke5100b.query('!?')
    print(response2)

    #
    # # jakby trzeba było zmienić bound_rate
    # # fluke5100b.baud_rate = 57600
    #
    # response = fluke5100b.query('SYSTem:ERRor?')
    # print(response)
    #
    # Zamykamy połączenie z kalibratorem
    fluke5100b.close()
    #
    #
    # def set_voltage(voltage):
    #     # Tworzymy obiekt VISA ResourceManager
    #     rm = visa.ResourceManager()
    #
    #     # Przypisujemy adres GPIB kalibratora do zmiennej
    #     fluke5100b_address = 'GPIB0::22::INSTR'
    #
    #     # Otwieramy połączenie z kalibratorem
    #     fluke5100b = rm.open_resource(fluke5100b_address)
    #
    #     # Ustawiamy tryb ręcznego ustawiania wartości napięcia
    #     fluke5100b.write('FUNCtion:VOLTage:MODE MANual')
    #
    #     # Ustawiamy wartość napięcia na 10 V
    #     fluke5100b.write('VOLTage:MANual 10')
    #
    #     # Wyświetlamy ustawioną wartość napięcia
    #     response = fluke5100b.query('VOLTage:MANual?')
    #     print(f'Ustawiona wartość napięcia: {response} V')
    #
    #     # Zamykamy połączenie z kalibratorem
    #     fluke5100b.close()
