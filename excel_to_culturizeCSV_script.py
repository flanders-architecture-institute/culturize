# Dit script gaat uit van het inladen van een Excel. De CSV-export uit de gebouwendatabank moet eerst worden verwerkt tot Excel.
# Tussenstap nodig omdat rechtstreeks inlezen van de gebouwendatabankexport op dit moment niet lukt.

import pandas as pd

workzone = input("Geef de naam van de folder (in de C-schijf), bv. culturizeapp: ")
excelloc = input("Geef de naam van het Excelbestand: ")
excelloc = "C:\\" + workzone + "\\" + str(excelloc)
resultfilename = input("Geef de naam van de resultaat-csv. (Hij wordt opgeslagen in je workzone): ")

df = pd.read_excel(excelloc, na_filter=False, dtype=object) # Inlezen van de Excel
df = df.filter(['id','title','uri','enabled'], axis=1) # Selecteren van de relevante kolommen
df = df.rename(columns={"id": "PID", "uri": "URL"}) # Renamen van de kolommen conform Culturize (https://github.com/PACKED-vzw/CultURIze/wiki/Create-a-Spreadsheet)
df['URL'] = "https://www.vai.be/" + df.URL.map(str) # De domeinnaam toevoegen aan de URL
df.to_csv("C:\\" + str(workzone) + "\\" + str(resultfilename), index=False) # index=False om te vermijden dat de rijnummers mee worden geëxporteerd
print("Culturize-CSV aangemaakt op deze locatie: " + "C:\\" + str(workzone) + "\\" + str(resultfilename))
