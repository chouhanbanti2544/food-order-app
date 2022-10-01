#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class FoodApp:

#main code

    def __init__(self,name):
        
        self.foodapp_name=name
        self.food={}                        # self.food= {1 : {---self.item--}, 2 : {------}, 3 : {------}}
        self.foodid=len(self.food)+1 
        self.admin_details={}
        self.user_details={}
        self.ordered_item=[]
        


    # admin functions


    def admin_register(self, email, password):        
        self.email=email 
        self.password=password
        self.admin_details={'ADMIN ID': self.email, 'ADMIN PASSWORD':self.password}
        print('\n!! Account Created Successfully !!\n')
        
    

    def admin_login(self, email, password):
        if len(self.admin_details)!=0:
            if email== self.admin_details['ADMIN ID'] and password==self.admin_details['ADMIN PASSWORD']:
                print('\n!!Successfully Login !!\n')
                return True
            else:
                return False
        else:
                return False
        


    def add_food_item(self, name, quantity, price, discount, stock):
        
        self.item={'NAME':name,'QUANTITY':quantity,'PRICE':price,'DISCOUNT':discount,'STOCK':stock}
        self.foodid=len(self.food)+1
        self.food[self.foodid]=self.item
        print('\n!! Item Added Successfully !!\n')
        
        # self.food= {1 : {---self.item--}, 2 : {------}, 3 : {------}}
        
    
    def edit_food_item(self, foodid):
        try:
            if len(self.food)!=0:
        
                if foodid in self.food.keys():
                    print("1. Edit Name")
                    print('2. Edit Quantity')
                    print('3. Edit Price')
                    print('4. Edit Discount')
                    print('5. Edit Stock')

                    x= input('Option from below Above : ')

                    if x=='1':
                        new_name= input('Enter the new updated name : ')
                        self.food[foodid]['NAME'] = new_name     # {'NAME':name,'QUANTITY':quantity,'PRICE':price,'STOCK':stock}
                        print('\n!! Name updated Successfully !!') 

                    elif x=='2':
                        new_quant=input('Enter Updated Quantity like For eg, 100ml, 250gm, 4pieces etc : ')
                        self.food[foodid]['QUANTITY'] = new_quant
                        print('\n!! Qantity updated Successfully !!')  

                    elif x=='3':
                        new_price= int(input('Enter Updated Price in RS : '))
                        self.food[foodid]['PRICE'] = new_price
                        print('\n!! Price updated Successfully !!') 

                    elif x=='4':
                        new_dis = float(input('Enter Updated Discount in RS : '))
                        self.food[foodid]['DISCOUNT'] = new_dis
                        print('\n!! Discount updated Successfully !!')

                    elif x=='5':

                        new_stock= int(input('Enter Updated Stock in RS : '))
                        self.food[foodid]['STOCK'] = new_stock
                        print('\n!!Stock updated Successfully !!')

                    else:
                        print('Invalid Option - Please enter from above option')
            else:
                print('\nNO FOOD ITEMS AVAILABE NOW FOR EDIT')
            
            
        except Exception as e:
            print('!! ENTERED INVALID FOOD ITEM DETAILS !!')
                
       

    def view_food_item(self):   # self.food= {1 : {---self.item--}, 2 : {------}, 3 : {------}}
        if len(self.food)!=0:
            for i in self.food:
                print('Food ID :',i)
                for j in self.food[i]:
                    print(j,":", self.food[i][j])
        else:
            print('\nNO FOOD ITEMS AVAILABE NOW FOR VIEW')
            
            
    def delete_food_item(self, foodid):
        if len(self.food)!=0:
            if foodid in self.food.keys():
                del self.food[foodid]
                print('\n!!Deleted Successfully !!\n')
                print('UPDATED FOOD ITEM :', self.food)
            else:
                print('Invalid Food ID')
        else:
            print('\nNO FOOD ITEMS AVAILABE NOW FOR DELETE')

    

    # user functions


    def user_register(self,fullname,phonenumber,Email,address,password): # you need to complete
        self.fullname=fullname
        self.phonenumber=phonenumber
        self.Email=Email       
        self.address=address
        self.password=password
        self.userdetails={"name":fullname,"phonenumber":phonenumber,"Email":Email,"address":address,"password":password}
        print("account created ")
        
    def user_login(self,Email,password): # you need to complete
        if len(self.userdetails)!=0:
            if Email==self.userdetails["Email"] and password == self.userdetails["password"]:
                print("/n!! succesfully log in !!/n")
                return True
            else:
                return False
        else:
            return False
    
    
    def place_order(self):
        try:
            foodlist=[]
            if len(self.food)==0:
                print("No item available for order")
            else:
                while True:
                    print('list of available items')
                    for i in self.food.key():
                        print(f"FOOD ID {i} : [{self.food[i]['NAME']} {self.food[i]['PRICE']} {self.food[i]['QUANTITY']}] (Items Left : {self.food[i]['STOCK']})") 
                    print('\n1. ORDER\n2. EXIT')
                    x = input('/n enter the option - /n')
                    if x == '1':
                        l = [int(i) for i in input('enter number by separated comma ').split(',')]
                        for i in l:
                            if i in self.food.keys():
                                if self.food[i]['STOCK']==0:
                                    print(f"not available - {i}")
                                else:
                                    if self.food[i]['STOCK']>0:
                                        foodlist.append(i)
                                        print(f'order done - {i}')
                                        self.food[i]['STOCK'] -= 1
                            else:
                                print(f'invalid food - {i}')
                        if foodlist:
                            print("\n----------selected items----------\n")
                            for i in self.food.keys():
                                print(f"{self.food[i]['NAME']} {self.food[i]['PRICE']} {self.food[i]['QUANTITY']}")
                        else:
                            print('\n----------EMPTY-----------\n')

                    elif x=='2':
                        break

                    else:
                        print('\n invaild option \n')
            if len(foodlist):
                    for i in foodlist:
                        self.ordered_item.append([self.food[i]['NAME'],self.food[i]['PRICE'],self.food[i]['QUANTITY']])
                    
        except Exception as e:
            print('\nINVALID INPUT ENTERED\n')
     
                    
                 
                            

    def ordered_history(self): 
        pass
              

    def update_details(self): 
         pass

    
    
# driver code


def driver_code(name): # any function name
    try:
    
        obj=FoodApp(name)

        while True:
            print(f'WELCOME TO MY RESTRO { obj.foodapp_name}\n')
            print('1. ADMIN')
            print('2. USER')
            print('3. CLOSE\n')

            x= input('Enter the number : ')
            if (x=='1'):
                while True:
                    print('\n1. ADMIN REGISTER')
                    print('2. ADMIN LOGIN')
                    print('3. BACK')

                    y= input('Enter the number : ')

                    if y=='1':  
                        email= input('ADMIN ID/EMAIL : ')
                        password = input('ADMIN PASSWORD : ')
                        obj.admin_register(email, password)

                    elif y=='2':

                        email= input('ADMIN ID/EMAIL : ')
                        password = input('ADMIN PASSWORD : ')
                        if obj.admin_login(email, password):

                            while True:  
                                print('\n1. Add new food item')
                                print('2. Edit food item')
                                print('3. View food item')
                                print('4. Delete food item')
                                print('5. Back')

                                z=input('Enter the number')
                                if z=='1':
                                    name= input('Enter the food name : ')
                                    quantity=input('Enter Updated Quantity like For eg, 100ml, 250gm, 4pieces etc : ')
                                    price=int(input('Enter Updated Price in RS : '))
                                    discount=float(input('Enter Updated Discount in RS : '))
                                    stock=int(input('Enter Updated Stock in RS : '))

                                    obj.add_food_item(name, quantity, price, discount, stock)

                                elif z=='2':
                                    foodid = int(input('Enter food id : '))
                                    obj.edit_food_item(foodid)

                                elif z=='3':
                                    obj.view_food_item()

                                elif z=='4':
                                    foodid = int(input('Enter food id : '))
                                    obj.delete_food_item(foodid)

                                elif z=='5':
                                    break

                                else:
                                    print('Invalid option\n')
                                    
                        else:
                            print('INVALID EMAIL OR PASSOWRD')

                    elif y=='3':
                            break
                    else:
                        print('INVALID OPTION')
            elif x=='2':
                 while True:
                    print("1.sign up")
                    print("2.sign in")
                    print("3.Back")
                    
                    p1 = input("Enter no : ")
                    if p1 =='1':
                        fullname=input("fullname : ")
                        phonenumber = input("phonenumber : ")
                        Email=input("Enter Emaild id : ")                                
                        address = input("Enter address : ")
                        password = input("Enter password : ")
                        obj.user_register(fullname,phonenumber,Email,address,password)
                        
                    elif p1=='2':
                            Email= input('Enter EMAIL : ')
                            password = input('Enter PASSWORD : ')
                            if obj.user_login( Email,password):
                                print('succ')
                                
                                while True:
                                    print('\n----------------USER DASHBOARD-------------------\n')
                                    print('\n1. Place New Order')
                                    print('2. Order History')
                                    print('3. Update Profile')
                                    print('4. Back')                                
                                    y=input('Enter the option : ')
                                    if y=='1':
                                        obj.place_order()
                                
                    
                                
                            
                               
                           
            elif x=='3':
                break

            else:
                print('Please enter again')
                
                
                
                
      
            
                
    except Exception as e:
        print('\n SOMETHING WENT WRONG')
        
        
        
    
if __name__=="__main__":
    
    name= input('Enter the APP Name : ')
    driver_code(name)
    
    
print('\nTHANK YOU VISIT AGAIN :)')   

# HTML , CSS, JAVASCRIPT


# In[ ]:




