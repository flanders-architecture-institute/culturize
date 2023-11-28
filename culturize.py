# Dit script gaat uit van het inladen van een Excel. De CSV-export uit de gebouwendatabank moet eerst worden verwerkt tot Excel.
# Tussenstap nodig omdat rechtstreeks inlezen van de gebouwendatabankexport op dit moment niet lukt.

import pandas as pd
import json

def open_json(json_file):
    with open(json_file, 'r', encoding="utf8") as myfile:
        data = myfile.read()
    obj = json.loads(data)
    return obj

# Om een CSV te maken
def filter_fields(obj):
    filtered_obj = []
    for building in obj:
        filt = {}
        filt['id'] = building['id']
        filt['title'] = building['title']
        filt['uri'] = building['uri']
        filt['enabled'] = building['enabled']
        filtered_obj.append(filt)
    return filtered_obj

def create_dataframe(input_json):
    inputdata = open_json(input_json)
    dic = filtered_fields(inputdata)
    df = pd.from_dict(dic, na_filter=False, dtype=object)
    df = df.rename(columns={"id": "PID", "uri": "URL"}) # Renamen van de kolommen conform Culturize (https://github.com/PACKED-vzw/CultURIze/wiki/Create-a-Spreadsheet)
    df['URL'] = "https://www.vai.be/" + df.URL.map(str) # De domeinnaam toevoegen aan de URL
    return df

def create_culturize_csv(input_json, output_csv):
    df = create_dataframe(input_json)
    df.to_csv(output_csv, index=False) # index=False om te vermijden dat de rijnummers mee worden geëxporteerd
    print("Culturize-CSV aangemaakt op deze locatie: " + str(output_csv))


# Om een .htaccess te maken
def create_culturize_htaccess(input_json, local_htaccess_path):
    obj = open_json(input_json)
    htstrings = [
        'Options +FollowSymLinks',
        'RewriteEngine on',
        ''
        ]
    for page in obj:
        pid = page.get('id')
        url = page.get('uri')
        htstring = f'RewriteRule ^{pid}$ {url} [R=302,NC,NE,L]'
        htstrings.append(htstring)
    
    with open(local_htaccess_path, 'w') as fp:
        fp.write('\n'.join(htstrings))


    print("Culturize-htaccess aangemaakt op deze locatie: " + str(local_htaccess_path))
    print("Push de nieuwe htaccess naar de repository")