
from page_objects.home_page import HomePage

class HomePageTest(HomePage):


    def setUp(self):
        super().setUp(); # It will go to the setup class of BaseCase 
        print("------🏃🏃🏃🏃Test Case Started Running🏃🏃🏃🏃----------")
        print("")

        self.open(self.page_url)
        print(f"We Have Opened {self.page_url}")


    def tearDown(self):
        
        print("----🥷🥷🥷🥷Test Check Completed🥷🥷🥷🥷----------")
        super().tearDown();

    

    def test_home_page(self):

        # open Home page
        print(f"The title of the page is {self.get_title()}")
        self.assertEqual(HomePage.page_title, self.get_title()) # check title is equal to tile_text
        self.assert_true("DishDelish" in self.get_title())
        # Since the data is coming from the API, wait for few seconds
        self.wait(3)

        # scroll to buttom
        self.slow_scroll_to(".text-red", by="css selector")
        self.click(self.help_page)

        # Goto the Help Page
        self.slow_click(self.help_page)
        expected_heading = 'FAQ'
        returned_heading = self.get_element(self.heading_help_page)
        self.assertEqual(expected_heading, returned_heading.text)
        print(f"The Headiing Matches where {expected_heading} and {returned_heading.text} are same")
        self.click_visible_elements(self.accordin);
        

    def test_header_links(self):
        expected_nav_bars = ["Home", "About", "Instamart", "Help", "Cart 0", "Login ●"]
        print(f"The NavBars present in the Header are {expected_nav_bars}")

        self.wait(3);

        nav_bar_links = self.find_elements(".nav--btn");
        
        for index, links in  enumerate(nav_bar_links): # Getting the index from loop through enumerate
            print(index, links.text)
            self.assertEqual(expected_nav_bars[index], links.text)

        
        self.click_visible_elements(self.favourtes_click)
        self.wait(3)
        self.slow_click(self.favourtes_button)
        self.click_visible_elements(self.favourtes_click)
        # self.wait_for_element(self.favourtes_button).click()

