class Constants:
    def __init__(self):
        print("Constants Loaded")

    @staticmethod
    def landing_url():
        return "https://katalon-demo-cura.herokuapp.com/#"

    @staticmethod
    def login_url():
        return "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    @staticmethod
    def appointment_url():
        return "https://katalon-demo-cura.herokuapp.com/#appointment"

    @staticmethod
    def confirmation_url():
        return "https://katalon-demo-cura.herokuapp.com/appointment.php#summary"

    @staticmethod
    def homepage_url():
        return "https://katalon-demo-cura.herokuapp.com/"
