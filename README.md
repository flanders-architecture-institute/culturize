# Culturize
Repository for VAi's CulturizeApp

# Quick csv-creation
Zie excel_to_culturizeCSV_script.py voor snelle CSV-creatie. (Gebruik Python3 met Pandas geïnstalleerd)

Als de culturize app niet meer werkt om één of andere reden, voeg dan volgende code toe aan het culturizeCSV_script om zelf de nieuwe .htaccess text te generen. Copy paste deze rechtstreeks in de Github repo.

```python
obj = df.to_dict('records')
for page in obj:
    pid = page.get('PID')
    url = page.get('URL')
    string = f'RewriteRule ^{pid}$ {url} [R=302,NC,NE,L]'
    print(string)
```

# Webserver
De webserver is een apache webserver die draait op de Amazon cloud (EC2 Free Tier). SSH-toegang hiertoe is beperkt tot enkele IP-adressen. Kijk of het IP-adres van de computer opgelijst staat in de security-group vooraleer via SSH met de server te connecteren. Gebruik Putty voor SSH-access (https://www.putty.org/)
