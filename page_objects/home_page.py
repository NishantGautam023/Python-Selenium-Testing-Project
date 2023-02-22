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


    def open_page(self):
        self.open(self.page_url)

    def login(self):
        self.open(self.page_url);
        self.wait(3)
        self.find_element(self.login_button).click()
        self.wait(1);
        # fill the form
        self.send_keys(self.email_button, self.user_name)
        self.send_keys(self.password_button, self.user_password);
        # click the signIn button
        self.click(self.signIn_button)
        # Verify the user Email has been displayed
        self.assert_text("Hello sippy@gmail.com !!!", ".text-green");
        self.wait(3);

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








