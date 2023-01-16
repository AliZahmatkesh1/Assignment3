import random as rn
import time
aa = 0
while True :
    aa = 0
    a = input("\nExit = exit , tas = enter empty \n _ ").strip().lower()
    if a == "" :
        while True :
            if a == "" :
                tas_a = rn.randint(1,6)
                tas_a1 = rn.randint(1,6)
                print ("please wait ...\n")
                time.sleep(rn.randint(1,3))
                print ("your dice 1 :" , tas_a)
                print ("your dice 2 :" , tas_a1)
                if tas_a == 6 and tas_a1 == 6 :
                    print ("******* pairs Six ********")
                    print ("******** you won *********\n\n")
                    print ("\nContinue = y , Exit = n")
                    while True :
                        p = input("do you continue?\n_ ")
                        if p == "n" :
                            exit()
                        elif p == "y" :
                            aa = 1
                            break
                        else :
                            print ("\nInvalid input\n")
                            pass
                            
                if aa == 1 :
                    break
                elif tas_a == tas_a1 :
                    b = 2
                    c = 0
                    print ("\nYour dice are "+str(tas_a)+" and you have "+str(b)+" more dice.\n")
                    while c < b :
                        print ("\nyou have "+str(b)+" more dice.\n")
                        print ("please wait ...\n")
                        time.sleep(rn.randint(1,3))
                        tas_a = rn.randint(1,6)
                        tas_a1 = rn.randint(1,6)
                        print ("your dice 1:" , tas_a)
                        print ("your dice 2:" , tas_a1)
                        if tas_a == 6 and tas_a1 == 6 :
                            print ("******* pairs Six ********")
                            print ("******** you won *********\n\n")
                            print ("\nContinue = y , Exit = n")
                            while True :
                                p = input("do you continue?\n_ ")
                                if p == "n" :
                                    exit()
                                elif p == "y" :
                                    aa = 1
                                    break
                                else :
                                    print ("\nInvalid input\n")
                                    pass
                        if aa == 1 :
                            break
                                
                        if tas_a == tas_a1 :
                            print ("\nYour dice are "+str(tas_a)+" \n")
                            b = b + 2
                        else :
                            b = b - 1
                if aa == 0 :    
                    print ("\nIt's the computer's turn")
                    print ("please wait ...\n")
                    time.sleep(rn.randint(1,3))
                    tas_b = rn.randint(1,6)
                    tas_b1 = rn.randint(1,6)
                    print ("Computer dice 1 :" , tas_b)
                    print ("Computer dice 2 :" , tas_b1)
                    if tas_b == 6 and tas_b1 == 6 :
                        print ("\n\n  ******* pairs Six ********")
                        print ("******** computer won *********\n\n")
                        print ("\nContinue = y , Exit = n")
                        while True :
                            p = input("do you continue?\n_ ")
                            if p == "n" :
                                exit()
                            elif p == "y" :
                                aa = 1
                                break
                            else :
                                print ("\nInvalid input\n")
                                pass
                        if aa == 1 :
                            break
                    elif tas_b == tas_b1 :
                        b = 2
                        c = 0
                        print ("\ncomputer dice are "+str(tas_b)+" and computer have "+str(b)+" more dice.\n")
                        while c < b :
                            print ("\ncomputer have "+str(b)+" more dice.\n")
                            print ("please wait ...\n")
                            time.sleep(rn.randint(1,3))
                            tas_b = rn.randint(1,6)
                            tas_b1 = rn.randint(1,6)
                            print ("computer dice 1:" , tas_b)
                            print ("computer dice 2:" , tas_b1)
                            if tas_b == 6 and tas_b1 == 6 :
                                print ("\n\n  ******* pairs Six ********")
                                print ("******** computer won *********\n\n")
                                print ("\nContinue = y , Exit = n")
                                while True :
                                    p = input("do you continue?\n_ ")
                                    if p == "n" :
                                        exit()
                                    elif p == "y" :
                                        aa = 1
                                        break
                                    else :
                                        print ("\nInvalid input\n")
                                        pass
                            if aa == 1 :
                                break
                            if tas_b == tas_b1 :
                                print ("\ncomputer dice are "+str(tas_b)+" \n")
                                b = b + 2
                            else :
                                b = b - 1
                else : break
            a = input("\nExit = exit , tas = enter empty \n _ ").strip().lower()       
    
