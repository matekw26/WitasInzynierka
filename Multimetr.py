
import pyvisa

try:
    # obiekt VISA ResourceManager, który będzie zarządzał dostępem do urządzeń VISA.
    rm = pyvisa.ResourceManager()

    # Znajdź adres GPIB kalibratora i przypisz go do zmiennej.
    multimetr_address = 'GPIB0::25::INSTR' # adres GPIB kalibratora

    # Następnie otwórz połączenie z kalibratorem za pomocą metody "open_resource" obiektu ResourceManager,
    # podając jako argument adres GPIB kalibratora.
    multimetr = rm.open_resource(multimetr_address)

except:
    print("Błąd komunikacji")
    pass

if __name__ == "__main__":

    # "list_resources" obiektu ResourceManager, aby wyświetlić dostępne urządzenia VISA na Twoim komputerze.
    devices = rm.list_resources()
    print(devices)

    #multimetr.write('FUNC:FREQ')

    # fluke5100b.write('G')
    #fluke5100b.write("1V,")
    # response = fluke5100b.query('V?')
    # response = multimetr.query('?')
    # print(response)

    #response = multimetr.query('SYSTem:ERRor?')
    response = multimetr.query('READ?')
    print(response)

