from seleniumbase import BaseCase

class CartPage(BaseCase):
    favourties_button = ".btn--secondary"
    error_message = "#error-message"
    search_button = ".btn--primary"
    nav_links = ".nav--btn"
    search_text = ".//h6[text()='Asha tiffins']"  # This might change due to Dynamic API
  
    search_using_menu = ".//h6[text()='Namaste']" # This mighr change due to Dynmaic API
    food_item =".tracking-normal"
    search_box = ".outline-none"
    make_favourite = "❤"
    login_button = "//*[@class='nav--btn' and contains(., 'Login')]"
    logout_button = "//*[@class='nav--btn' and contains(., 'Logout')]"
   
   # Login Section
    signIn_button = ".inline-block"
    email_button = "input[type='email']"
    password_button = "input[type='password']"
    user_name = "sippy@gmail.com"
    user_password = "123456"



    # checkout Section
    all_items_Add = ".//button[text()='+']"
    all_items_Minus = ".//button[text()='-']" 
    recommended_items = "p.text-sm"
    checkout_button = ".//button[text()='CHECKOUT']"
    empty_image_cart = "h2.my-4"
    subTotoal_text = ".text-bio"
    subCart_add = ".delay-100"
    subcart_minus = ".//button[@class='text-xl']"
    number_of_items_in_cart =".//p[@class='text-gray-count']"
    clear_cart_button = ".bg-red"
    user_login_button =".//button[text()='LOG IN']"
    user_signup_button  = ".//button[text()='SIGN UP']"
    cart_count = "text-orange"
    empty_cart_button =" .//button[text()='SEE RESTAURANTS NEAR YOU']"

    # Delivery Address
    home_address = ".//h2[text()='Home']"
    work_address = ".//h2[text()='Work']"

    #Payment Method
    payment_method_online = ".//h2[text()='Pay Online']"
    payment_method_offline = ".//h2[text()='Pay Offline']"
    proceed_payment_button = ".//button[text()='PROCEED TO PAYMENT']"


    def UserLoggedIn(self):
        self.click(self.search_using_menu);
        self.wait(3);
        
        # Check the Image is displayed with the message when the cart is empty
        self.assert_text("Good food is always cooking! Go ahead, order some yummy items from the menu.", self.empty_image_cart)
        # Aseert Number of Recommended Items in the Restaurant
      #  self.assert_teitemst("85", self.recommended_items)
        

        restaurant_items = self.find_elements(self.all_items_Add)
        for items in range(0,1): # displaying only 1 due to Exception Error. 
            if restaurant_items[items].is_displayed():
                restaurant_items[items].click()


        self.wait(3);
        self.click(self.checkout_button)
        self.wait(3);
        self.click(self.home_address)
        self.wait(3)
        self.click(self.payment_method_online)


        

    







