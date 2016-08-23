from lxml import html
from trip import Trip

logfile = open("logs/2016-08.html", "r")
webpage = open("docs/index.html", "rw")

page = webpage.read()
print(page)

content = logfile.read()
tree = html.fromstring(content)

# Find and print the log period
log_period = tree.xpath('.//span[@class="history-for"]/text()')[0].split(' ')
# log_period = log_period.split(' ')
month = log_period[0]
year = log_period[1]

print('Month: ' + month)
print('Year: ' + year)

logs = tree.findall('.//table[@class="result-tables"]')

print('Nodes: ' + str(len(logs)))
i = 1

for trip in logs:
    trip_period = trip.xpath('.//div[@class="dr-title"]/text()')[0].split(' ')
    date = trip_period[0]
    minutes = trip_period[2]
    
    checkout = trip.find_class('trip-checkout')[0].text_content().split(' - ')
    checkin = trip.find_class('trip-checkin')[0].text_content().split(' - ')
    miles = trip.find_class('trip-miles')[0].text_content().split(' ')[0]
    cost = trip.find_class('trip-cost')[0].text_content().split(' ')[1]

    checkout_time = checkout[0].split(' ')[0] + checkout[0].split(' ')[1]
    checkout_station = checkout[1]
    checkin_time = checkin[0].split(' ')[0] + checkin[0].split(' ')[1]
    checkin_station = checkin[1]

    # Check the type of a return value:
    # print('Type: ' + type(checkout).__name__)

    print('Date: ' + date)
    print('Minutes: ' + minutes)
    
    print('Checkout Time: ' + checkout_time)
    print('Checkout Station: ' + checkout_station)
    print('Checkin Time: ' + checkin_time)
    print('Checkin Station: ' + checkin_station)
    print('Miles: ' + miles)
    print('Cost: ' + cost)
    print('\n----------------\n')
    i += 1

logfile.close()
webpage.close()

