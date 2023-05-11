import time
import pyvisa

try:
    # obiekt VISA ResourceManager, który będzie zarządzał dostępem do urządzeń VISA.
    rm = pyvisa.ResourceManager()

    # Znajdź adres GPIB kalibratora i przypisz go do zmiennej.
    multimetr_address = 'GPIB0::1::INSTR'  # adres GPIB dmm
    #
    # # Następnie otwórz połączenie z kalibratorem za pomocą metody "open_resource" obiektu ResourceManager,
    # # podając jako argument adres GPIB kalibratora.
    multimetr = rm.open_resource(multimetr_address)

except:
    print("Błąd komunikacji")
    pass

if __name__ == "__main__":

    # "list_resources" obiektu ResourceManager, aby wyświetlić dostępne urządzenia VISA na Twoim komputerze.
    devices = rm.list_resources()
    print(devices)


    # Sprawdź status połączenia
    try:
        multimetr.timeout = 5000
        # print(multimetr.timeout)
        ident = multimetr.query("*IDN?")
        print(f"Połączenie z urządzeniem {ident.strip()} zostało nawiązane.")
    except Exception as e:
        print(f"Wystąpił błąd podczas nawiązywania połączenia: {str(e)}")


    # multimetr.write('MEASure:VOLTage:DC')
    # # # # # # multimetr.write('MEASure:FREQuency')
    # # # # # # #
    # # # # # #
    # # # # # # #
    # # # # #
    multimetr.write('CONF:VOLT:DC')
    time.sleep(5)
    response = multimetr.query('READ?')
    # response = multimetr.query('MEASure:VOLTage:AC?')
    ## response = multimetr.query('FETCH?')
    # response = multimetr.query('MEASure:VOLTage:DC?')
    # response = multimetr.query('MEASure:CURRent:DC?')
    print(response)

    # response2 = multimetr.query('SYSTem:ERRor?')
    # print(response2)
