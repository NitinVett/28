from .CardTest import CardTest
from .CardManagerTest import CardManagerTest

if __name__ == "__main__":
    GREEN = '\033[32m'
    RESET = '\033[0m'
    RED = '\033[31m'
    testCard = CardTest()
    testCardManager = CardManagerTest()

    
    try:
        testCard.run()
        print(GREEN + "CARD TEST PASSED!" + RESET)
    except Exception as e:
        print(RED + "CARD TEST FAILED!" + RESET)
        print(e)

    try:
        testCardManager.run()
        print(GREEN + "CARD_MANAGER TEST PASSED!" + RESET)
    except Exception as e:
        print(RED + "CARD_MANAGER TEST FAILED!" + RESET)
        print(e)
    

    
