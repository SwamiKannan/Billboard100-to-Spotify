from bs4 import BeautifulSoup
import requests
import calendar


class Billboard:
    def __init__(self):
        self.playlist_length = None
        self.calender_dict_non_leap = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30,
                                       12: 31}
        self.calender_dict_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30,
                                   12: 31}
        self.date, self.month, self.year, self.ranks = None, None, None, {}
        self.url, self.response = "", ''

    def get_dates(self):
        complete_date = input('Please enter the date chosen in "DD/MM/YYYY" format\n')
        req_len = input(
            'How many songs do you want in your playlist? Type 1,2 etc for number of songs or press "Enter" for all songs.')
        try:
            self.playlist_length = int(req_len)
            print(f'Top {self.playlist_length} songs selected\n')
        except:
            self.playlist_length = None
            print(f'All songs selected\n')
        date_arr = complete_date.split('/')
        date, month, year = int(date_arr[0]), int(date_arr[1]), int(date_arr[2])
        # print(date, month, year)
        if month not in range(1, 13):
            print('Incorrect month provided')
            exit()
        if date > calendar.monthrange(year, month)[1] or date < 1:
            print('Incorrect date provided')
            exit()
        self.date, self.month, self.year = str(date), str(month), str(year)

        return None

    def get_url(self):
        self.get_dates()
        self.date = '0' + self.date if len(self.date) < 2 else self.date
        self.month = '0' + self.month if len(self.month) < 2 else self.month
        self.url = "https://www.billboard.com/charts/hot-100/" + self.year + '-' + self.month + '-' + self.date + '/'
        print(self.url)

    def get_ratings(self):
        self.get_url()
        self.response = requests.get(self.url)
        page = BeautifulSoup(self.response.text, 'html.parser')

        # Get first song
        first_song = page.find_all("ul",
                                   class_="o-chart-results-list-row // lrv-a-unstyle-list lrv-u-flex u-height-200 "
                                          "u-height-100@mobile-max u-height-100@tablet-only "
                                          "lrv-u-background-color-white a-chart-has-chart-detail")
        if len(first_song) == 0:
            print("Sorry. No records found")
            exit()
        title_1 = first_song[0].find_all("h3", {"id": "title-of-a-story"})[0].text.strip()
        band_1 = first_song[0].find_all("span")[1].text.strip()
        # for band in band_1:
        #     print(band)
        self.ranks[1] = (title_1, band_1)

        # Get all songs from rank 2 to 100
        title = page.find_all("li",
                              class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex "
                                     "lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 "
                                     "u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 "
                                     "lrv-u-padding-l-1@mobile-max")

        for i, p in enumerate(title):
            song_name = p.find("h3")
            band_name = p.find("span")
            self.ranks[i + 2] = (song_name.text.strip(), band_name.text.strip())
        self.ranks = self.ranks[range(self.playlist_length)] if self.playlist_length else self.ranks
        print('List of songs extracted....\n\nFinal list:')

        for k in self.ranks.values():
            print(k[0] + ' by ' + k[1])
        print('\nThe list of songs is also available at: ', self.url)

# bb = Billboard()
# bb.get_ratings()
# print(bb.ranks)
