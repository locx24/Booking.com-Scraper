from playwright.sync_api import sync_playwright
import pandas as pd

def main():
    
    # call the playwright context manager
    with sync_playwright() as p:
        
        # Variables for the checkin and checkout dates
        checkin_date = '2024-12-01'
        checkout_date = '2024-12-24'
        
        page_url = f'https://www.booking.com/searchresults.html?ss=Los+Angeles&ssne=Los+Angeles&ssne_untouched=Los+Angeles&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaIgCiAEBmAExuAEHyAEP2AEB6AEB-AECiAIBqAIDuAKYv-ywBsACAdICJGZkMzQ1Mjc0LWViMWUtNDI0NS04ZWM2LTY2MGY3NzE5YzBjMNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20014181&dest_type=city&checkin={checkin_date}&checkout={checkout_date}&group_adults=2&no_rooms=1&group_children=0'
        
        # instantiate the browser. headless set to false so the user can view the browser open
        browser = p.firefox.launch(headless=False)
        
        # create new webpage
        page = browser.new_page()
        
        # set the webpage to the page_url variable. timeout after 60 seconds
        page.goto(page_url, timeout=60000)
        
        
        # set hotels variable to get the hotels using the page object 
        hotels = page.locator('//div[@data-testid="property-card"]').all()
        
        #print out the number of hotels retrieved
        print(f'There are {len(hotels)} hotels available.')
        
        #store results of hotels in a list
        hotels_list = []
        
        # loop over each hotel and store results in a dictionary
        for hotel in hotels:
            hotel_dict = {}
            hotel_dict['hotel'] = hotel.locator('//div[@data-testid="title"]').inner_text()
            hotel_dict['price'] = hotel.locator('//span[@data-testid="price-and-discounted-price"]').inner_text()
            hotel_dict['score'] = hotel.locator('//div[@data-testid="review-score"]/div[1]').inner_text()
            hotel_dict['avg review'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[1]').inner_text()
            hotel_dict['reviews count'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[2]').inner_text().split()[0]

            # append the hotels dictionary to the hotels list
            hotels_list.append(hotel_dict)
        
        # create pandas dataframe 
        df = pd.DataFrame(hotels_list)
        
        df.to_excel('hotels_list.xlsx', index=False) 
        
        #write hotels list to csv file
        df.to_csv('hotels_list.csv', index=False) 
       
       # close browser
        browser.close()
        
        
if __name__ == '__main__':
    main()