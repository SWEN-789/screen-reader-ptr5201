"""
Author: Philip Rodriguez
Date created: 01/24/2019
Date last modified: 01/26/2019
"""

import ctypes

"""
Returns a list of numbers in the Fibonacci sequence starting at 0

@param numFibNumbers: the number of numbers to return from the Fibonacci sequence
@return: a list of numbers, with the size set to the number entered by the user, in the Fibonacci sequence starting at 0
"""
def fibonacci(numFibNumbers):
    fibNumbers = list()
    currentFibNumber = 0
    for fibNumberIndex in range(numFibNumbers):
        if fibNumberIndex < 2:
            currentFibNumber = currentFibNumber + fibNumberIndex
        else:
            currentFibNumber = fibNumbers[fibNumberIndex - 2] + fibNumbers[fibNumberIndex - 1]
        fibNumbers.append(currentFibNumber)
    return fibNumbers



# Load the NVDA client library
clientLib=ctypes.windll.LoadLibrary('./nvdaControllerClient32.dll')

# Test if NVDA is running, and if its not show a message
res=clientLib.nvdaController_testIfRunning()
if res!=0:
    errorMessage=str(ctypes.WinError(res))
    ctypes.windll.user32.MessageBoxW(0,u"Error: %s"%errorMessage,u"Error communicating with NVDA",0)
else:
    # Needed for compatibility with Python 2 and Python 3 in getting user input
    try:
        input = raw_input
    except NameError:
        pass

    # Establish the boundaries of the input for the number of numbers to return from the Fibonacci sequence
    inputMustBeGreaterThan = 0
    inputMustBeLessThan = 25

    # Create the message to prompt the user
    promptMessage = u"Enter how many numbers to return from the Fibonacci sequence (first number starts at 0; input must be greater than " + str(inputMustBeGreaterThan) + " and less than " + str(inputMustBeLessThan) + ")"

    # Speak, print and send the prompt message in braille
    clientLib.nvdaController_speakText(promptMessage)
    clientLib.nvdaController_brailleMessage(promptMessage)
    numFibNumbersToSpeak = input(promptMessage+": ")
    try:
        numFibNumbersToSpeak = int(numFibNumbersToSpeak)
    except ValueError:
        pass

    # If the input number is within the boundaries, then get the Fibonacci numbers
    if type(numFibNumbersToSpeak) is int and numFibNumbersToSpeak > inputMustBeGreaterThan and numFibNumbersToSpeak < inputMustBeLessThan:
        fibNumbersList = fibonacci(numFibNumbersToSpeak)
        fibNumbersToSpeakString = u", ".join(str(fibNum) for fibNum in fibNumbersList)
        clientLib.nvdaController_speakText(fibNumbersToSpeakString)
        clientLib.nvdaController_brailleMessage(fibNumbersToSpeakString)
        print(fibNumbersToSpeakString)
    else:
        # If the input was not valid, speak, print and send the invalid-input message in braille
        invalidInputMessage = u"Input " + str(numFibNumbersToSpeak) + " is not greater than " + str(inputMustBeGreaterThan) + " and less than " + str(inputMustBeLessThan)
        clientLib.nvdaController_speakText(invalidInputMessage)
        clientLib.nvdaController_brailleMessage(invalidInputMessage)
        print(invalidInputMessage)
