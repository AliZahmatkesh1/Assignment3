import random as rn
nn =0
while True :
    nn =0
    print ("easy range(1,50) ,normal range(1,200) ,hard range(1,500)")
    o = input("easy = 1 ,normal = 2 ,hard = 3 , Exit = exit\n_ ").strip().lower()
    
    if o == "1" or o == "easy" :
        add = rn.randint(1,50)
        a = 1
        while True :
            op = int(input("\nEnter a namber : "))

            if op < 1 or op > 50 :
                print ("\nInvalid input\n")
                pass
            elif op > add :
                print ("The desired number is smaller.")
                a = a + 1
            elif op < add :
                print ("The desired number is larger.")
                a = a + 1
            elif op == add :
                print ("\n\n     *****you win*****")
                print ("The desired number was (",add,").")
                print ("You tried (",a,") times.")
                while True :
                    ad = input("\n\ndo you continue? yes = y , no = n \n_ ").strip().lower()
                    if ad == "n" :
                        nn = 1
                        break
                    elif ad == "y" :
                        add = rn.randint(1,50)
                        a = 1
                        break
                    else :
                        print ("\nInvalid input\n")
                        pass
            if nn == 1 :
                break

    elif o == "2" or o == "normal" :
        add = rn.randint(1,200)
        a = 1
        while True :
            op = int(input("\nEnter a namber : "))

            if op < 1 or op > 200 :
                print ("\nInvalid input\n")
                pass
            elif op > add :
                print ("The desired number is smaller.")
                a = a + 1
            elif op < add :
                print ("The desired number is larger.")
                a = a + 1
            elif op == add :
                print ("\n\n     *****you win*****")
                print ("The desired number was (",add,").")
                print ("You tried (",a,") times.")
                while True :
                    ad = input("\n\ndo you continue? yes = y , no = n \n_ ").strip().lower()
                    if ad == "n" :
                        nn = 1
                        break
                    elif ad == "y" :
                        add = rn.randint(1,200)
                        a = 1
                        break
                    else :
                        print ("\nInvalid input\n")
                        pass
            if nn == 1 :
                break

    elif o == "3" or o == "hard" :
        add = rn.randint(1,500)
        a = 1
        while True :
            op = int(input("\nEnter a namber : "))

            
            if op < 1 or op > 500 :
                print ("\nInvalid input\n")
                pass
            elif op > add :
                print ("The desired number is smaller.")
                a = a + 1
            elif op < add :
                print ("The desired number is larger.")
                a = a + 1
            elif op == add :
                print ("\n\n     *****you win*****")
                print ("The desired number was (",add,").")
                print ("You tried (",a,") times.")
                while True :
                    ad = input("\n\ndo you continue? yes = y , no = n \n_ ").strip().lower()
                    if ad == "n" :
                        nn = 1
                        break
                    elif ad == "y" :
                        add = rn.randint(1,500)
                        a = 1
                        break
                    else :
                        print ("\nInvalid input\n")
                        pass
            if nn == 1 :
                break
    
    elif o == "exit" :
        break
    else :
        print ("\nInvalid input\n")
        pass
