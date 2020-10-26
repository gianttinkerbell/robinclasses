import feedparser
from pprint import pprint

feed1 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale')
feed2 = feedparser.parse("https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale&Day=tomorrow")
#pprint(feed1)

#creating list from today's price
address_price_list_today = []
for entry in feed1['entries']:
    address_price_list_today.append({'Date': entry['updated'], 'Address': entry['address'], 'Price': float(entry['price'])})
#pprint(address_price_list_today)

#creating list from tomorrow's price
address_price_list_tomorrow = []
for entry in feed2['entries']:
    address_price_list_tomorrow.append({'Date': entry['updated'], 'Address': entry['address'], 'Price': float(entry['price'])})
#pprint(address_price_list_tomorrow)

#adding two list
address_price_list = address_price_list_today + address_price_list_tomorrow
#pprint(address_price_list)

#sorting by price
def by_price(item):
   return item['Price']
sorted_price = sorted(address_price_list, key=by_price)
pprint(sorted_price)

#Making a HTML Table

style ='''<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}

</style>
</head>
<body>'''

my_list =''
for entry3 in sorted_price:
    my_list += f'''
{style}
<tr style="background:#ffdddd">
<td>{entry3["Address"]}</td>
<td>{entry3["Date"]}</td>
<td>{entry3["Price"]}</td>
</tr>
'''

fuel_table = f'''
<h2>Fuel Price Table</h2>

<table>
  <tr>
    <th>Address</th>
    <th>Date</th>
    <th>Price</th>
  </tr>

{my_list}

</table>

'''

f = open('table.html', 'w')
f.write(fuel_table)
f.close()
