from selenium.webdriver.common.by import By
class Register_locators:
    name_input = {"by":By.XPATH, "value": "//input[@aria-label='Name']"}
    surname_input = {"by":By.XPATH, "value":"//input[@aria-label='Last Name']"}
    email_input = {"by":By.CSS_SELECTOR,"value":"[aria-label=Email]"}
    password_input = {"by":By.CSS_SELECTOR,"value":"[aria-label=Password]"}
    confirm_pass_inp = {"by":By.XPATH,"value":"/html/body/div[1]/div/div/main/div/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[3]/label[5]/div/div/div[2]/input"}
    next_button = {"by":By.XPATH, "value":"/html/body/div[1]/div/div/main/div/div/div[2]/div/div[1]/div/div/div/div[3]/button"}

    mailtrap_google_login_button = {"by": By.CSS_SELECTOR, "value":".google-signup.mbm"}
    mailtrap_gmail_input = {"by":By.ID, "value":"identifierId"}
    mailtrap_gmail_input_next = {"by":By.CSS_SELECTOR,"value":".VfPpkd-vQzf8d"}
    mailtrap_gmail_pass = {"by": By.CSS_SELECTOR, "value": ".whsOnd.zHQkBf"}
    mailtrap_gmail_pass_next = {"by": By.CSS_SELECTOR, "value": ".VfPpkd-vQzf8d"}

    mailtrap_last_mail = {"by":By.XPATH, "value":"/html/body/div[2]/div/div[2]/div/div[1]/div[2]/ul/li[1]/a"}
    mailtrap_mail_click = {"by":By.XPATH,"value":"/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/a"}
