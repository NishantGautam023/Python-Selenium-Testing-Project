from seleniumbase import BaseCase

class HomePage(BaseCase):

    # Put all the Locators Here
    page_url = "https://dishdelish.netlify.app/"
    title_text = "DishDelish Food Version 6.0"
    nav_links = ".nav--btn"
    page_title ="DishDelish Food Version 6.0"
    footer = ".text-red"
    login_button = "//*[@class='nav--btn' and contains(., 'Login')]"
    logout_button = "//*[@class='nav--btn' and contains(., 'Logout')]"
    favourtes_button = ".btn--secondary"
    favourtes_click = ".absolute span"
    
   
    


   # Login Section
    user_name = "sippy@gmail.com"
    user_password = "123456"
    signIn_button = ".inline-block"
    email_button = "input[type='email']"
    password_button = "input[type='password']"
    user_name = "sippy@gmail.com"
    user_password = "123456"
    signUp_anchor = ".text-red"
    signUp_button = "button[type='submit']"
    error_message = ".error-text"

    #Help Page Section
    heading_help_page= ".card-container-title"
    help_page = "//*[@class='nav--btn' and contains(., 'Help')]"
    accordin = ".cursor-pointer"



    def open_page(self):
        self.open(self.page_url)

    def login(self):
        
        
        self.wait_for_element(self.login_button).click()
        
        # fill the form
        self.send_keys(self.email_button, self.user_name)
        print(f"The user have entered {self.user_name}")
        self.send_keys(self.password_button, self.user_password);
        print(f"The user entered password as {self.user_password[0:3]}****")


        # click the signIn button
        self.click(self.signIn_button)
        # Verify the user Email has been displayed
        self.assert_text("Hello sippy@gmail.com !!!", ".text-green");
        print(f"The user is LoggedIn and status is Online")
        self.wait(3);
        # Click on Logout
        self.slow_click(self.logout_button);
        self.wait_for_element(self.login_button).click()
        self.wait(2)


    def register(self):
        self.click(self.login_button);
        self.wait(2);
        self.click(self.signUp_anchor);

        # If already Registered users tries to re-register Again

        self.send_keys(self.email_button, self.user_name)
        self.send_keys(self.password_button, self.user_password);
        self.click(self.signUp_button);
        self.wait_for_element_present(self.error_message)
        self.assert_text("Firebase: Error (auth/email-already-in-use).", self.error_message)
        self.wait(3)

        # If it is a New User but gives password less than 6 characters.
        
        # Find the form field element and clear its value
        form_field = self.find_element(self.email_button)
        form_field.clear()

        # Verify that the form field value is empty
        assert form_field.get_attribute("value") == ""
        self.wait(4)









