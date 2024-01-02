import pytest
from Dataset import test_data
from page_object.oneWayTicket import Ticket
@pytest.mark.usefixtures("browser_setup")
class TestTicketFeature:

   def test_ticket_book(self):
       self.book = Ticket(self.driver)
       self.book.ticketBook()

