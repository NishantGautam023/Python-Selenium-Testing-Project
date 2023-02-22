
from page_objects.home_page import HomePage

class HomePageTest(HomePage):


    def setUp(self):
        super().setUp(); # It will go to the setup class of BaseCase 
        print("Running before each Test")

        self.open(HomePage.page_url)


    def tearDown(self):
        
        print("Running after each Test")
        super().tearDown();

    

    def test_home_page(self):

        # open Home page
        self.open_page()
        # Get the cookies
        cookies = self.driver.get_cookies()
        
        # Print the cookies
        print(cookies) 



        

        
        self.assertEqual(HomePage.page_title, self.get_title()) # check title is equal to tile_text
        self.assert_true("DishDelish" in self.get_title())

        # Since the data is coming from the API, wait for few seconds
        self.wait(3)

        # scroll to buttom
        self.slow_scroll_to(".text-red", by="css selector")
        

    def test_header_links(self):
        expected_nav_bars = ["Home", "About", "Instamart", "Help", "Cart 0", "Login ●"]

        self.wait(3);

        nav_bar_links = self.find_elements(".nav--btn");
        
        for index, links in  enumerate(nav_bar_links): # Getting the index from loop through enumerate
            print(index, links.text)
            self.assertEqual(expected_nav_bars[index], links.text)

