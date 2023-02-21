from seleniumbase import BaseCase

class HomePage(BaseCase):

    # Put all the Locators Here
    page_url = "https://dishdelish.netlify.app/"
    title_text = "DishDelish Food Version 6.0"
    nav_links = ".nav--btn"
    page_title ="DishDelish Food Version 6.0"
    footer = ".text-red"
    user_name = "sippy@gmail.com"
    user_password = "123456"
    login_button = "//*[@class='nav--btn' and contains(., 'Login')]"
    signup_button = ".inline-block"
    email_button = ".form_control"
    password_button = "input[type='password']"



    def open_page(self):
        self.open(self.page_url)

    def login(self):
        self.open(self.page_url);
        self.wait(3)
        self.find_element(self.login_button).click()
        self.wait(1);
        # fill the form
        self.send_keys(self.login_button, self.user_name)
        self.send_keys(self.password_button, self.user_password);
        # click the signup button
        self.click(self.signup_button)
        # Verify the user Email has been displayed
        self.assert_text("Hello sippy@gmail.com !!!", ".text-green");
        self.wait(3);




