import nose
from nose.tools import *
from ticketprice import *

def test_ticket_price_takes_an_age_as_an_argument():
    assert_raises(TypeError, ticket_price)

def test_ticket_price_raises_ValueError_if_age_is_negative():
    assert_raises(ValueError, ticket_price, -1)

def test_ticket_price_raises_ValueError_if_age_is_invalid_string():
    assert_raises(ValueError, ticket_price, "Hello")

def test_ticket_price_calculates_the_price_for_travelers_under_18():
    assert_equal(ticket_price(12), 10)

def test_ticket_price_calculates_the_price_for_travelers_18_to_64():
    assert_equal(ticket_price(33), 20)

def test_ticket_price_calculates_the_price_for_travelers_over_64():
    assert_equal(ticket_price(65), 15)