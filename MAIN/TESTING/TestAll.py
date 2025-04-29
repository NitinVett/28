from .CardTest import CardTest

if __name__ == "__main__":
    GREEN = '\033[32m'
    RESET = '\033[0m'
    RED = '\033[31m'
    testCard = CardTest()

    
    try:
        testCard.run()
        print(GREEN + "CARD TEST PASSED!" + RESET)
    except:
        print(RED + "CARD TEST FAILED!" + RESET)

    
