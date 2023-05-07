product_menu={}

menu='''
        press 1 for manager
        press 2 for customer
        press 3 for exit '''
        
status=True
p_status=True

while status:
    print(menu)
    choice=int(input("enter your choice"))
    if choice==1:
        while p_status:
            spec={}
            print("welcome to product manager :-")
            product_name=input("enter your product name :-")
            qty=int(input("enter your quantity :-"))
            amount=int(input("enter amount :-"))
            
            if product_name in product_menu.keys():
                spec['qty']=product_menu[product_name]['qty']+qty
                spec['amount']=amount
            else:
                spec['qty']=qty
                spec['amount']=amount    
            product_menu[product_name]=spec
            print(product_menu)
            p_choice=input("do you want to add more products? :-")
            
            if p_choice=='n':
                p_status=False
            elif choice==2:
                print("customer")
                
            else:
                print("thank you for using this application")
                status=False           