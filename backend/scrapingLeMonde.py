import requests
from bs4 import BeautifulSoup
import json


# Fonction pour récupérer et parser la page HTML
def get_articles_from_lemonde(search_query, page=1):
    url = f"https://www.lemonde.fr/recherche/?search_keywords={search_query}&start_at=&end_at=&page={page}"


    # En-têtes pour imiter un navigateur (User-Agent)
    headers = {
    'Host': 'www.lemonde.fr',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://www.lemonde.fr/recherche/',
    'Connection': 'keep-alive',
    'Cookie': 'lmd_rand_id=382799738154206334; lmd_initial_source_params=%7B%22referrer%22%3A%22https%3A%2F%2Fwww.ecosia.org%2F%22%7D; pa_privacy=%22optin%22; atauthority=%7B%22name%22%3A%22atauthority%22%2C%22val%22%3A%7B%22authority_name%22%3A%22default%22%2C%22visitor_mode%22%3A%22optin%22%7D%2C%22options%22%3A%7B%22end%22%3A%222026-12-29T13%3A52%3A03.881Z%22%2C%22path%22%3A%22%2F%22%7D%7D; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbAJ4BWAO4BHAOYA3GAB9%2B9ABZKIALwBWMEAF8gA; atidx=019AC595-D857-703E-8890-949F53FD9E0B; atid=019AC595-D857-703E-8890-949F53FD9E0B; lmd_pa=1764251523; euconsent-v2=CQbi80AQbi80AFzACBFRCGFsAP_gAAAAAAqII7NB7G_fSSFjcTZ3YPtkaYxfx1Bi4sAhBgIBgywBiBqQoIwWkmAqIAjAAqAKGBIAImRBIQBtGAjABAAAAIABISCEAECAARAAJqBAAEARAgFACAhJGQEAEAAQgEDUAhUAgAIEQFooQNxAAgAgLQAAIAAhAIAFAAAIACAAQAAAAAAAQmAAAAAAAAAAAAAAABAIEEdgARDQqIICwIAAgEDCCBAAoIwgAIEAQAAAAwQAABAwIUAYACDARAAAAAAAEAAAAAQAAgAAAgAQgAAAAAEAAEAAAAAAAAAAAABAgAAAAgQAAAAQEAIAAAAAAAAAiAAgAQAAAAAgAICgAAAAQFgAAAAAAAEAAAAAAAAAAAAAAAAAAASAAAAAAAAAAAAAAAAAECAMEgAwABBHYdABgACCOxCADAAEEdiUAGAAII7FIAMAAQR2LQAYAAgjsA; lmd_consent=%7B%22userId%22%3A%2255b8e385-f113-4acf-b41f-567094c5fa47%22%2C%22timestamp%22%3A%221764251523.876987654%22%2C%22version%22%3A2%2C%22cmpId%22%3A371%2C%22displayMode%22%3A%22cookiewall%22%2C%22purposes%22%3A%7B%22analytics%22%3Atrue%2C%22ads%22%3Atrue%2C%22personalization%22%3Atrue%2C%22mediaPlatforms%22%3Atrue%2C%22social%22%3Atrue%7D%2C%22optoutAnalytics%22%3Afalse%7D; AMP_7dec6d6e90=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIyNmYzNmRjYi0xNTJjLTRiN2ItOTdhNy01YjI3NDkxOWY0YjElMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzY0MjUxNTI1NTg2JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTc2NDI1NTU4NDQ5OSUyQyUyMmxhc3RFdmVudElkJTIyJTNBNjklMkMlMjJwYWdlQ291bnRlciUyMiUzQTAlN0Q=; __spdt=665ad70e06ae4c4f93fc7f566c51272c; _gcl_au=1.1.1768912401.1764251524; _pin_unauth=dWlkPVptTmlOVEEyTldNdFpURTJNQzAwT0Rnd0xUbGtNREl0TVdFME9XVXlZakkzTW1ZMA; fc_all_cd=%7B%220197cfd7-c351-7cbf-8f7b-2cfe1c3d904b_02760314-f1c6-4255-a229-e57eb15c1a97%22%3A%7B%22offerId%22%3A%22paywall_abandon_ppo_classique%22%7D%7D; AF_BANNERS_SESSION_TOKEN=bu2ef31hb1i1764251524289; _cb=D2HK7uB5DSm9Cx3SQx; _chartbeat2=.1764251524305.1764255583634.1.LPtftHj_wEDhE5dsCX8LNACuGYav.19; _cb_svref=https%3A%2F%2Fwww.ecosia.org%2F; lead=3c0f8a43-9361-434d-9e27-6d88fb993886; lead_ads=3c0f8a43-9361-434d-9e27-6d88fb993886; _fbp=fb.1.1764251524493.452694200178255567; AMP_MKTG_7dec6d6e90=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5lY29zaWEub3JnJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMnd3dy5lY29zaWEub3JnJTIyJTdE; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-43260-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; lmd_cap=_08i075esf; uid_dm=077e8710-1551-18c7-a7df-790abc912420; __gads=ID=9f0c046e088f7f2e:T=1764251532:RT=1764255525:S=ALNI_Ma2pPvemXsQ4hqq9t1np1oYxP6zWg; __gpi=UID=0000131459f35625:T=1764251532:RT=1764255525:S=ALNI_Mb29V1PHpf026ZsZGdz9nlNkrcRkQ; __eoi=ID=d968d70208b8caf3:T=1764251532:RT=1764255525:S=AA-AfjZJRy_BLhMIhjjp92rmeAT-; ivbsdid={"id":"qvmcisvyce62t5_a4"}; ivNotCD=y; ivdtbrk=20422.2,7,10; ivBlk=n; _t_tests=eyJ5QURvdnFvYkhWNVVjIjp7ImNob3NlblZhcmlhbnQiOiJCIiwic3BlY2lmaWNMb2NhdGlvbiI6WyJCNEpleS0iXX0sImxpZnRfZXhwIjoibSJ9; _chartbeat5=773|143|%2F|https%3A%2F%2Fwww.lemonde.fr%2F|VHeScBvSYX4DJvQ00CFe4jjDoxfPX||c|DMKV-7Bb94CQCWeZzjCL6J2tROdmQ|lemonde.fr||',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
    'TE': 'trailers'
}
   
    # Envoi de la requête HTTP avec les en-têtes
    response = requests.get(url, headers=headers)
   
    # Vérifier si la requête a réussi
    if response.status_code != 200:
        print(f"Erreur lors de la récupération de la page {url}")
        return []
   
    # Parser le contenu HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    # Liste pour stocker les articles extraits
    articles = []


    # Recherche des titres dans les balises <h3> et des liens dans le premier <a>
    for article in soup.find_all('h3'):
        title_tag = article.find('a')
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag['href']
            articles.append({'title': title, 'link': link})
   
    return articles


# Exemple d'utilisation : chercher les articles sur "Ukraine" à partir de la première page
search_query = "ukraine"
articles = get_articles_from_lemonde(search_query, page=1)


# Convertir les résultats en JSON et l'afficher
articles_json = json.dumps(articles, ensure_ascii=False, indent=4)
print(articles_json)
