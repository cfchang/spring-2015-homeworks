get_city_page(city, state, datadir)
get_hotellist_page(city_url, page_count, city, datadir='data/')
parse_hotellist_page(html)
scrape_hotels(city, state, datadir='data/')

get hotellist --> html



def get_hotel_page(hotel_url):
    """ Returns the URL of the list of reviews for a hotel
    Parameters
    hotel: str

    <div class= "content wrap trip_type_layout">
    'Reviews', 'HotelName', class="property_title", dir="ltr"
    http://www.tripadvisor.com/city=boston&state=ma

    div class = "listing_title"
    """
    #build the request URL
    <a target="_blank" href="/Hotel_Review-g60745-d94330-Reviews-Seaport_Boston_Hotel-Boston_Massachusetts.html" id="property_94330" class="property_title" onclick=" ta.setEvtCookie('Reviews', 'HotelName', 60745, 0, this.href); ta.util.cookie.setPIDCookie(15176);" dir="ltr">
    Seaport Boston Hotel</a>
    
    url = base_url + "Reviews=" + hotelName
    soup = BeautifuSoup(html)

    #get next URL page if exists, otherwise exit
    div = soup.find("div",{"class": "listing_title"})
    if div.find('span', {'class': 'guiArw pageEndNext'}):
        sys.ext()
    hrefs = div.findAll(
    
    hotel_url = div.find('a', href=True)
    return hotel_url['href']

    base_url = www.tripadvisor.com/Hotels-g60745-Boston_Massachusetts-Hotels.html
    http://www.tripadvisor.com/Hotel_Review-g60745-d234752-Reviews-Nine_Zero_Hotel_a_Kimpton_Hotel-Boston_Massachusetts.html
    http://www.tripadvisor.com/Hotel_Review-g60745-d94330-Reviews-Seaport_Boston_Hotel-Boston_Massachusetts.html
    
def scrape_hotels_info():
    get_hotel_page(hotel_url)
<fieldset class="review_filter_lodging">
<div class="content wrap trip_type_layout">
"click" on each hotel
scrape "Traveler rating", "See reviews for ", "Rating summary"
