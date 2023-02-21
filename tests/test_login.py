from seleniumbase import BaseCase

class LoginTest(BaseCase):

    def setUp(self):
        super().setUp();
        print("Running Before Each Test case");

        # open page
        self.open_page()

        # Login
        self.login()



    def tearDown(self):
        print("Running after Each test")
        # Logout
        self.find_element("//*[@class='nav--btn' and contains(., 'Logout')]").click()
         # Verify the Please Login !!! been displayed
        self.assert_text("Please Login !!!", ".text-green"); 


        super().tearDown();

        
            


    def test_login_page(self):
        
        # open page
        print("Hello")
        
       

        # fill the form
   

        
        

      
        
        

        

        

