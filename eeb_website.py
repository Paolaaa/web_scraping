curl 'https://www.eeb.ucla.edu/seminars.php?id=[001-800]' > 1.html
curl -L https://www.dropbox.com/s/u70dtrdr35p5tgk/seminars.tar.gz | tar zxv > eeb.html
history
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("eeb.html"))
seminar_pane = soup.find(id="secondary-nav")
dates = seminar_pane.find_all("p", class_="subnavlinks")
dates_p = seminar_pane.find_all("p", class_="subnavlinks")
for p in dates_p:
        div = p.find("div", class_="subnavlinks")
        seminar_dates = div.span
        print seminar_dates.string
history

