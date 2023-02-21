from seleniumbase import BaseCase
from page_objects.home_page import HomePage


class LoginTest(HomePage):

    def setUp(self):
        super().setUp();
        print("Running Before Each Test case");

        # open page
        self.open("https://dishdelish.netlify.app/")

        # Login
        self.login();



    def tearDown(self):
        print("Running after Each test")
        # Logout
        self.wait(2)
        self.find_element("//*[@class='nav--btn' and contains(., 'Logout')]").click()
         # Verify the Please Login !!! been displayed
        self.assert_text("Please Login !!!", ".text-green"); 


        super().tearDown();

        
            


    def test_login_page(self):
        
        # open page
        print("Hello")
        
       

        # fill the form
   

        
        

      
        
        

        

        

