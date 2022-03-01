from textwrap import dedent


def welcome_msg() :
  """ this function will print the welcome message on the screen """

  print("**************************************")
  print("**    Welcome to the Snakes Cafe!   **")
  print("**    Please see our menu below.    **")
  print("**")
  print("** To quit at any time, type \"quit\" **")
  print("**************************************")

def promot_order():

    """this function will prompt the user for an order"""
    print( " ***********************************")
    print("** What would you like to order? **")
    print(" ***********************************")

cafe_menu = {

    "Wings":0,
    "Cookies":0,
    "Spring Rolls":0,
     
    "Salmon":0,
    "Steak":0,
    "Meat Tornado":0,
    "A Literal Garden":0,

    "Ice Cream":0,
    "Cake":0,
    "Pie":0,

    "Coffee":0,
    "Tea":0,
    "Unicorn Tears":0,

}

cafe_menu_sections = dedent("""
Appetizers
----------
{}
{}
{}

Entrees
-------
{}
{}
{}
{}

Desserts
--------
{}
{}
{}

Drinks
------
{}
{}
{}
""".format(*cafe_menu)
)

welcome_msg()
print(cafe_menu_sections)
promot_order()
order={}
item=input('> ')

while item!='quit':
    if item.lower() not in [key.lower() for key in cafe_menu.keys()]:
      #if the user enterd an item that is not exist in the menue , this message will appear to him 
      print("**sorry this item is not in our menu , please order items from the above menu**")
      item=input('> ')
     

    if item.lower() in [key.lower() for key in cafe_menu.keys()]:
        if item.lower() not in [key.lower() for key in order.keys()]:
          order[item]=0
        order[item.lower()]+=1
        print(f"** {order[item.lower()]} order of {item.lower()} have been added to your meal ")
        item=input('> ')


if item=='quit':
    if order =={}:
        print("**Thank you , have a nice day**")
    else : 
        print(f"**Your order of {order} will be ready soon **")
