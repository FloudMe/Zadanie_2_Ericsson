#function that collects the data and selects the appropriate function to convert
def mainConvert(typeOfConvert):
    print("\nPlease, type number to convert\n" +
          "if you want to exit type: exit\n" +
          "if you want to switch convert:\n" +
          "From binary to decimal type: binary\n" +
          "From decimal to binary type: decimal")

    while 1 == 1:
        data = input().lower() #get the output data and convert it to a lower case

        if data == "exit": #checking that user want exit program
            break
        elif data in ["binary", "decimal"]: #checking that user want switch type of data
            typeOfConvert = data
        else:
            try:
                number = int(data) #convert data to int, if data isn't correct then throw error
                if typeOfConvert == "binary": #checking which type is to convert
                    fromBinaryToDecimal(number)
                else:
                    fromDecimalToBinary(number)
            except ValueError:
                print("Incorect data")


#function in which we choose conversions at the beginning
def selectTypeOfConvertion():
    while 1 == 1:
        print("Please, select number conversion:\n" +
              "From binary to decimal type: binary\n" +
              "From decimal to binary type: decimal")

        typeOfConvert = input().lower() #get the output data and convert it to a lower case

        if typeOfConvert in ["binary", "decimal"]: #checking that user write correct type of data
            return typeOfConvert


#function that convert number from binary to decimal
def fromBinaryToDecimal(number):
    decimal = 0 #number in decimal
    counter = 0

    while number != 0:
        remainder = number % 10 #number of units

        if not 2 > remainder > -1: #checking that user write correct data (only 0 and 1)
            print("Incorect data")
            return

        decimal += remainder * int(2 ** counter)
        number = number // 10

        counter += 1

    print("Output: " + str(decimal))


#function that conbert number from decimal to binary
def fromDecimalToBinary(number):
    binary = 0 #number in binary
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
