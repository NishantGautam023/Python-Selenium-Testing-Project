
from page_objects.home_page import HomePage


class LoginTest(HomePage):

    def setUp(self):
        super().setUp(); # It will go to the setup class of BaseCase 
        print("------🏃🏃🏃🏃Test Case Started Running🏃🏃🏃🏃----------")
        print("")

        self.open(self.page_url)
        print(f"We Have Opened {self.page_url}")


    def test_login_page(self):
        
        # open page by callling Login Method defined in home_page.py
        self.login();
       
        
       
    def test_registration_page(self):
        self.register();


   

        
        

      
        
        

        

        

