
BASE_URL = "https://restful-booker.herokuapp.com"

class APIconstants():
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking/"

    @staticmethod
    def create_token():
        return "https://restful-booker.herokuapp.com/auth"

    @staticmethod
    def url_put_patch_delete(bookingid):
        return "https://restful-booker.herokuapp.com/booking/"+ str(bookingid)


