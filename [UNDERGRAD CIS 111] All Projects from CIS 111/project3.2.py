income = float(input("Enter your total gross income: $"))
status = str(input("Enter (s)ingle or (m)arried: "))
if income < 0 : 
        print("error! Invalid input")
if status != "M" or "S":
   print("Error")
if status == "s" or "S":
    print("Filing status options:\n\t1. Single\n\t2. Head of Household\n\t3. Qualifying Widow")
    filing = int(input("Enter filing status: "))
    if filing == 1: 
            if income >=  0 and income <= 9875: 
                   fed = .1
                   state = income*.031
                   s1 = income - ((income*fed)+state)
            if income >= 9876 and income <= 40125: 
                   fed = .12 
                   if income >=9876 and income <= 14999:
                       state = income*.31
                       s2 = income - ((income*fed)+state)
                   if income >= 15000 and income <= 30000: 
                          state = 465 + (.0525*(income - 15000))
                          s2 = income - ((income*fed)+state)
                   else:
                          state = 1252.50 + (.0525*(income - 30000))
                          s3 = income - ((income*fed)+state)
            if income >= 40126 and income <= 85525: 
                   fed = .22
                   state = 1252.50 + (.0525*(income - 30000))
                   s4 = income - ((income*fed)+state)
            if income >= 85526 and income <= 163330: 
                   fed = .24 
                   state = 1252.50 + (.0525*(income - 30000))
                   s5 = income - ((income*fed)+state)
            if income >= 163301 and 207350: 
                   fed = .32 
                   state = 1252.50 + (.0525*(income - 30000))
                   s6 = income - ((income*fed)+state)       
            if income >= 207351 and income <= 518400:
                   fed = .35
                   state = 1252.50 + (.0525*(income - 30000))
                   s7 = income - ((income*fed)+state)
            if income > 518401: 
                   fed = .37
                   state = 1252.50 + (.0525*(income - 30000))
                   s8 = income - ((income*fed)+state)
    elif filing == 2: 
            if income >=  0 and income <= 14100: 
                   fed = .1
                   state = income*.031
                   hh1 = income - ((income*fed)+state)
            if income >= 14100 and income <= 53700: 
                   fed = .12
                   if income >= 14100 and income <= 14999: 
                       state = income *.031
                       hh2 = income - ((income*fed)+state) 
                   if income >= 15000 and income <= 30000: 
                          state = 465 + (.0525*(income - 15000))
                          hh3 = income - ((income*fed)+state)
                   else:
                          state = 1252.50 + (.0525*(income - 30000))
                          hh4 = income - ((income*fed)+state)
            if income >= 53701 and income <= 85500: 
                   fed = .22
                   state = 1252.50 + (.0525*(income - 30000))
                   hh5 = income - ((income*fed)+state)
            if income >= 85501 and income <= 163330: 
                   fed = .24 
                   state = 1252.50 + (.0525*(income - 30000))
                   hh6 = income - ((income*fed)+state)
            if income >= 163301 and income <= 207350: 
                   fed = .32 
                   state = 1252.50 + (.0525*(income - 30000))
                   hh7 = income - ((income*fed)+state)       
            if income >= 207351 and income <= 518400:
                   fed = .35
                   state = 1252.50 + (.0525*(income - 30000))
                   hh8 = income - ((income*fed)+state)
            if income > 518401: 
                   fed = .37
                   state = 1252.50 + (.0525*(income - 30000))
                   hh9 = income - ((income*fed)+state)
            elif filing == 3:
                if income >=  0 and income <= 19750: 
                   fed = .1
                   if income >0 and income <= 14999: 
                         state = income*.031
                         w2 = income - ((income*fed)+state)
                   if income >= 15000 and income <= 19750:
                       state = 465 + (income-(15000*.0525))
                       w1 = income - ((income * fed) + state) 
                if income >= 19751 and income <= 80250: 
                   fed = .12
                   if income >= 19750 and income < 30000: 
                       state = 465 + ((income * fed)+state)
                       w3 = income - ((income*fed)+state) 
                   else: 
                          state = 1242.50 + (.057*(income - 30000))
                          w4 = income - ((income*fed)+state)
                if income >= 80251 and income <= 171050: 
                   fed = .22
                   state = 1252.50 + (.0525*(income - 30000))
                   w5 = income - ((income*fed)+state)
                if income >= 171051 and income <= 326600: 
                   fed = .24 
                   state = 1252.50 + (.0525*(income - 30000))
                   w6 = income - ((income*fed)+state)
                if income >= 326601 and income <= 414700: 
                   fed = .32 
                   state = 1252.50 + (.0525*(income - 30000))
                   w7 = income - ((income*fed)+state)       
                if income >= 414701 and income <= 622050:
                   fed = .35
                   state = 1252.50 + (.0525*(income - 30000))
                   w8 = income - ((income*fed)+state)
                if income > 622051: 
                   fed = .37
                   state = 1252.50 + (.0525*(income - 30000))
                   w9 = income - ((income*fed)+state)
    else: 
            print("Error")
            if status == "m" or "M": 
               print("Filing status options:\n\t1. Head of Household\n\t2. Married Filing Jointly\n\t3. Married Filing Seperately")
               filing2 = int(input("Enter your filing status: "))
               if filing2 == 1: 
                   if income >=  0 and income <= 14100: 
                    fed = .1
                   state = income*.031
                   hh1 = income - ((income*fed)+state)
                   if income >= 14100 and income <= 53700: 
                    fed = .12
                   if income >= 14100 and income <= 14999: 
                       state = income *.031
                       hh2 = income - ((income*fed)+state) 
                   if income >= 15000 and income <= 30000: 
                          state = 465 + (.0525*(income - 15000))
                          hh3 = income - ((income*fed)+state)
                   else:
                          state = 1252.50 + (.0525*(income - 30000))
                          hh4 = income - ((income*fed)+state)
                   if income >= 53701 and income <= 85500: 
                    fed = .22
                   state = 1252.50 + (.0525*(income - 30000))
                   hh5 = income - ((income*fed)+state)
                   if income >= 85501 and income <= 163330: 
                    fed = .24 
                   state = 1252.50 + (.0525*(income - 30000))
                   hh6 = income - ((income*fed)+state)
                   if income >= 163301 and income <= 207350: 
                    fed = .32 
                   state = 1252.50 + (.0525*(income - 30000))
                   hh7 = income - ((income*fed)+state)       
                   if income >= 207351 and income <= 518400:
                    fed = .35
                   state = 1252.50 + (.0525*(income - 30000))
                   hh8 = income - ((income*fed)+state)
                   if income > 518401: 
                    fed = .37
                   state = 1252.50 + (.0525*(income - 30000))
                   hh9 = income - ((income*fed)+state)
               elif filing2 == 3:
                 if income >0 and income <= 14999: 
                         state = income*.031
                         w2 = income - ((income*fed)+state)
                         if income >= 15000 and income <= 19750:
                          state = 465 + (income-(15000*.0525))
                          w1 = income - ((income * fed) + state) 
                         if income >= 19751 and income <= 80250: 
                          fed = .12
                          if income >= 19750 and income < 30000: 
                           state = 465 + ((income * fed)+state)
                          w3 = income - ((income*fed)+state) 
                         else: 
                          state = 1242.50 + (.057*(income - 30000))
                          w4 = income - ((income*fed)+state)
                         if income >= 80251 and income <= 171050: 
                          fed = .22
                         state = 1252.50 + (.0525*(income - 30000))
                         w5 = income - ((income*fed)+state)
                         if income >= 171051 and income <= 326600: 
                          fed = .24 
                         state = 1252.50 + (.0525*(income - 30000))
                         w6 = income - ((income*fed)+state)
                         if income >= 326601 and income <= 414700: 
                          fed = .32 
                          state = 1252.50 + (.0525*(income - 30000))
                          w7 = income - ((income*fed)+state)       
                         if income >= 414701 and income <= 622050:
                          fed = .35
                         state = 1252.50 + (.0525*(income - 30000))
                         w8 = income - ((income*fed)+state)
                         if income > 622051: 
                          fed = .37
                         state = 1252.50 + (.0525*(income - 30000))
                         w9 = income - ((income*fed)+state)
               elif filing2 == 2:
                   if income >=  0 and income <= 9875: 
                    fed = .1
                   state = income*.031
                   s1 = income - ((income*fed)+state)
                   if income >= 9876 and income <= 40125: 
                    fed = .12 
                   if income >=9876 and income <= 14999:
                       state = income*.31
                       s2 = income - ((income*fed)+state)
                   if income >= 15000 and income <= 30000: 
                          state = 465 + (.0525*(income - 15000))
                          s2 = income - ((income*fed)+state)
                   else:
                          state = 1252.50 + (.0525*(income - 30000))
                          s3 = income - ((income*fed)+state)
                   if income >= 40126 and income <= 85525: 
                    fed = .22
                   state = 1252.50 + (.0525*(income - 30000))
                   s4 = income - ((income*fed)+state)
                   if income >= 85526 and income <= 163330: 
                    fed = .24 
                   state = 1252.50 + (.0525*(income - 30000))
                   s5 = income - ((income*fed)+state)
                   if income >= 163301 and income <= 207350: 
                    fed = .32 
                   state = 1252.50 + (.0525*(income - 30000))
                   s6 = income - ((income*fed)+state)       
                   if income >= 207351 and income <= 311025:
                    fed = .35
                   state = 1252.50 + (.0525*(income - 30000))
                   ss1 = income - ((income*fed)+state)
                   if income > 311026: 
                    fed = .37
                   state = 1252.50 + (.0525*(income - 30000))
                   ss2 = income - ((income*fed)+state)                      


        
        
        


