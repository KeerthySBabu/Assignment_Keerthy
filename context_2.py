from playwright.sync_api import expect, sync_playwright
def test_application():
   with sync_playwright() as p:
      browser = p.chromium.launch(headless = False)
      user_context = browser.new_context() # creare new contest
      user_page = user_context.new_page()
      user_page.goto("https://www.akbartravels.com/in")
      expect(user_page).to_have_title("Akbar Travels - Best Travel Website. Book Flights, Hotels, Holidays & more")
      
      hotel_context =browser.new_context()
      hotel_page = hotel_context.new_page()
      hotel_page.goto("https://www.akbartravels.com/in/cheap-hotels/")
      expect(hotel_page).to_have_title("Book Cheap Hotels in India | Budget Hotel Booking Deals - Akbar Travels")