import random as rn
import time
while True :
    op = input("\ndo you continue? = enter is empty , Exit = exit,\n_ ").strip().lower()

    if op == "" :
        time.sleep(rn.randint(1,2))
        ran = rn.randint(1,6)
        if ran == 1 :
           ran1 = "\n-   ."
        elif ran == 2 :
            ran1 = "\n-   :"
        elif ran == 3 :
            ran1 = "\n-   :."
        elif ran == 4 :
            ran1 = "\n-   ::"
        elif ran == 5 :
            ran1 = "\n-   :.:"
        elif ran == 6 :
            ran1 = "\n-   :::"

        print (ran1)

        if ran == 6 :
            print ("\n******* pairs Six ********\n")
            for i in range(2) :
                time.sleep(rn.randint(1,2))
                ran = rn.randint(1,6)
                if ran == 1 :
                   ran1 = "\n-   ."
                elif ran == 2 :
                    ran1 = "\n-   :"
                elif ran == 3 :
                    ran1 = "\n-   :."
                elif ran == 4 :
                    ran1 = "\n-   ::"
                elif ran == 5 :
                    ran1 = "\n-   :.:"
                elif ran == 6 :
                    ran1 = "\n-   :::"

                print (ran1)

    elif op == "exit" :
        break
    else :
        print ("\nInvalid input\n")
        pass
