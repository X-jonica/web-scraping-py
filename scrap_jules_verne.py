import requests
from bs4 import BeautifulSoup

# 1. URL cible 
url = "https://www.espacefrancais.com/les-oeuvres-de-jules-verne/"

# 2. Envoyer une requete HTTP
response = requests.get(url)

# 3. Vérifier si la requete a reussi
if(response.status_code == 200):
    # 4. Parser le HTML avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # 5. Trouver tous les titres (exemple : balise <h2> ou <a> selon le site )
    # Adapter le selecteur en inspectant le HTML 
    h5_tags = soup.find_all('h5', align="left") #cible

    for i, h5 in enumerate(h5_tags, 1) :
        #Recuperer les text du <span> a l'interieur du <h5>
        title_span = h5.find('span')
        if title_span:
            title = title_span.get_text(strip=True) #nettoie les espaces superflus
            print(f"{i}. {title}")

else:
    print("Erreur : Impossible d'acceder a la page.")