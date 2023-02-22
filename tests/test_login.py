
from page_objects.home_page import HomePage


class LoginTest(HomePage):

    def setUp(self):
        super().setUp();
        print("Running Before Each Test case");

        # open page
        self.open("https://dishdelish.netlify.app/")

        # Login
        # self.login();



    def tearDown(self):
        print("Running after Each test")
        # Logout
        self.wait(2)
        self.click(self.logout_button)
         # Verify the Please Login !!! been displayed
        self.wait(3)
        self.assert_text("Please Login !!!", ".text-green"); 


        super().tearDown();

        
            


    def test_login_page(self):
        
        # open page
        print("Hello, User has logged iN and logged Out")
        
       
    def test_registration_page(self):
        self.register();


   

        
        

      
        
        

        

        

