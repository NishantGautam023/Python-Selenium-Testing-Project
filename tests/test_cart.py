from page_objects.cart_page import CartPage




class CartPageTest(CartPage):

    def setUp(self):
        super().setUp();
        self.open("https://dishdelish.netlify.app/")

    
    # Add to Cart without logged In and using the SearchBar 
    def test_add_to_cart_NotLoggedIn(self):
        self.click(self.search_text);
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
        self.click(self.clear_cart_button)
        self.wait(2);
       


    # Add to Cart When the user is Looged in and using the Menu List

    def test_add_to_cart_LoggedIn(self):
        self.wait(3);
        self.click(self.login_button)
        self.wait(3);

        # fill the form
        self.send_keys(self.email_button, self.user_name)
        self.send_keys(self.password_button, self.user_password);
        # click the signup button
        self.click(self.signIn_button)
        self.wait(1)
        # Verify the user Email has been displayed
        self.assert_text("Hello sippy@gmail.com !!!", ".text-green");
        self.wait(3);

        self.UserLoggedIn();

       




        

      
           

