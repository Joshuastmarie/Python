from flask_app.models.listing_model import Listing
import unittest
from flask import flash
from flask_app import app

class ModelTests(unittest.TestCase):

    def setup(self):
        self.app = app.run(port=8000, debug=True)
        return super().setup()

    # happy case - test passes

    def test_validator_listing_validates_form(self):
        test_form_data = {
            "street" : "1011 3rd st",
            "city" : "Snohomish",
            "state" : "WA",
            "zip" : "98290",
            "bd_count" : "2",
            "full_bath" : "2",
            "half_bath" : "1",
            "a_price" : "1000000",
            "square_ft" : "2000",
            "gross_sales" : "200000"
        }
        result = Listing.validator_listing(test_form_data)
        return self.assertEquals(result, False)

    # def test_validator_listing_fails()

if __name__=='__main__':
    unittest.main()