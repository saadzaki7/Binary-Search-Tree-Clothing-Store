#Name: Saad Zaki
#Date: June 18, 2021
#Description: A program designed to simulate the experience of shopping for 
#             clothes at a clothing store. Rather than displaying all the 
#             items for sale, the program curates an item specifically for the user
#             from the stores inventory using a binary search esque algorithm.
#             The program has a complete checkout sequence with an included receipt.  

#Importing libraries and initializing time.sleep's constant variables
import input_utilities
import time
vshort = 0.5
short = 0.75
long = 3.5

#The class that represents the store's shirts category
class shirts():
    #Adding attributes to the shirts
    def __init__(self, sex, size, price, name):
        self.sex = sex
        self.size = size
        self.price = price
        self.name = name
    #Getter method
    def getter(self, attrib):
        if attrib =="sex":
            return self.sex
        elif attrib == "name":
            return self.name
        elif attrib == "size":
            return self.size
        elif attrib == "price":
            return self.price
    #Setter method
    def setter(self, attrib, change):
        if attrib =="sex":
            self.sex = change
        elif attrib == "name":
            self.name = change
        elif attrib == "size":
            self.size = change
        elif attrib == "price":
            self.price = change

#The class that represents the store's hoodies category
#Inherits from the shirts class to reuse innit, getter, and setter methods
class hoodies(shirts):
    #Adding attributes to the hoodies
    def __init__(self, sex, size, price, name):
        #uses super() to reuse to innit
        super().__init__(sex, size, price, name)
    #Getter method
    def getter(self, attrib):
        #Also uses super()
        return super().getter(attrib)
    #Setter method
    def setter(self, attrib, change):
        super().setter(attrib, change)

#The class that represents the store's jeans category
#Inherits from the shirts class to reuse innit, getter, and setter methods
class jeans(shirts):
    #Adding attributes to the hoodies
    def __init__(self, sex, size, price,  name):
        super().__init__(sex, size, price,  name)
    #Getter method
    def getter(self, attrib):
        return super().getter(attrib)
    #Setter method
    def setter(self, attrib, change):
        super().setter(attrib, change)

#The class that represents the store's sweatpants category
#Inherits from the shirts class to reuse innit, getter, and setter methods
class sweats(shirts):
    #Adding attributes to the hoodies
    def __init__(self, sex, size, price,  name):
        super().__init__(sex, size, price,  name)
    #Getter method
    def getter(self, attrib):
        return super().getter(attrib)
    def setter(self, attrib, change):
        super().setter(attrib, change)

#The class that represents the store's running shoes category
#Inherits from the shirts class to reuse innit, getter, and setter methods
class runners(shirts):
    #Adding attributes to the hoodies
    def __init__(self, sex, size, price,  name):
        super().__init__(sex, size, price,  name)
    #Getter method
    def getter(self, attrib):
        return super().getter(attrib)
    #Setter method
    def setter(self, attrib, change):
        super().setter(attrib, change)

#The class that represents the store's winter boots category
#Inherits from the shirts class to reuse innit, getter, and setter methods
class boots(shirts):
    #Adding attributes to the hoodies
    def __init__(self, sex, size, price,  name):
        super().__init__(sex, size, price,  name)
    #Getter method
    def getter(self, attrib):
        return super().getter(attrib)
    #Setter method
    def setter(self, attrib, change):
        super().setter(attrib, change)

#Class for the ordering/purchasing where the program curates an item for the user
#Inherits from all categories to leverage their getter and setter methods
class order(hoodies, jeans, sweats, runners, boots):
    global rec_names
    global rec_prices
    global buying
    #List that stores the names of all items in the cart
    rec_names=[]
    #List that stores the prices of all items in the cart
    rec_prices=[]
    #Condition of purchasing loop that continues to prompt user to but
    #until they decide to exit
    buying=True

    #Static method for the main menu text
    @staticmethod
    def menu_text():
        #Visually appealing ASCII for store sign
        print('''
                        *   ____     _   _    ___       _    __ _ _   _                *
                        *  |_  /__ _| |_(_)  / _ \ _  _| |_ / _(_) |_| |_ ___ _ _ ___  *
                        *   / // _` | / / | | (_) | || |  _|  _| |  _|  _/ -_) '_(_-<  *
                        *  /___\__,_|_\_\_|  \___/ \_,_|\__|_| |_|\__|\__\___|_| /__/  *
                        *                                                              *''')
    #Decorator method to create an outline around the store sign
    def decorator(function):
        def outline():
            print("      "*4,"**"*31, end="")
            function()
            print("      "*4,"**"*31)
            print('''
                                            
  ______     _    _    _____                 _                                             
 |___  /    | |  (_)  / ____|               ( )                                            
    / / __ _| | ___  | |     ___  _ __ _ __ |/ ___                                         
   / / / _` | |/ / | | |    / _ \| '__| '_ \  / __|                                        
  / /_| (_| |   <| | | |___| (_) | |  | |_) | \__ \                                        
 /_____\__,_|_|\_\_|  \_____\___/|_|  | .__/  |___/               _     _              _   
  / ____| |                     (_)   | |           /\           (_)   | |            | |  
 | (___ | |__   ___  _ __  _ __  _ _ _|_| __ _     /  \   ___ ___ _ ___| |_ __ _ _ __ | |_ 
  \___ \| '_ \ / _ \| '_ \| '_ \| | '_ \ / _` |   / /\ \ / __/ __| / __| __/ _` | '_ \| __|
  ____) | | | | (_) | |_) | |_) | | | | | (_| |  / ____ \\__ \__ \ \__ \ || (_| | | | | |_ 
 |_____/|_| |_|\___/| .__/| .__/|_|_| |_|\__, | /_/    \_\___/___/_|___/\__\__,_|_| |_|\__|
                    | |   | |             __/ |                                            
                    |_|   |_|            |___/                                              ''')
            return
        outline()
    
    #class method because this method deals with all the objects instead of just 1
    @classmethod
    def ordering(cls):    
        #Initailizing variables
        global rec_names
        global rec_prices
        global buying
        

        #The binary search esque algorithm that curates a suggestions for the 
        #user to purchase. This algorithm's advanatage is how effiecent it
        #is in terms of processing power. Instead of checking every item in
        #the inventory each time a question is answered, the algorithm
        #divides the the number of potential options by a number after
        #each iteration, to eventually land on an item. Also creates a more
        #fun and intuitive way to shop rather than being shown 36 items at once.
        def cat_size_ask(cat):
            global buying
            #mens shirts are items 1-3
            if cat=="Mshirts":
                obj1=item1
                obj2=item2
                obj3=item3
            #mens hoodies are items #4-6 
            elif cat=="Mhoodies":
                obj1=item4
                obj2=item5
                obj3=item6
            #mens jeans are items #7-9
            elif cat=="Mjeans":
                obj1=item7
                obj2=item8
                obj3=item9
            #mens sweatpants are items #10-12
            elif cat=="Msweats":
                obj1=item10
                obj2=item11
                obj3=item12
            #mens runnning shoes are items #13-15
            elif cat=="Mshoes":
                obj1=item13
                obj2=item14
                obj3=item15
            #mens winter boots are items #16-18
            elif cat=="Mboots":
                obj1=item16
                obj2=item17
                obj3=item18
            #womens shirts are items #19-21
            elif cat=="Fshirts":
                obj1=item19
                obj2=item20
                obj3=item21
            #women's hoodies are items #22-24
            elif cat=="Fhoodies":
                obj1=item22
                obj2=item23
                obj3=item24
            #women's jeans are items #25-27
            elif cat=="Fjeans":
                obj1=item25
                obj2=item26
                obj3=item27
            #women's sweatpants are items #28-30
            elif cat=="Fsweats":
                obj1=item28
                obj2=item29
                obj3=item30
            #women's running shoes are items #31-33
            elif cat=="Fshoes":
                obj1=item31
                obj2=item32
                obj3=item33
            #women's winter boots are items #34-36
            elif cat=="Fboots":
                obj1=item34
                obj2=item35
                obj3=item36
            #Use getters to find out the 3 sizes for the specific category
            size_one = obj1.getter('size')
            size_two = obj2.getter('size')
            size_three = obj3.getter('size')
            time.sleep(short)
            #visually appealing Ascii title
            size_title = '''

   _____ _            _____      _           _   _             
  / ____(_)          / ____|    | |         | | (_)            
 | (___  _ _______  | (___   ___| | ___  ___| |_ _  ___  _ __  
  \___ \| |_  / _ \  \___ \ / _ \ |/ _ \/ __| __| |/ _ \| '_ \ 
  ____) | |/ /  __/  ____) |  __/ |  __/ (__| |_| | (_) | | | |
 |_____/|_/___\___| |_____/ \___|_|\___|\___|\__|_|\___/|_| |_|
                                                               
                                                               
            '''
            print(size_title)
            time.sleep(vshort)
            print(" "*11,"1.",size_one,"\n")
            time.sleep(vshort)
            print(" "*11,"2.",size_two,"\n")
            time.sleep(vshort)
            print(" "*11,"3.",size_three,"\n")
            time.sleep(vshort)
            print(" "*11,"4. None of the above\n")
            time.sleep(short)
            #Uses input utilities to have the user pick a size or exit
            size = input_utilities.get_option(4,"\nSize (1-4):")
            #Size one represents object 1 from the respective category
            if size == 1:
                #Using getters to find the product's price and name
                price= obj1.getter('price')
                name= obj1.getter('name')
                print("Searching our inventory for the most suitable product for you"\
                    +"",end = "")
                #Loading animation to build up anticipation and make the program 
                #more enjoyable
                for dot in range (6):
                    #Adds 1 dot each time it loops.
                    print(".",end = "")
                    time.sleep(vshort)
                print("\nProduct Found!")
                time.sleep(vshort)
                print(name," $", price,"." ,sep="")
                #Vusually appealing Ascii Art of a cart
                print('''
  _                
   \________
    \######/       
     |####/
     |____.
   __o____o_
                    ''')
                print("Do you want to add this product to your cart? (1/2)")
                #Uses input utilities to have the user confirm adding
                #the item to their cart
                print(" "*10,"\n1. Yes"," "*10, "\n\n2. No\n")
                confirm_purchase = input_utilities.get_option(2,"(1/2):")
                #If the user confirms their purchase the item's details are found
                if confirm_purchase == 1:
                    rec_names.append(name)
                    rec_prices.append(price)
                    #Ensures the grammar is correct when informing user that 
                    #the item has been added to their cart
                    time.sleep(short)
                    if (cat=="Mshirts" or cat == "Mhoodies" or cat == "Fshirts" or
                     cat== "Fhoodies"):
                        print(name,"has been added to your cart. \n\nWould you like to purchase anything else today?")
                    else:
                        print(name,"have been added to your cart. \n\nWould you like to purchase anything else today?")
                   
                    print(" "*10,"\n1. Yes"," "*10, "\n\n2. No\n")
                    #Uses input utilities to have user confirm purchase
                    restart= input_utilities.get_option(2, "(1/2):")
                    #If the user decides not to purchase anything else, the buying
                    #while loop is exited.
                    if restart==2:
                        buying=False
                    #Positive reinforcement for buying more and making the 
                    #business more profitable
                    else:
                        print('''
╱╱┏╮
╱╱┃┃
▉━╯┗━╮
▉┈┈┈┈┃
▉╮┈┈┈┃
╱╰━━━╯
''')
                
                #If the user decides to not purchase the suggested item,
                # the program ask if the user wants to purchase anything else 
                else:
                    print("\nNo worries, we have a wide selection of apparel."\
                        +" Anything you'd like to purchase?")
                    #Input Utilities to take input  
                    restart= input_utilities.get_option(2, " "*10,"\n1. Yes"\
                    +""," "*10, "\n\n2. No\n",sep="")
                    #If the user decides not to purchase anything else, the buying
                    #while loop is exited.
                    if restart==2:
                        buying=False
            

            #Size two represents object 2 from the respective category
            elif size== 2:
                #Using getters to find the product's price and name
                price= obj2.getter('price')
                name= obj2.getter('name')
                print("Searching our inventory for the most suitable product for you"\
                    +"",end = "")
                #Loading animation to build up anticipation and make the program 
                #more enjoyable
                for dot in range (6):
                    #Adds 1 dot each time it loops.
                    print(".",end = "")
                    time.sleep(vshort)
                print("\nProduct Found!")
                time.sleep(vshort)
                print(name," $", price,"." ,sep="")
                #Vusually appealing Ascii Art of a cart
                print('''
  _                
   \________
    \######/       
     |####/
     |____.
   __o____o_
                    ''')
                print("Do you want to add this product to your cart? (1/2)")
                #Uses input utilities to have the user confirm adding
                #the item to their cart
                print(" "*10,"\n1. Yes"," "*10, "\n\n2. No\n")
                confirm_purchase = input_utilities.get_option(2,"(1/2):")
                #If the user confirms their purchase the item's details are found
                if confirm_purchase == 1:
                    rec_names.append(name)
                    rec_prices.append(price)
                    #Ensures the grammar is correct when informing user that 
                    #the item has been added to their cart
                    time.sleep(short)
                    if (cat=="Mshirts" or cat == "Mhoodies" or cat == "Fshirts" or
                     "Fhoodies"):
                        print(name,"has been added to your cart. \n\nWould you like to purchase anything else today?")
                    else:
                        print(name,"have been added to your cart. \n\nWould you like to purchase anything else today?")
                   
                    print(" "*10,"\n1. Yes"," "*10, "\n\n2. No\n")
                    #Uses input utilities to have user confirm purchase
                    restart= input_utilities.get_option(2, "(1/2):")
                    #If the user decides not to purchase anything else, the buying
                    #while loop is exited.
                    if restart==2:
                        buying=False
                    #Positive reinforcement for buying more and making the 
                    #business more profitable
                    else:
                        print('''
╱╱┏╮
╱╱┃┃
▉━╯┗━╮
▉┈┈┈┈┃
▉╮┈┈┈┃
╱╰━━━╯
''')
                
                #If the user decides to not purchase the suggested item,
                # the program ask if the user wants to purchase anything else 
                else:
                    print("\nNo worries, we have a wide selection of apparel."\
                        +" Anything you'd like to purchase?")
                    #Input Utilities to take input  
                    print(" "*10,"\n1. Yes"," "*10, "\n\n2. No\n")
                    #Uses input utilities to have user confirm purchase
                    restart= input_utilities.get_option(2, "(1/2):")
                    #If the user decides not to purchase anything else, the buying
                    #while loop is exited.
                    if restart==2:
                        buying=False


            elif size== 3:
                #Using getters to find the product's price and name
                price= obj3.getter('price')
                name= obj3.getter('name')
                print("Searching our inventory for the most suitable product for you"\
                    +"",end = "")
                #Loading animation to build up anticipation and make the program 
                #more enjoyable
                for dot in range (6):
                    #Adds 1 dot each time it loops.
                    print(".",end = "")
                    time.sleep(vshort)
                print("\nProduct Found!")
                time.sleep(vshort)
                print(name," $", price,"." ,sep="")
                #Vusually appealing Ascii Art of a cart
                print('''
  _                
   \________
    \######/       
     |####/
     |____.
   __o____o_
                    ''')
                print("Do you want to add this product to your cart? (1/2)")
                #Uses input utilities to have the user confirm adding
                #the item to their cart
                print(" "*10,"\n1. Yes"," "*10, "\n\n2. No\n")
                confirm_purchase = input_utilities.get_option(2,"(1/2):")
                #If the user confirms their purchase the item's details are found
                if confirm_purchase == 1:
                    rec_names.append(name)
                    rec_prices.append(price)
                    #Ensures the grammar is correct when informing user that 
                    #the item has been added to their cart
                    time.sleep(short)
                    if (cat=="Mshirts" or cat == "Mhoodies" or cat == "Fshirts" or
                     "Fhoodies"):
                        print(name,"has been added to your cart. \n\nWould you like to purchase anything else today?")
                    else:
                        print(name,"have been added to your cart. \n\nWould you like to purchase anything else today?")
                   
                    print(" "*10,"\n1. Yes"," "*10, "\n\n2. No\n")
                    #Uses input utilities to have user confirm purchase
                    restart= input_utilities.get_option(2, "(1/2):")
                    #If the user decides not to purchase anything else, the buying
                    #while loop is exited.
                    if restart==2:
                        buying=False
                    #Positive reinforcement for buying more and making the 
                    #business more profitable
                    else:
                        print('''
╱╱┏╮
╱╱┃┃
▉━╯┗━╮
▉┈┈┈┈┃
▉╮┈┈┈┃
╱╰━━━╯
''')
                
                #If the user decides to not purchase the suggested item,
                # the program ask if the user wants to purchase anything else 
                else:
                    print("\nNo worries, we have a wide selection of apparel."\
                        +" Anything you'd like to purchase?")
                    #Input Utilities to take input  
                    print(" "*10,"\n1. Yes"," "*10, "\n\n2. No\n")
                    #Uses input utilities to have user confirm purchase
                    restart= input_utilities.get_option(2, "(1/2):")
                    #If the user decides not to purchase anything else, the buying
                    #while loop is exited.
                    if restart==2:
                        buying=False
            else:
                print("\nNo worries, we have a wide selection of apparel."\
                        +" Anything you'd like to purchase?")
                #Input Utilities to take input  
                print(" "*10,"\n1. Yes"," "*10, "\n\n2. No\n")
                #Uses input utilities to have user confirm purchase
                restart= input_utilities.get_option(2, "(1/2):")
                #If the user decides not to purchase anything else, the buying
                #while loop is exited.
                if restart==2:
                    buying=False

        #Buying while loop that has the user continue to purchase until they decide to leave
        while buying:
            #Display menu and instructions
            #Uses decorator
            order.decorator(order.menu_text) 
            time.sleep(short)
            print("\nOur patented shopping assistant will help you find the"\
            +" apparel that fits your preferences and needs perfectly!")
            time.sleep(short)
            print("\nSimply answer a few questions and our algorithm will do the rest.\n")
            time.sleep(short)

            validAns=False
            while not validAns:

                print('''
   _____                _              _____      _           _   _             
  / ____|              | |            / ____|    | |         | | (_)            
 | |  __  ___ _ __   __| | ___ _ __  | (___   ___| | ___  ___| |_ _  ___  _ __  
 | | |_ |/ _ \ '_ \ / _` |/ _ \ '__|  \___ \ / _ \ |/ _ \/ __| __| |/ _ \| '_ \ 
 | |__| |  __/ | | | (_| |  __/ |     ____) |  __/ |  __/ (__| |_| | (_) | | | |
  \_____|\___|_| |_|\__,_|\___|_|    |_____/ \___|_|\___|\___|\__|_|\___/|_| |_|
                                                                                
                                                                                
     
                    ''')
                #Ask if Male (item#1-18) or Female (item#19-36)
                try:
                    print(" "*11,"1. Men's Clothing","\n\n"," "*10,"2. Women's"\
                        +" Clothing")
                    time.sleep(short)
                    sex = input_utilities.get_option(2,"Gender (1/2):")
                    if sex == 1 or sex ==2:
                        validAns = True
                    else:
                        print("Sorry,could you repeat that? (1/2)")
                except:
                    print("Sorry,could you repeat that? (1/2)")
            #Men's products curation
            if sex == 1:
                #Ask for desired product category
                #Display Product category menu
                time.sleep(short)
                print('''
_____               _            _      _____      _                               
|  __ \             | |          | |    / ____|    | |                              
| |__) | __ ___   __| |_   _  ___| |_  | |     __ _| |_ ___  __ _  ___  _ __ _   _  
|  ___/ '__/ _ \ / _` | | | |/ __| __| | |    / _` | __/ _ \/ _` |/ _ \| '__| | | | 
| |   | | | (_) | (_| | |_| | (__| |_  | |___| (_| | ||  __/ (_| | (_) | |  | |_| | 
|_|   |_|  \___/ \__,_|\__,_|\___|\__|  \_____\__,_|\__\___|\__, |\___/|_|   \__, | 
                                                             __/ |            __/ | 
                                                            |___/            |___/  
                    ''')
                time.sleep(vshort)
                print(" "*10, "1. Shirts \n")
                time.sleep(vshort)
                print(" "*10, "2. Hoodies \n")
                time.sleep(vshort)
                print(" "*10, "3. Jeans \n")
                time.sleep(vshort)
                print(" "*10, "4. Sweatpants \n")
                time.sleep(vshort)
                print(" "*10, "5. Running Shoes \n")
                time.sleep(vshort)
                print(" "*10, "6. Winter Boots \n")
                time.sleep(vshort)
                print(" "*10, "7. None \n")
                time.sleep(short)
                
                #Take input for to determine the category
                cat = input_utilities.get_option(7,"Category (1-7):")
                if cat != 7:
                    #items #1-3 for mens shirts
                    if cat == 1:
                        cat_size_ask("Mshirts")
                    #mens hoodies #4-6            
                    elif cat == 2:
                        cat_size_ask("Mhoodies")
                    #mens jeans #7-9
                    elif cat == 3:
                        cat_size_ask("Mjeans")
                    #mens sweatpants #10-12
                    elif cat == 4:
                        cat_size_ask("Msweats")
                    #mens running shoes #13-15            
                    elif cat == 5:
                        cat_size_ask("Mshoes")
                    #mens Winter boots #16-18
                    elif cat == 6:
                        cat_size_ask("Mboots")
                #Leave option if the customer is not interested in the
                #categories.
                else:
                    time.sleep(long)
                    print("\nNo worries, we offer a wide selection of apparel."\
                    +" Is there anything you'd like to purchase?")
                    #Input utilities to take input  
                    print(" "*10,"\n1. Yes"," "*10, "\n\n2. No\n")
                    #Uses input utilities to have user confirm purchase
                    restart= input_utilities.get_option(2, "(1/2):")
                    #If the user decides not to purchase anything else, the buying
                    #while loop is exited.
                    if restart==2:
                        buying=False
            #Women's product curation            
            else:
                #Ask for desired product category
                #Display Product category menu
                time.sleep(short)
                print('''
_____               _            _      _____      _                               
|  __ \             | |          | |    / ____|    | |                              
| |__) | __ ___   __| |_   _  ___| |_  | |     __ _| |_ ___  __ _  ___  _ __ _   _  
|  ___/ '__/ _ \ / _` | | | |/ __| __| | |    / _` | __/ _ \/ _` |/ _ \| '__| | | | 
| |   | | | (_) | (_| | |_| | (__| |_  | |___| (_| | ||  __/ (_| | (_) | |  | |_| | 
|_|   |_|  \___/ \__,_|\__,_|\___|\__|  \_____\__,_|\__\___|\__, |\___/|_|   \__, | 
                                                          __/ |            __/ | 
                                                         |___/            |___/  
                    ''')
                time.sleep(vshort)
                print(" "*10, "1. Shirts \n")
                time.sleep(vshort)
                print(" "*10, "2. Hoodies \n")
                time.sleep(vshort)
                print(" "*10, "3. Jeans \n")
                time.sleep(vshort)
                print(" "*10, "4. Sweatpants \n")
                time.sleep(vshort)
                print(" "*10, "5. Running Shoes \n")
                time.sleep(vshort)
                print(" "*10, "6. Winter Boots \n")
                time.sleep(vshort)
                print(" "*10, "7. None \n")
                time.sleep(short)
                
                #Take input for to determine the category
                cat = input_utilities.get_option(7,"Category (1-7):")
                if cat != 7:
                    #items #1-3 for women's shirts
                    if cat == 1:
                        cat_size_ask("Fshirts")
                    #women's hoodies #4-6            
                    elif cat == 2:
                        cat_size_ask("Fhoodies")
                    #women's jeans #7-9
                    elif cat == 3:
                        cat_size_ask("Fjeans")
                    #women's sweatpants #10-12
                    elif cat == 4:
                        cat_size_ask("Fsweats")
                    #women's running shoes #13-15            
                    elif cat == 5:
                        cat_size_ask("Fshoes")
                    #women's Winter boots #16-18
                    elif cat == 6:
                        cat_size_ask("Fboots")
                #Leave option if the customer is not interested in the
                #categories.
                else:
                    time.sleep(long)
                    print("\nNo worries, we offer a wide selection of apparel."\
                    +" Is there anything you'd like to purchase?")
                    #Input utilities to take input  
                    print(" "*10,"\n1. Yes"," "*10, "\n\n2. No\n")
                    #Uses input utilities to have user confirm purchase
                    restart= input_utilities.get_option(2, "(1/2):")
                    #If the user decides not to purchase anything else, the buying
                    #while loop is exited.
                    if restart==2:
                        buying=False

#Cash register class for almost all transactional information
class cash_register():
    def __init__(self, amount):
    #weakly private most transactional info is somewhat private
        self._amount = amount
    #@property to find the amount of subtotal taken up by taxes
    @property
    def tax_amount(self):
        cash=self._amount
        return(round(cash * 0.13,2)) 
    #Method that adds all elements of a pricing list
    def order_total(price_list):
        total=0
        for x in price_list:
            total+=x
        return total
    #Magic method common operator multiply
    def __mul__(self, other):
        return self._amount * other._amount
    #Magic method common operator add
    def __add__(self, other):
        return self._amount + other._amount
    #Magic method common operator subtract
    def __sub__(self, other):
        return self._amount - other._amount
    #Magic method comparison operator greater than equal
    def __ge__(self, other):
        if self._amount >= other._amount:
            return True
        else:
            return False
    #prints receipt
    #Takes all necessary information as parameters
    def receipt(name_list, price_list, donation, subtotal, order_total, change, paid):
        global rev
        print("       Zaki Outfitters")
        for x in range (len(name_list)):
            print(name_list[x], " "*5,"$",price_list[x],sep="")
        print("Total:", " "*5,"$",order_total._amount)
        print("Tax:", " "*5,"$", rev.tax_amount)
        print("Charity donation:", " "*4, "$", donation._amount, sep="")
        print("Subtotal:", " "*4, "$", subtotal._amount, sep="")
        print("Payment:", " "*4, "$", paid._amount, sep="")
        print("Change:", " "*4, "$", round(change,2), sep="")
    def take_payment(subtotal):
        print("The subtotal of your order is $", subtotal._amount,".",sep="")
        validPayment=False
        while not validPayment:
            payment= input_utilities.get_float("Payment: $")
            payment= payment_cls(payment)
            payment= cash_register(payment._payment_cls__amount)
            if payment >= subtotal:
                change= payment-subtotal
                print("Your change is: $",round(change,2),".", sep="")
                print("Here's your receipt.")
                validPayment=True
            else:
                print("Sorry, that wasn't quite enough. Please try again.")
        return payment, change
class payment_cls():
    def __init__(self, amount):
    #Strongly private
        self.__amount = amount



       

        

#Male shirt inventory
item1 = shirts("male", "Small", 20,  "Red Men's Shirt (Small)")
item2 = shirts("male", "Medium", 20,  "Blue Men's Shirt (Medium)")
item3 = shirts("male", "Large", 20,  "Red Men's Shirt (Large)")
#Male hoodie inventory
item4 = hoodies("male", "Small", 25,  "Men's Beige Hoodie (Small)")
item5 = hoodies("male", "Medium", 25,  "Men's Black Hoodie (Medium)")
item6 = hoodies("male", "Large", 25,  "Men's Beige Hoodie (Large)")
#Male jeans inventory
item7 = jeans("male", "29-30", 50,  "Men's Dark Washed Jeans (29-30)")
item8 = jeans("male", "30-32", 50,  "Men's Dark Washed Jeans (30-32)")
item9 = jeans("male", "34-34", 50,  "Men's Light Washed Jeans (34-34)")
#Male sweatpants inventory
item10 = sweats("male", "Small", 15,  "Men's Black Sweatpants (Small)")
item11 = sweats("male", "Medium", 15,  "Men's Grey Sweatpants (Medium)")
item12 = sweats("male", "Large", 15,  "Men's Grey Sweatpants (Large)")
#Male running shoes inventory
item13 = runners("male", "8", 90,  "Men's White Running Shoes (8)")
item14 = runners("male", "10", 90,  "Men's White Running Shoes (10)")
item15 = runners("male", "12", 90,  "Men's Blue Running Shoes (12)")
#Male winter boots inventory
item16 = boots("male", "8", 120, "Men's Brown Winter Boots (8)")
item17 = boots("male", "10", 120,  "Men's Brown Winter Boots (10)")
item18 = boots("male", "12", 120,  "Men's Black Winter Boots (12)")

#Female shirts inventory
item19 = shirts("female", "Small", 20,  "Red Women's Shirt (Small)")
item20 = shirts("female", "Medium", 20,  "Red Women's Shirt (Medium)")
item21 = shirts("female", "Large", 20,  "Blue Women's Shirt (Large)")
#Female hoodies inventory
item22 = hoodies("female", "Small", 25,  "Women's Black Hoodie (Small)")
item23 = hoodies("female", "Medium", 25,  "Women's Black Hoodie (Medium)")
item24 = hoodies("female", "Large", 25,  "Women's Grey Hoodie (Large)")
#Female jeans inventory
item25 = jeans("female", "29-30", 50, "Women's Light Washed Jeans (29-30)")
item26 = jeans("female", "30-32", 50, "Women's Light Washed Jeans (30-32)")
item27 = jeans("female", "32-32", 50, "Women's Dark Washed Jeans (32-32)")
#Female sweatpants inventory
item28 = sweats("female", "Small", 15,  "Women's Black Sweatpants (Small)")
item29 = sweats("female", "Medium", 15,  "Women's Black Sweatpants (Medium)")
item30 = sweats("female", "Large", 15,  "Women's Grey Sweatpants (Large)")
#Female running shoes inventory
item31 = runners("female", "6", 90,  "Women's White Running Shoes (6)")
item32 = runners("female", "8", 90,  "Women's White Running Shoes (8)")
item33 = runners("female", "10", 90,  "Women's Blue Running Shoes (10)")
#Female winter boots inventory
item34 = boots("female", "6", 120,  "Women's Brown Winter Boots (6)")
item35 = boots("female", "8", 120,  "Women's Brown Winter Boots (8)")
item36 = boots("female", "10", 120,  "Women's Black Winter Boots (10)")



def main():
    #Takes order from user
    global rev
    order.ordering()
    #References receipt price list to find the revenue generated
    rev= cash_register.order_total(rec_prices)
    #Attributes the revenue to the object revenue
    rev= cash_register(rev)
    #Sets tax rate on cash register. This is a variable tax rate
    tax = cash_register(1.13)
    #gross income generated
    gross= rev * tax
    #Round gross income to include cents
    gross=round(gross,2)
    #Gross becomes an instance of cash register with the attribute of gross income
    gross = cash_register (gross)
    #Asks user to donate to charity
    time.sleep(short)
    print('''
   _____ _               _               _      _____                  _            
  / ____| |             | |             | |    / ____|                | |           
 | |    | |__   ___  ___| | _____  _   _| |_  | |     ___  _   _ _ __ | |_ ___ _ __ 
 | |    | '_ \ / _ \/ __| |/ / _ \| | | | __| | |    / _ \| | | | '_ \| __/ _ \ '__|
 | |____| | | |  __/ (__|   < (_) | |_| | |_  | |___| (_) | |_| | | | | ||  __/ |   
  \_____|_| |_|\___|\___|_|\_\___/ \__,_|\__|  \_____\___/ \__,_|_| |_|\__\___|_|   
                                                                                    
                                                                                
        ''')
    time.sleep(long)
    print('''
  _____                    _   _               _           _____ _                _ _         
 |  __ \                  | | (_)             | |         / ____| |              (_) |        
 | |  | | ___  _ __   __ _| |_ _  ___  _ __   | |_ ___   | |    | |__   __ _ _ __ _| |_ _   _ 
 | |  | |/ _ \| '_ \ / _` | __| |/ _ \| '_ \  | __/ _ \  | |    | '_ \ / _` | '__| | __| | | |
 | |__| | (_) | | | | (_| | |_| | (_) | | | | | || (_) | | |____| | | | (_| | |  | | |_| |_| |
 |_____/ \___/|_| |_|\__,_|\__|_|\___/|_| |_|  \__\___/   \_____|_| |_|\__,_|_|  |_|\__|\__, |
                                                                                         __/ |
                                                                                        |___/  ''')
    #created new function call get_float in input utilities for this use case
    charity = input_utilities.get_float("Donation: $")
    #charity becomes an instance of cash register with the attribute of the amount
    #donated to charity 
    charity = cash_register(charity)
    #sub total
    subtotal = charity + gross
    subtotal = cash_register(subtotal)
    time.sleep(short)
    #Takes payment for order
    paid, change= cash_register.take_payment(subtotal)
    time.sleep(vshort)
    #displays receipt
    print("")
    cash_register.receipt(rec_names, rec_prices, charity, subtotal, rev, change, paid)
    print("\nThank you for shopping with Zaki Outfitters!")
    print ("\nHave a great day!")
main()