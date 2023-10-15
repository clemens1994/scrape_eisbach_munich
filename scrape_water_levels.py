from urllib.request import urlopen

url = "https://www.hnd.bayern.de/pegel/isar/muenchen-himmelreichbruecke-16515005/tabelle?methode=wasserstand&"

page_with_waterlevel_list = urlopen(url)

html_bytes = page_with_waterlevel_list.read()

html = html_bytes.decode("utf-8")


def print_list_with_water_levels(html):
    
    start_index = html.find("<td >")

    if not start_index > -1:
      return

    end_index = html.find("</td>")
    end_index = end_index + html[end_index+1:].find("</td>") + 1

    line = html[start_index+5:end_index]

    print("Tag "+line[:10])
    print("Zeit "+line[11:16])
    print("Stand "+line[41:])
  
    print_list_with_water_levels(html=html[end_index+5:])


print_list_with_water_levels(html)










