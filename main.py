def mainConvert(typeOfConvert):
    print("Please, type number to convert\n" +
          "if you want to exit type: exit\n" +
          "if you want to switch convert:\n" +
          "From binary to decimal type: binary\n" +
          "From decimal to binary type: decimal")

    while 1 == 1:
        data = input().lower()

        if data == "exit":
            break
        elif data in ["binary", "decimal"]:
            typeOfConvert = data
        else:
            try:
                number = int(data)
                if typeOfConvert == "binary":
                    fromBinaryToDecimal(number)
                else:
                    fromDecimalToBinary(number)
            except ValueError:
                print("Incorect data")


def selectTypeOfConvertion():
    while 1 == 1:
        print("Please, select number conversion:\n" +
              "From binary to decimal type: binary\n" +
              "From decimal to binary type: decimal")

        typeOfConvert = input().lower()

        if typeOfConvert in ["binary", "decimal"]:
            return typeOfConvert


def fromBinaryToDecimal(number):
    decimal = 0
    counter = 0
    while number != 0:
        remainder = number % 10
        if not 2 > remainder > -1:
            print("Incorect data")
            return

        decimal += remainder * int(2 ** counter)
        number = number // 10

        counter += 1

    print("Output: " + str(decimal))


def fromDecimalToBinary(number):
    binary = 0
    counter = 1

    while number != 0:
        remainder = number % 2
        number = number // 2
        binary += remainder * counter
        counter *= 10

    print("Output: " + str(binary))


if __name__ == "__main__":
    typeOfConvert = selectTypeOfConvertion()
    mainConvert(typeOfConvert)
