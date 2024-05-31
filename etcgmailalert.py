from typing import Any

import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium_imports import *
import time


def check_api_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print("Exception occurred while accessing URL:", e)
        return False


def send_failure_email(sender_email, sender_password, receiver_emails, failed_urls):
    subject = "404 Page Not Found"
    body = "The following URLs are getting 404 check:\n\n" + "\n".join(failed_urls)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(receiver_emails)  # Join multiple emails with comma
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail SMTP server and port
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_emails, text)  # Send to multiple receivers
        print("Failure email sent successfully!")
    except Exception as e:
        print("An error occurred while sending email:", e)
    finally:
        server.quit()


if __name__ == "__main__":
    # Your existing Selenium script goes here...
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')  # Add this line to avoid /dev/shm issues
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    action = ActionChains(driver)

    driver.get('https://www.equipetonclub.fr/connexion?back=my-account')
    loginmail = driver.find_element(By.ID, 'email')
    loginmail.send_keys('etcaravind@yopmail.com')
    time.sleep(1)
    passwordmts = driver.find_element(By.ID, 'passwd')
    passwordmts.send_keys('Aravind@123')
    submitlog = driver.find_element(By.ID, 'SubmitLogin')
    submitlog.click()
    time.sleep(5)

    allArr = [
        {
            'arr': ['https://www.equipetonclub.fr/content/4-a-propos', 'https://www.instagram.com/equipetonclub.fr', 'https://www.facebook.com/Equipetonclub', 'https://www.pinterest.fr/myteamfoot', 'https://twitter.com/myteamfoot_fr', 'https://www.equipetonclub.fr/#', 'https://www.equipetonclub.fr/', 'https://www.equipetonclub.fr/simulateur3d', 'https://www.equipetonclub.fr/114-pack?orderby=name&orderway=asc&orderway=asc', 'https://www.equipetonclub.fr/126-haut', 'https://www.equipetonclub.fr/130-bas', 'https://www.equipetonclub.fr/132-accessoires', 'https://www.equipetonclub.fr/119-Mailllot', 'https://www.equipetonclub.fr/120-Veste', 'https://www.equipetonclub.fr/129-Sweat', 'https://www.equipetonclub.fr/122-Polo', 'https://www.equipetonclub.fr/127-Parka', 'https://www.equipetonclub.fr/128-Coupe-vent', 'https://www.equipetonclub.fr/140-Tenues-De-Compression', 'https://www.equipetonclub.fr/121-Shorts', 'https://www.equipetonclub.fr/123-Pantalon', 'https://www.equipetonclub.fr/131-Chaussettes', 'https://www.equipetonclub.fr/133-Bonnet', 'https://www.equipetonclub.fr/134-Gants', 'https://www.equipetonclub.fr/118-Sac', 'https://www.equipetonclub.fr/117-ballons', 'https://www.equipetonclub.fr/135-Chasubles', 'https://www.equipetonclub.fr/89-materiel?orderby=name&orderway=asc', 'https://www.equipetonclub.fr/92-Entrainement', 'https://www.equipetonclub.fr/93-Entretien-Equipement-Terrain', 'https://www.equipetonclub.fr/94-Soins', 'https://www.equipetonclub.fr/95-Arbitre-Dirigeant', 'https://www.equipetonclub.fr/96-Outils-Du-Coach', 'https://www.equipetonclub.fr/117-ballons?orderby=name&orderway=asc', 'https://www.equipetonclub.fr/boutique-club', 'https://www.equipetonclub.fr/119-mailot-puma-collection-2021', 'https://www.equipetonclub.fr/120-veste-puma-collection-2021', 'https://www.equipetonclub.fr/122-polo-puma-collection-2021', 'https://www.equipetonclub.fr/121-short-puma-collection-2021', 'https://www.equipetonclub.fr/123-pantalon-puma-collection-2021', 'https://www.equipetonclub.fr/118-sac-puma-collection-2021', 'https://www.equipetonclub.fr/92-entrainement', 'https://www.equipetonclub.fr/93-entretien-equipement-terrain', 'https://www.equipetonclub.fr/94-soins', 'https://www.equipetonclub.fr/95-arbitre-dirigeant', 'https://www.equipetonclub.fr/96-outils-du-coach', 'https://www.equipetonclub.fr/mon-compte', 'https://www.equipetonclub.fr/commande', 'https://www.equipetonclub.fr/recherche?controller=search&orderby=position&orderway=desc&search_query=enfant&submit_search=', 'https://www.equipetonclub.fr/recherche?controller=search&orderby=position&orderway=desc&search_query=ballonpuma&submit_search=', 'https://www.equipetonclub.fr/recherche?controller=search&orderby=position&orderway=desc&search_query=FEMININEPUMA&submit_search=', 'https://www.equipetonclub.fr/recherche?controller=search&orderby=position&orderway=desc&search_query=LIFESTYLEPUMA&submit_search=', 'https://www.equipetonclub.fr/accueil/725908049-offre-pack-entrainement-adulte-cup-jersey-bronze.html?search_query=OFFRE+PACK+ENTRAINEMENT+ADULTE+CUP+JERSEY+BRONZE&results=1', 'https://www.equipetonclub.fr/accueil/725907137-offre-pack-match-feminine.html?search_query=OFFRE+PACK+MATCH+FeMININE+&results=1', 'https://www.equipetonclub.fr/accueil/725908035-offre-pack-match-adulte-striped-jersey.html?search_query=MATCHPUMA&results=23', 'https://www.equipetonclub.fr/accueil/725908043-offre-pack-match-adulte-rise-jersey.html?search_query=OFFRE+PACK+MATCH+ADULTE+RISE+JERSEY&results=1', 'https://www.equipetonclub.fr/accueil/725908044-offre-pack-match-enfant-rise-jersey.html?search_query=OFFRE+PACK+MATCH+ENFANT+RISE+JERSEY&results=1', 'https://www.equipetonclub.fr/simulateur3d/', 'https://www.equipetonclub.fr/accueil/725909070-offre-pack-entrainement-adulte-team-final-zip-top.html?search_query=ENTRAINEMENTPUMA&results=19', 'https://www.equipetonclub.fr/accueil/725909079-offre-pack-entrainement-team-rise-adulte-bronze.html?search_query=ENTRAINEMENTPUMA&results=19', 'https://www.equipetonclub.fr/accueil/725909069-offre-pack-match-enfant-gardien-pacer.html?search_query=MATCHPUMA&results=14', 'https://www.equipetonclub.fr/accueil/725909078-offre-ballon-orbita-6-ms-taille-3-4-et-5.html?search_query=ballonpuma&results=6', 'https://www.equipetonclub.fr/#homefeatured', 'https://www.equipetonclub.fr/#blockbestsellers', 'https://www.equipetonclub.fr/accueil/725908043-offre-pack-match-adulte-rise-jersey.html', 'https://www.equipetonclub.fr/accueil/725908057-offre-pack-sortie-liga-adulte.html', 'https://www.equipetonclub.fr/accueil/725908055-offre-pack-entrainement-adulte-liga-argent.html', 'https://www.equipetonclub.fr/accueil/725909016-offre-ballon-orbita-5-hs-taille-4-et-5.html', 'https://www.equipetonclub.fr/accueil/725908394-boutique-teamrise-jersey-adulte.html', 'https://www.equipetonclub.fr/materiels/725899367-10-coupelles-de-4-coloris.html', 'https://www.equipetonclub.fr/materiels/725899315-marquage-au-sol-de-1-a-5-.html', 'https://www.equipetonclub.fr/nous-contacter', 'https://www.equipetonclub.fr/content/24-guide-des-tailles-ensemble', 'https://www.equipetonclub.fr/content/23-entretenir-les-produits', 'https://www.equipetonclub.fr/content/14-personnalisation-des-produits', 'https://www.equipetonclub.fr/content/15-emplacement-des-zones-d-impression', 'https://www.equipetonclub.fr/content/16-couleurs-des-polices-imprimees', 'https://www.equipetonclub.fr/content/17-preparation-de-vos-fichiers', 'https://www.equipetonclub.fr/content/18-paiement-securise', 'https://www.equipetonclub.fr/content/19-livraison-et-suivi', 'https://www.equipetonclub.fr/content/20-garanties', 'https://www.equipetonclub.fr/content/21-retours-et-retractation', 'https://www.equipetonclub.fr/content/22-offre-pour-les-clubs', 'https://www.equipetonclub.fr/historique-commandes', 'https://www.equipetonclub.fr/avoirs', 'https://www.equipetonclub.fr/adresses', 'https://www.equipetonclub.fr/identite', 'https://www.equipetonclub.fr/reduction', 'https://www.equipetonclub.fr/content/2-mentions-legales', 'https://www.equipetonclub.fr/content/3-conditions-utilisation']
        },

        {
            'arr': ['https://www.equipetonclub.fr/114-pack?orderby=name&orderway=asc&orderway=asc', 'https://www.equipetonclub.fr/126-haut', 'https://www.equipetonclub.fr/130-bas', 'https://www.equipetonclub.fr/132-accessoires', 'https://www.equipetonclub.fr/119-Mailllot', 'https://www.equipetonclub.fr/120-Veste', 'https://www.equipetonclub.fr/129-Sweat', 'https://www.equipetonclub.fr/122-Polo', 'https://www.equipetonclub.fr/127-Parka', 'https://www.equipetonclub.fr/128-Coupe-vent', 'https://www.equipetonclub.fr/140-Tenues-De-Compression', 'https://www.equipetonclub.fr/121-Shorts', 'https://www.equipetonclub.fr/123-Pantalon', 'https://www.equipetonclub.fr/131-Chaussettes', 'https://www.equipetonclub.fr/133-Bonnet', 'https://www.equipetonclub.fr/134-Gants', 'https://www.equipetonclub.fr/118-Sac', 'https://www.equipetonclub.fr/117-ballons', 'https://www.equipetonclub.fr/135-Chasubles', 'https://www.equipetonclub.fr/89-materiel?orderby=name&orderway=asc', 'https://www.equipetonclub.fr/92-Entrainement', 'https://www.equipetonclub.fr/93-Entretien-Equipement-Terrain', 'https://www.equipetonclub.fr/94-Soins', 'https://www.equipetonclub.fr/95-Arbitre-Dirigeant', 'https://www.equipetonclub.fr/96-Outils-Du-Coach', 'https://www.equipetonclub.fr/117-ballons?orderby=name&orderway=asc', 'https://www.equipetonclub.fr/boutique-club', 'https://www.equipetonclub.fr/119-mailot-puma-collection-2021', 'https://www.equipetonclub.fr/120-veste-puma-collection-2021', 'https://www.equipetonclub.fr/122-polo-puma-collection-2021', 'https://www.equipetonclub.fr/121-short-puma-collection-2021', 'https://www.equipetonclub.fr/123-pantalon-puma-collection-2021', 'https://www.equipetonclub.fr/118-sac-puma-collection-2021', 'https://www.equipetonclub.fr/92-entrainement', 'https://www.equipetonclub.fr/93-entretien-equipement-terrain', 'https://www.equipetonclub.fr/94-soins', 'https://www.equipetonclub.fr/95-arbitre-dirigeant', 'https://www.equipetonclub.fr/96-outils-du-coach', 'https://www.equipetonclub.fr/mon-compte', 'https://www.equipetonclub.fr/commande', 'https://www.equipetonclub.fr/89-Materiels#categories-entrainement', 'https://www.equipetonclub.fr/89-Materiels#categories-entretien_equipement_terrain', 'https://www.equipetonclub.fr/89-Materiels#categories-soins', 'https://www.equipetonclub.fr/89-Materiels#categories-arbitre_dirigeant', 'https://www.equipetonclub.fr/89-Materiels#categories-outils_du_coach', 'https://www.equipetonclub.fr/89-Materiels#couleur-gris', 'https://www.equipetonclub.fr/89-Materiels#couleur-marine', 'https://www.equipetonclub.fr/89-Materiels#couleur-noir', 'https://www.equipetonclub.fr/89-Materiels#couleur-rouge', 'https://www.equipetonclub.fr/89-Materiels#couleur-vert', 'https://www.equipetonclub.fr/89-Materiels#brand-jako', 'https://www.equipetonclub.fr/89-Materiels#brand-puma', 'https://www.equipetonclub.fr/89-Materiels#genre-adulte', 'https://www.equipetonclub.fr/89-Materiels#sports-football', 'https://www.equipetonclub.fr/materiels/725899367-10-coupelles-de-4-coloris.html', 'https://www.equipetonclub.fr/materiels/725899351-25-plifix-enfoncoir.html', 'https://www.equipetonclub.fr/materiels/725899327-aiguille-culot-americain-par-12.html', 'https://www.equipetonclub.fr/materiels/725899391-aiguille-de-gonflage-blister-de-3.html', 'https://www.equipetonclub.fr/materiels/725899445-bande-adhesive-elastique-6-cm.html', 'https://www.equipetonclub.fr/materiels/725899447-bande-de-kinesiologie.html', 'https://www.equipetonclub.fr/materiels/725899446-bande-mousse-20-m-x-75-cm.html', 'https://www.equipetonclub.fr/materiels/725899430-bloc-de-changement-de-joueurs.html', 'https://www.equipetonclub.fr/materiels/725899369-bouclier-de-rugby-adulte.html', 'https://www.equipetonclub.fr/materiels/725899368-bouclier-de-rugby-enfant.html', 'https://www.equipetonclub.fr/materiels/725899353-bouclier-gardien-handball.html', 'https://www.equipetonclub.fr/materiels/725899342-bouteille.html', 'https://www.equipetonclub.fr/materiels/725899372-bouteille-hygienique-1l.html', 'https://www.equipetonclub.fr/materiels/725899431-brassard-capitaine-junior.html', 'https://www.equipetonclub.fr/materiels/725899432-brassard-capitaine-senior.html', 'https://www.equipetonclub.fr/materiels/725899314-but-de-basket-de-165m-a-220m-.html', 'https://www.equipetonclub.fr/materiels/725899364-but-de-basket-de-165m-a-220m-.html', 'https://www.equipetonclub.fr/materiels/725899373-but-de-basket-de-165m-a-220m-.html', 'https://www.equipetonclub.fr/materiels/725899328-carnet-tactique-basket-ball.html', 'https://www.equipetonclub.fr/materiels/725899357-carnet-tactique-handball.html', 'https://www.equipetonclub.fr/materiels/725899441-carton-darbitre-lot-de-5.html', 'https://www.equipetonclub.fr/materiels/725899337-cerceau.html', 'https://www.equipetonclub.fr/materiels/725899320-cerceau-40cm-de-diametre-en-polypropylene.html', 'https://www.equipetonclub.fr/materiels/725899321-cerceau-60cm-de-diametre-en-polypropylene.html', 'https://www.equipetonclub.fr/materiels/725899423-cerceau-hexagonal.html', 'https://www.equipetonclub.fr/materiels/725899363-cerceau-petanque-lot-de-6.html', 'https://www.equipetonclub.fr/materiels/725899325-cercle-de-basket.html', 'https://www.equipetonclub.fr/materiels/725899375-changement-de-joueurs-de-1-a-20.html', 'https://www.equipetonclub.fr/accueil/725908980-chasuble-ajouree-numerotee-de-16-a-20.html', 'https://www.equipetonclub.fr/materiels/725899318-chasuble-ajouree-reversible-.html', 'https://www.equipetonclub.fr/accueil/725908981-chasuble-ajouree-reversible.html', 'https://www.equipetonclub.fr/materiels/725899317-chasuble-ajouree-simple.html', 'https://www.equipetonclub.fr/accueil/725907968-chasubles-puma.html', 'https://www.equipetonclub.fr/materiels/725899451-chlorhexidine-lot-de-10compresses.html', 'https://www.equipetonclub.fr/materiels/725899452-chlorhexidine-spray-100-ml.html', 'https://www.equipetonclub.fr/materiels/725899329-chronometre.html', 'https://www.equipetonclub.fr/materiels/725899392-chronometre.html', 'https://www.equipetonclub.fr/materiels/725899398-cible-football-a-7.html', 'https://www.equipetonclub.fr/materiels/725899354-clible-but-handball.html', 'https://www.equipetonclub.fr/materiels/725899380-collecteur-de-cone-en420-s.html', 'https://www.equipetonclub.fr/materiels/725899349-compresse-de-froid-par-12.html', 'https://www.equipetonclub.fr/materiels/725899450-compresse-reutilisable-chaudfroid-10-x-26-cm.html', 'https://www.equipetonclub.fr/materiels/725899326-compresseur-a-membrane-avec-mesureur-de-pression-et-aiguille.html', 'https://www.equipetonclub.fr/materiels/725899384-cone-12-trous-avec-encoche.html', 'https://www.equipetonclub.fr/materiels/725899383-cone-12-trous-encoche.html', 'https://www.equipetonclub.fr/materiels/725899333-cone-a-trous-avec-encoche-pour-cerceau-plat-et-jalon.html', 'https://www.equipetonclub.fr/materiels/725899332-cone-classique-en-pvc.html', 'https://www.equipetonclub.fr/materiels/725899319-cone-souple-18-cm-190-grammes.html', 'https://www.equipetonclub.fr/materiels/725899415-corde-a-sauter-245-m-junior.html', 'https://www.equipetonclub.fr/materiels/725899433-crayon-darbitre-les-6.html', 'https://www.equipetonclub.fr/materiels/725899454-creme-chauffante-a-larnica.html', 'https://www.equipetonclub.fr/materiels/725899338-echelle-de-rythme.html', 'https://www.equipetonclub.fr/materiels/725899405-echelle-de-rythme-en-croix-4-x-4-m.html', 'https://www.equipetonclub.fr/materiels/725899339-echelle-double.html', 'https://www.equipetonclub.fr/materiels/725899388-embase-avec-bouchon.html', 'https://www.equipetonclub.fr/materiels/725899323-filet-basket-nylon-tresse-4mm-de-diametre.html', 'https://www.equipetonclub.fr/materiels/725899324-filet-basket-polypropylene-tresse-a-franges-6mm-de-diametre.html', 'https://www.equipetonclub.fr/materiels/725899360-filet-but-2mm-maille-double.html', 'https://www.equipetonclub.fr/materiels/725899409-filet-football-11-joueurs-2mm-md.html', 'https://www.equipetonclub.fr/materiels/725899408-filet-football-11-joueurs-2mm-ms.html', 'https://www.equipetonclub.fr/materiels/725899410-filet-football-11-joueurs-4mm-ms.html', 'https://www.equipetonclub.fr/materiels/725899411-filet-football-8-joueurs-2mm-ms.html', 'https://www.equipetonclub.fr/materiels/725899412-filet-football-europeen-11-joueurs-4-mm-ms-145-mm.html', 'https://www.equipetonclub.fr/materiels/725899414-filet-football-nid-dabeille-europeen-blanc.html', 'https://www.equipetonclub.fr/materiels/725899413-filet-football-pour-but-rabattable-2-mm-md.html', 'https://www.equipetonclub.fr/materiels/725899417-filet-pour-8-a-10-ballons.html', 'https://www.equipetonclub.fr/materiels/725899407-filet-transportable-11-joueurs.html', 'https://www.equipetonclub.fr/materiels/725899406-filet-transportable-7-joueurs.html', 'https://www.equipetonclub.fr/materiels/725899378-filet-volley-polyethylene-cable.html', 'https://www.equipetonclub.fr/materiels/725899453-gel-de-massage-chauffant-500-ml.html', 'https://www.equipetonclub.fr/materiels/725899335-haie-15cm.html', 'https://www.equipetonclub.fr/materiels/725899336-haie-30cm.html', 'https://www.equipetonclub.fr/materiels/725899322-hands-on-basket-.html', 'https://www.equipetonclub.fr/materiels/725899404-harnais-de-resistance-double.html', 'https://www.equipetonclub.fr/materiels/725899449-huile-camphree-500-ml.html', 'https://www.equipetonclub.fr/materiels/725899434-jeton-pile-ou-face-par-5.html', 'https://www.equipetonclub.fr/materiels/725899390-kit-corner-articule-fluo.html', 'https://www.equipetonclub.fr/materiels/725899422-kit-dentrainement-avec-14-jalons-10-cones-et-6-pinces.html', 'https://www.equipetonclub.fr/materiels/725899419-kit-dentrainement-avec-plot-dur-et-leger.html', 'https://www.equipetonclub.fr/materiels/725899393-kit-de-delimitation-40-soucoupes.html', 'https://www.equipetonclub.fr/materiels/725899425-kit-perfect-soccer-juggle.html', 'https://www.equipetonclub.fr/materiels/725899331-kits-de-delimitation.html', 'https://www.equipetonclub.fr/materiels/725899334-lot-de-10-cones-5-jalons.html', 'https://www.equipetonclub.fr/accueil/725907984-lot-de-12-sprays-desinfectant-surfaces.html', 'https://www.equipetonclub.fr/accueil/725907981-lot-de-24-sprays-a-percussion-pulverisation-dynamique-petite-piece-et-vehicules-50ml.html', 'https://www.equipetonclub.fr/accueil/725907982-lot-de-24-sprays-a-percussion-125ml-pulverisation-dynamique-pour-surface-jusqu-a-60m2.html', 'https://www.equipetonclub.fr/accueil/725907983-lot-de-24-sprays-hydro-alcoolique-actiff.html', 'https://www.equipetonclub.fr/materiels/725899394-lot-de-5-aimants-pour-en204129.html', 'https://www.equipetonclub.fr/materiels/725899316-lunette-de-jeu-.html', 'https://www.equipetonclub.fr/materiels/725899438-malette-arbitre-medium-avec-montre.html', 'https://www.equipetonclub.fr/materiels/725899428-mallette-20-chronos-chro14.html', 'https://www.equipetonclub.fr/materiels/725899402-mannequin-180-m.html', 'https://www.equipetonclub.fr/materiels/725899424-mannequin-gonflable.html', 'https://www.equipetonclub.fr/materiels/725899315-marquage-au-sol-de-1-a-5-.html', 'https://www.equipetonclub.fr/materiels/725899416-medecine-ball-souple-2-kg.html', 'https://www.equipetonclub.fr/materiels/725899341-mini-but-pro.html', 'https://www.equipetonclub.fr/materiels/725899420-mini-haie-de-saut-45-cm.html', 'https://www.equipetonclub.fr/materiels/725899347-mini-set-arbitrage.html', 'https://www.equipetonclub.fr/materiels/725899358-mini-set-arbitrage.html', 'https://www.equipetonclub.fr/materiels/725899439-montre-arbitre.html', 'https://www.equipetonclub.fr/materiels/725899440-montre-arbitre-casio.html', 'https://www.equipetonclub.fr/materiels/725899346-paire-de-drapeaux-de-touches.html', 'https://www.equipetonclub.fr/materiels/725899350-pansement-a-decouper.html', 'https://www.equipetonclub.fr/materiels/725899401-parachute.html', 'https://www.equipetonclub.fr/materiels/725899340-piquet-de-slalom.html', 'https://www.equipetonclub.fr/materiels/725899381-piquet-de-slalom-3-trous-terrain-synthetique.html', 'https://www.equipetonclub.fr/materiels/725899399-planche-a-rebond.html', 'https://www.equipetonclub.fr/materiels/725899374-plaquette-effacable-terrain.html', 'https://www.equipetonclub.fr/materiels/725899344-plaquette-football.html', 'https://www.equipetonclub.fr/materiels/725899418-plaquette-rectoverso-football.html', 'https://www.equipetonclub.fr/materiels/725899435-pochette-arbitre-petit-modele.html', 'https://www.equipetonclub.fr/materiels/725899444-pochette-arbitre-hand-petit-modele.html', 'https://www.equipetonclub.fr/materiels/725899343-porte-6-bouteilles.html', 'https://www.equipetonclub.fr/materiels/725899362-porte-8-bouteilles.html', 'https://www.equipetonclub.fr/materiels/725899379-porte-filet.html', 'https://www.equipetonclub.fr/materiels/725899389-poteau-corner-articule-seul.html', 'https://www.equipetonclub.fr/materiels/725899387-poteaux-de-corner-avec-articulation-integre.html', 'https://www.equipetonclub.fr/materiels/725899371-protection-de-poteau.html', 'https://www.equipetonclub.fr/materiels/725899356-protege-dents.html', 'https://www.equipetonclub.fr/accueil/725907967-puma-captains-armbands.html', 'https://www.equipetonclub.fr/accueil/725907966-puma-liga-cap.html', 'https://www.equipetonclub.fr/materiels/725899355-resine-blanche-select-100ml.html', 'https://www.equipetonclub.fr/materiels/725899459-sac-banane-soigneur.html', 'https://www.equipetonclub.fr/materiels/725899421-sac-de-musculation-capacite-15-kg.html', 'https://www.equipetonclub.fr/materiels/725899352-sac-expert-garni.html', 'https://www.equipetonclub.fr/materiels/725899330-sac-mid-garni-.html', 'https://www.equipetonclub.fr/materiels/725899458-sac-soigneur-eco.html', 'https://www.equipetonclub.fr/materiels/725899376-scorer.html', 'https://www.equipetonclub.fr/materiels/725899442-sifflet-fox-40-sonik-avec-embout.html', 'https://www.equipetonclub.fr/materiels/725899443-sifflet-fox-sharx.html', 'https://www.equipetonclub.fr/materiels/725899345-sifflet-plastique.html', 'https://www.equipetonclub.fr/materiels/725899456-sparadrap-lot-de-6.html', 'https://www.equipetonclub.fr/materiels/725899455-sparadrap-strapping-10-m-x-25cm.html', 'https://www.equipetonclub.fr/materiels/725899436-spray-arbitre-150-ml.html', 'https://www.equipetonclub.fr/materiels/725899348-spray-de-froid-400ml.html', 'https://www.equipetonclub.fr/materiels/725899448-spray-de-froid-a-larnica.html', 'https://www.equipetonclub.fr/materiels/725899385-spray-repare-ballons.html', 'https://www.equipetonclub.fr/materiels/725899377-strap-doigt-38cm-largeur.html', 'https://www.equipetonclub.fr/materiels/725899396-support-de-transport-pour-en-201.html', 'https://www.equipetonclub.fr/materiels/725899400-support-pour-planche-a-rebond-en288.html', 'https://www.equipetonclub.fr/materiels/725899437-support-spray-arbitre-avec-clip.html', 'https://www.equipetonclub.fr/materiels/725899403-tableau-effacable-taktifol-football.html', 'https://www.equipetonclub.fr/materiels/725899395-tableau-magnetique-football-90-x-60-cm.html', 'https://www.equipetonclub.fr/materiels/725899429-tableau-magnetique-et-effacable-football-60-x-80-cm.html', 'https://www.equipetonclub.fr/materiels/725899426-tchoukball-1-x-1-m-inclinaison-2545.html', 'https://www.equipetonclub.fr/materiels/725899370-tee-de-rugby-avec-ergots.html', 'https://www.equipetonclub.fr/materiels/725899359-temps-mort-par-3.html', 'https://www.equipetonclub.fr/materiels/725899397-tennis-ballon.html', 'https://www.equipetonclub.fr/materiels/725899224-trousse-de-toilette-striker-adulte.html', 'https://www.equipetonclub.fr/materiels/725899457-vessie-a-glace.html', 'https://www.equipetonclub.fr/materiels/725899361-wizzball.html', 'https://www.equipetonclub.fr/accueil/725907034-teamgoal-training-14-zip-top-pour-homme.html', 'https://www.equipetonclub.fr/accueil/725907063-teamgoal-training-14-zip-top-pour-enfant.html', 'https://www.equipetonclub.fr/accueil/725907854-team-rise-training-14-zip-top-pour-homme.html', 'https://www.equipetonclub.fr/accueil/725907928-teamliga-14-zip-top-pour-femme.html', 'https://www.equipetonclub.fr/accueil/725907855-team-rise-training-14-zip-top-pour-enfant.html', 'https://www.equipetonclub.fr/accueil/725908996-teamfinal-training-14-zip-top.html', 'https://www.equipetonclub.fr/accueil/725910293-team-liga-training-14-zip-top-pour-homme.html', 'https://www.equipetonclub.fr/accueil/725910294-team-liga-training-14-zip-top-pour-enfant.html', 'https://www.equipetonclub.fr/accueil/725907946-puma-bench-jacket-pour-homme.html', 'https://www.equipetonclub.fr/accueil/725908994-teamliga-hybrid-jacket.html', 'https://www.equipetonclub.fr/accueil/725907948-teamliga-padded-jacket-pour-homme.html', 'https://www.equipetonclub.fr/accueil/725907949-teamliga-padded-jacket-pour-enfant.html', 'https://www.equipetonclub.fr/accueil/725910295-puma-bench-jacket-pour-enfant.html', 'https://www.equipetonclub.fr/accueil/725910296-teamliga-vest-jacket.html']
        },

        {
            'arr': ['https://www.equipetonclub.fr/content/4-a-propos', 'https://www.instagram.com/equipetonclub.fr', 'https://www.facebook.com/Equipetonclub', 'https://www.pinterest.fr/myteamfoot', 'https://twitter.com/myteamfoot_fr', 'https://www.equipetonclub.fr/#', 'https://www.equipetonclub.fr/', 'https://www.equipetonclub.fr/simulateur3d', 'https://www.equipetonclub.fr/114-pack?orderby=name&orderway=asc&orderway=asc', 'https://www.equipetonclub.fr/126-haut', 'https://www.equipetonclub.fr/130-bas', 'https://www.equipetonclub.fr/132-accessoires', 'https://www.equipetonclub.fr/119-Mailllot', 'https://www.equipetonclub.fr/120-Veste', 'https://www.equipetonclub.fr/129-Sweat', 'https://www.equipetonclub.fr/122-Polo', 'https://www.equipetonclub.fr/127-Parka', 'https://www.equipetonclub.fr/128-Coupe-vent', 'https://www.equipetonclub.fr/140-Tenues-De-Compression', 'https://www.equipetonclub.fr/121-Shorts', 'https://www.equipetonclub.fr/123-Pantalon', 'https://www.equipetonclub.fr/131-Chaussettes', 'https://www.equipetonclub.fr/133-Bonnet', 'https://www.equipetonclub.fr/134-Gants', 'https://www.equipetonclub.fr/118-Sac', 'https://www.equipetonclub.fr/117-ballons', 'https://www.equipetonclub.fr/135-Chasubles', 'https://www.equipetonclub.fr/89-materiel?orderby=name&orderway=asc', 'https://www.equipetonclub.fr/92-Entrainement', 'https://www.equipetonclub.fr/93-Entretien-Equipement-Terrain', 'https://www.equipetonclub.fr/94-Soins', 'https://www.equipetonclub.fr/95-Arbitre-Dirigeant', 'https://www.equipetonclub.fr/96-Outils-Du-Coach', 'https://www.equipetonclub.fr/117-ballons?orderby=name&orderway=asc', 'https://www.equipetonclub.fr/boutique-club', 'https://www.equipetonclub.fr/119-mailot-puma-collection-2021', 'https://www.equipetonclub.fr/120-veste-puma-collection-2021', 'https://www.equipetonclub.fr/122-polo-puma-collection-2021', 'https://www.equipetonclub.fr/121-short-puma-collection-2021', 'https://www.equipetonclub.fr/123-pantalon-puma-collection-2021', 'https://www.equipetonclub.fr/118-sac-puma-collection-2021', 'https://www.equipetonclub.fr/92-entrainement', 'https://www.equipetonclub.fr/93-entretien-equipement-terrain', 'https://www.equipetonclub.fr/94-soins', 'https://www.equipetonclub.fr/95-arbitre-dirigeant', 'https://www.equipetonclub.fr/96-outils-du-coach', 'https://www.equipetonclub.fr/mon-compte', 'https://www.equipetonclub.fr/commande', 'https://www.equipetonclub.fr/recherche?controller=search&orderby=position&orderway=desc&search_query=enfant&submit_search=', 'https://www.equipetonclub.fr/recherche?controller=search&orderby=position&orderway=desc&search_query=ballonpuma&submit_search=', 'https://www.equipetonclub.fr/recherche?controller=search&orderby=position&orderway=desc&search_query=FEMININEPUMA&submit_search=', 'https://www.equipetonclub.fr/recherche?controller=search&orderby=position&orderway=desc&search_query=LIFESTYLEPUMA&submit_search=', 'https://www.equipetonclub.fr/accueil/725908049-offre-pack-entrainement-adulte-cup-jersey-bronze.html?search_query=OFFRE+PACK+ENTRAINEMENT+ADULTE+CUP+JERSEY+BRONZE&results=1', 'https://www.equipetonclub.fr/accueil/725907137-offre-pack-match-feminine.html?search_query=OFFRE+PACK+MATCH+FeMININE+&results=1', 'https://www.equipetonclub.fr/accueil/725908035-offre-pack-match-adulte-striped-jersey.html?search_query=MATCHPUMA&results=23', 'https://www.equipetonclub.fr/accueil/725908043-offre-pack-match-adulte-rise-jersey.html?search_query=OFFRE+PACK+MATCH+ADULTE+RISE+JERSEY&results=1', 'https://www.equipetonclub.fr/accueil/725908044-offre-pack-match-enfant-rise-jersey.html?search_query=OFFRE+PACK+MATCH+ENFANT+RISE+JERSEY&results=1', 'https://www.equipetonclub.fr/simulateur3d/', 'https://www.equipetonclub.fr/accueil/725909070-offre-pack-entrainement-adulte-team-final-zip-top.html?search_query=ENTRAINEMENTPUMA&results=19', 'https://www.equipetonclub.fr/accueil/725909079-offre-pack-entrainement-team-rise-adulte-bronze.html?search_query=ENTRAINEMENTPUMA&results=19', 'https://www.equipetonclub.fr/accueil/725909069-offre-pack-match-enfant-gardien-pacer.html?search_query=MATCHPUMA&results=14', 'https://www.equipetonclub.fr/accueil/725909078-offre-ballon-orbita-6-ms-taille-3-4-et-5.html?search_query=ballonpuma&results=6', 'https://www.equipetonclub.fr/#homefeatured', 'https://www.equipetonclub.fr/#blockbestsellers', 'https://www.equipetonclub.fr/accueil/725908043-offre-pack-match-adulte-rise-jersey.html', 'https://www.equipetonclub.fr/accueil/725908057-offre-pack-sortie-liga-adulte.html', 'https://www.equipetonclub.fr/accueil/725908055-offre-pack-entrainement-adulte-liga-argent.html', 'https://www.equipetonclub.fr/accueil/725909016-offre-ballon-orbita-5-hs-taille-4-et-5.html', 'https://www.equipetonclub.fr/accueil/725908394-boutique-teamrise-jersey-adulte.html', 'https://www.equipetonclub.fr/materiels/725899367-10-coupelles-de-4-coloris.html', 'https://www.equipetonclub.fr/materiels/725899315-marquage-au-sol-de-1-a-5-.html', 'https://www.equipetonclub.fr/nous-contacter', 'https://www.equipetonclub.fr/content/24-guide-des-tailles-ensemble', 'https://www.equipetonclub.fr/content/23-entretenir-les-produits', 'https://www.equipetonclub.fr/content/14-personnalisation-des-produits', 'https://www.equipetonclub.fr/content/15-emplacement-des-zones-d-impression', 'https://www.equipetonclub.fr/content/16-couleurs-des-polices-imprimees', 'https://www.equipetonclub.fr/content/17-preparation-de-vos-fichiers', 'https://www.equipetonclub.fr/content/18-paiement-securise', 'https://www.equipetonclub.fr/content/19-livraison-et-suivi', 'https://www.equipetonclub.fr/content/20-garanties', 'https://www.equipetonclub.fr/content/21-retours-et-retractation', 'https://www.equipetonclub.fr/content/22-offre-pour-les-clubs', 'https://www.equipetonclub.fr/historique-commandes', 'https://www.equipetonclub.fr/avoirs', 'https://www.equipetonclub.fr/adresses', 'https://www.equipetonclub.fr/identite', 'https://www.equipetonclub.fr/reduction', 'https://www.equipetonclub.fr/content/2-mentions-legales', 'https://www.equipetonclub.fr/content/3-conditions-utilisation']
        },

        {
            'arr': ['https://www.equipetonclub.fr/114-pack?orderby=name&orderway=asc&orderway=asc',
                    'https://www.equipetonclub.fr/126-haut', 'https://www.equipetonclub.fr/130-bas',
                    'https://www.equipetonclub.fr/132-accessoires', 'https://www.equipetonclub.fr/119-Mailllot',
                    'https://www.equipetonclub.fr/120-Veste', 'https://www.equipetonclub.fr/129-Sweat',
                    'https://www.equipetonclub.fr/122-Polo', 'https://www.equipetonclub.fr/127-Parka',
                    'https://www.equipetonclub.fr/128-Coupe-vent',
                    'https://www.equipetonclub.fr/140-Tenues-De-Compression', 'https://www.equipetonclub.fr/121-Shorts',
                    'https://www.equipetonclub.fr/123-Pantalon', 'https://www.equipetonclub.fr/131-Chaussettes',
                    'https://www.equipetonclub.fr/133-Bonnet', 'https://www.equipetonclub.fr/134-Gants',
                    'https://www.equipetonclub.fr/118-Sac', 'https://www.equipetonclub.fr/117-ballons',
                    'https://www.equipetonclub.fr/135-Chasubles',
                    'https://www.equipetonclub.fr/89-materiel?orderby=name&orderway=asc',
                    'https://www.equipetonclub.fr/92-Entrainement',
                    'https://www.equipetonclub.fr/93-Entretien-Equipement-Terrain',
                    'https://www.equipetonclub.fr/94-Soins', 'https://www.equipetonclub.fr/95-Arbitre-Dirigeant',
                    'https://www.equipetonclub.fr/96-Outils-Du-Coach',
                    'https://www.equipetonclub.fr/117-ballons?orderby=name&orderway=asc',
                    'https://www.equipetonclub.fr/boutique-club',
                    'https://www.equipetonclub.fr/119-mailot-puma-collection-2021',
                    'https://www.equipetonclub.fr/120-veste-puma-collection-2021',
                    'https://www.equipetonclub.fr/122-polo-puma-collection-2021',
                    'https://www.equipetonclub.fr/121-short-puma-collection-2021',
                    'https://www.equipetonclub.fr/123-pantalon-puma-collection-2021',
                    'https://www.equipetonclub.fr/118-sac-puma-collection-2021',
                    'https://www.equipetonclub.fr/92-entrainement',
                    'https://www.equipetonclub.fr/93-entretien-equipement-terrain',
                    'https://www.equipetonclub.fr/94-soins', 'https://www.equipetonclub.fr/95-arbitre-dirigeant',
                    'https://www.equipetonclub.fr/96-outils-du-coach', 'https://www.equipetonclub.fr/mon-compte',
                    'https://www.equipetonclub.fr/commande',
                    'https://www.equipetonclub.fr/89-Materiels#categories-entrainement',
                    'https://www.equipetonclub.fr/89-Materiels#categories-entretien_equipement_terrain',
                    'https://www.equipetonclub.fr/89-Materiels#categories-soins',
                    'https://www.equipetonclub.fr/89-Materiels#categories-arbitre_dirigeant',
                    'https://www.equipetonclub.fr/89-Materiels#categories-outils_du_coach',
                    'https://www.equipetonclub.fr/89-Materiels#couleur-gris',
                    'https://www.equipetonclub.fr/89-Materiels#couleur-marine',
                    'https://www.equipetonclub.fr/89-Materiels#couleur-noir',
                    'https://www.equipetonclub.fr/89-Materiels#couleur-rouge',
                    'https://www.equipetonclub.fr/89-Materiels#couleur-vert',
                    'https://www.equipetonclub.fr/89-Materiels#brand-jako',
                    'https://www.equipetonclub.fr/89-Materiels#brand-puma',
                    'https://www.equipetonclub.fr/89-Materiels#genre-adulte',
                    'https://www.equipetonclub.fr/89-Materiels#sports-football',
                    'https://www.equipetonclub.fr/materiels/725899367-10-coupelles-de-4-coloris.html',
                    'https://www.equipetonclub.fr/materiels/725899351-25-plifix-enfoncoir.html',
                    'https://www.equipetonclub.fr/materiels/725899327-aiguille-culot-americain-par-12.html',
                    'https://www.equipetonclub.fr/materiels/725899391-aiguille-de-gonflage-blister-de-3.html',
                    'https://www.equipetonclub.fr/materiels/725899445-bande-adhesive-elastique-6-cm.html',
                    'https://www.equipetonclub.fr/materiels/725899447-bande-de-kinesiologie.html',
                    'https://www.equipetonclub.fr/materiels/725899446-bande-mousse-20-m-x-75-cm.html',
                    'https://www.equipetonclub.fr/materiels/725899430-bloc-de-changement-de-joueurs.html',
                    'https://www.equipetonclub.fr/materiels/725899369-bouclier-de-rugby-adulte.html',
                    'https://www.equipetonclub.fr/materiels/725899368-bouclier-de-rugby-enfant.html',
                    'https://www.equipetonclub.fr/materiels/725899353-bouclier-gardien-handball.html',
                    'https://www.equipetonclub.fr/materiels/725899342-bouteille.html',
                    'https://www.equipetonclub.fr/materiels/725899372-bouteille-hygienique-1l.html',
                    'https://www.equipetonclub.fr/materiels/725899431-brassard-capitaine-junior.html',
                    'https://www.equipetonclub.fr/materiels/725899432-brassard-capitaine-senior.html',
                    'https://www.equipetonclub.fr/materiels/725899314-but-de-basket-de-165m-a-220m-.html',
                    'https://www.equipetonclub.fr/materiels/725899364-but-de-basket-de-165m-a-220m-.html',
                    'https://www.equipetonclub.fr/materiels/725899373-but-de-basket-de-165m-a-220m-.html',
                    'https://www.equipetonclub.fr/materiels/725899328-carnet-tactique-basket-ball.html',
                    'https://www.equipetonclub.fr/materiels/725899357-carnet-tactique-handball.html',
                    'https://www.equipetonclub.fr/materiels/725899441-carton-darbitre-lot-de-5.html',
                    'https://www.equipetonclub.fr/materiels/725899337-cerceau.html',
                    'https://www.equipetonclub.fr/materiels/725899320-cerceau-40cm-de-diametre-en-polypropylene.html',
                    'https://www.equipetonclub.fr/materiels/725899321-cerceau-60cm-de-diametre-en-polypropylene.html',
                    'https://www.equipetonclub.fr/materiels/725899423-cerceau-hexagonal.html',
                    'https://www.equipetonclub.fr/materiels/725899363-cerceau-petanque-lot-de-6.html',
                    'https://www.equipetonclub.fr/materiels/725899325-cercle-de-basket.html',
                    'https://www.equipetonclub.fr/materiels/725899375-changement-de-joueurs-de-1-a-20.html',
                    'https://www.equipetonclub.fr/accueil/725908980-chasuble-ajouree-numerotee-de-16-a-20.html',
                    'https://www.equipetonclub.fr/materiels/725899318-chasuble-ajouree-reversible-.html',
                    'https://www.equipetonclub.fr/accueil/725908981-chasuble-ajouree-reversible.html',
                    'https://www.equipetonclub.fr/materiels/725899317-chasuble-ajouree-simple.html',
                    'https://www.equipetonclub.fr/accueil/725907968-chasubles-puma.html',
                    'https://www.equipetonclub.fr/materiels/725899451-chlorhexidine-lot-de-10compresses.html',
                    'https://www.equipetonclub.fr/materiels/725899452-chlorhexidine-spray-100-ml.html',
                    'https://www.equipetonclub.fr/materiels/725899329-chronometre.html',
                    'https://www.equipetonclub.fr/materiels/725899392-chronometre.html',
                    'https://www.equipetonclub.fr/materiels/725899398-cible-football-a-7.html',
                    'https://www.equipetonclub.fr/materiels/725899354-clible-but-handball.html',
                    'https://www.equipetonclub.fr/materiels/725899380-collecteur-de-cone-en420-s.html',
                    'https://www.equipetonclub.fr/materiels/725899349-compresse-de-froid-par-12.html',
                    'https://www.equipetonclub.fr/materiels/725899450-compresse-reutilisable-chaudfroid-10-x-26-cm.html',
                    'https://www.equipetonclub.fr/materiels/725899326-compresseur-a-membrane-avec-mesureur-de-pression-et-aiguille.html',
                    'https://www.equipetonclub.fr/materiels/725899384-cone-12-trous-avec-encoche.html',
                    'https://www.equipetonclub.fr/materiels/725899383-cone-12-trous-encoche.html',
                    'https://www.equipetonclub.fr/materiels/725899333-cone-a-trous-avec-encoche-pour-cerceau-plat-et-jalon.html',
                    'https://www.equipetonclub.fr/materiels/725899332-cone-classique-en-pvc.html',
                    'https://www.equipetonclub.fr/materiels/725899319-cone-souple-18-cm-190-grammes.html',
                    'https://www.equipetonclub.fr/materiels/725899415-corde-a-sauter-245-m-junior.html',
                    'https://www.equipetonclub.fr/materiels/725899433-crayon-darbitre-les-6.html',
                    'https://www.equipetonclub.fr/materiels/725899454-creme-chauffante-a-larnica.html',
                    'https://www.equipetonclub.fr/materiels/725899338-echelle-de-rythme.html',
                    'https://www.equipetonclub.fr/materiels/725899405-echelle-de-rythme-en-croix-4-x-4-m.html',
                    'https://www.equipetonclub.fr/materiels/725899339-echelle-double.html',
                    'https://www.equipetonclub.fr/materiels/725899388-embase-avec-bouchon.html',
                    'https://www.equipetonclub.fr/materiels/725899323-filet-basket-nylon-tresse-4mm-de-diametre.html',
                    'https://www.equipetonclub.fr/materiels/725899324-filet-basket-polypropylene-tresse-a-franges-6mm-de-diametre.html',
                    'https://www.equipetonclub.fr/materiels/725899360-filet-but-2mm-maille-double.html',
                    'https://www.equipetonclub.fr/materiels/725899409-filet-football-11-joueurs-2mm-md.html',
                    'https://www.equipetonclub.fr/materiels/725899408-filet-football-11-joueurs-2mm-ms.html',
                    'https://www.equipetonclub.fr/materiels/725899410-filet-football-11-joueurs-4mm-ms.html',
                    'https://www.equipetonclub.fr/materiels/725899411-filet-football-8-joueurs-2mm-ms.html',
                    'https://www.equipetonclub.fr/materiels/725899412-filet-football-europeen-11-joueurs-4-mm-ms-145-mm.html',
                    'https://www.equipetonclub.fr/materiels/725899414-filet-football-nid-dabeille-europeen-blanc.html',
                    'https://www.equipetonclub.fr/materiels/725899413-filet-football-pour-but-rabattable-2-mm-md.html',
                    'https://www.equipetonclub.fr/materiels/725899417-filet-pour-8-a-10-ballons.html',
                    'https://www.equipetonclub.fr/materiels/725899407-filet-transportable-11-joueurs.html',
                    'https://www.equipetonclub.fr/materiels/725899406-filet-transportable-7-joueurs.html',
                    'https://www.equipetonclub.fr/materiels/725899378-filet-volley-polyethylene-cable.html',
                    'https://www.equipetonclub.fr/materiels/725899453-gel-de-massage-chauffant-500-ml.html',
                    'https://www.equipetonclub.fr/materiels/725899335-haie-15cm.html',
                    'https://www.equipetonclub.fr/materiels/725899336-haie-30cm.html',
                    'https://www.equipetonclub.fr/materiels/725899322-hands-on-basket-.html',
                    'https://www.equipetonclub.fr/materiels/725899404-harnais-de-resistance-double.html',
                    'https://www.equipetonclub.fr/materiels/725899449-huile-camphree-500-ml.html',
                    'https://www.equipetonclub.fr/materiels/725899434-jeton-pile-ou-face-par-5.html',
                    'https://www.equipetonclub.fr/materiels/725899390-kit-corner-articule-fluo.html',
                    'https://www.equipetonclub.fr/materiels/725899422-kit-dentrainement-avec-14-jalons-10-cones-et-6-pinces.html',
                    'https://www.equipetonclub.fr/materiels/725899419-kit-dentrainement-avec-plot-dur-et-leger.html',
                    'https://www.equipetonclub.fr/materiels/725899393-kit-de-delimitation-40-soucoupes.html',
                    'https://www.equipetonclub.fr/materiels/725899425-kit-perfect-soccer-juggle.html',
                    'https://www.equipetonclub.fr/materiels/725899331-kits-de-delimitation.html',
                    'https://www.equipetonclub.fr/materiels/725899334-lot-de-10-cones-5-jalons.html',
                    'https://www.equipetonclub.fr/accueil/725907984-lot-de-12-sprays-desinfectant-surfaces.html',
                    'https://www.equipetonclub.fr/accueil/725907981-lot-de-24-sprays-a-percussion-pulverisation-dynamique-petite-piece-et-vehicules-50ml.html',
                    'https://www.equipetonclub.fr/accueil/725907982-lot-de-24-sprays-a-percussion-125ml-pulverisation-dynamique-pour-surface-jusqu-a-60m2.html',
                    'https://www.equipetonclub.fr/accueil/725907983-lot-de-24-sprays-hydro-alcoolique-actiff.html',
                    'https://www.equipetonclub.fr/materiels/725899394-lot-de-5-aimants-pour-en204129.html',
                    'https://www.equipetonclub.fr/materiels/725899316-lunette-de-jeu-.html',
                    'https://www.equipetonclub.fr/materiels/725899438-malette-arbitre-medium-avec-montre.html',
                    'https://www.equipetonclub.fr/materiels/725899428-mallette-20-chronos-chro14.html',
                    'https://www.equipetonclub.fr/materiels/725899402-mannequin-180-m.html',
                    'https://www.equipetonclub.fr/materiels/725899424-mannequin-gonflable.html',
                    'https://www.equipetonclub.fr/materiels/725899315-marquage-au-sol-de-1-a-5-.html',
                    'https://www.equipetonclub.fr/materiels/725899416-medecine-ball-souple-2-kg.html',
                    'https://www.equipetonclub.fr/materiels/725899341-mini-but-pro.html',
                    'https://www.equipetonclub.fr/materiels/725899420-mini-haie-de-saut-45-cm.html',
                    'https://www.equipetonclub.fr/materiels/725899347-mini-set-arbitrage.html',
                    'https://www.equipetonclub.fr/materiels/725899358-mini-set-arbitrage.html',
                    'https://www.equipetonclub.fr/materiels/725899439-montre-arbitre.html',
                    'https://www.equipetonclub.fr/materiels/725899440-montre-arbitre-casio.html',
                    'https://www.equipetonclub.fr/materiels/725899346-paire-de-drapeaux-de-touches.html',
                    'https://www.equipetonclub.fr/materiels/725899350-pansement-a-decouper.html',
                    'https://www.equipetonclub.fr/materiels/725899401-parachute.html',
                    'https://www.equipetonclub.fr/materiels/725899340-piquet-de-slalom.html',
                    'https://www.equipetonclub.fr/materiels/725899381-piquet-de-slalom-3-trous-terrain-synthetique.html',
                    'https://www.equipetonclub.fr/materiels/725899399-planche-a-rebond.html',
                    'https://www.equipetonclub.fr/materiels/725899374-plaquette-effacable-terrain.html',
                    'https://www.equipetonclub.fr/materiels/725899344-plaquette-football.html',
                    'https://www.equipetonclub.fr/materiels/725899418-plaquette-rectoverso-football.html',
                    'https://www.equipetonclub.fr/materiels/725899435-pochette-arbitre-petit-modele.html',
                    'https://www.equipetonclub.fr/materiels/725899444-pochette-arbitre-hand-petit-modele.html',
                    'https://www.equipetonclub.fr/materiels/725899343-porte-6-bouteilles.html',
                    'https://www.equipetonclub.fr/materiels/725899362-porte-8-bouteilles.html',
                    'https://www.equipetonclub.fr/materiels/725899379-porte-filet.html',
                    'https://www.equipetonclub.fr/materiels/725899389-poteau-corner-articule-seul.html',
                    'https://www.equipetonclub.fr/materiels/725899387-poteaux-de-corner-avec-articulation-integre.html',
                    'https://www.equipetonclub.fr/materiels/725899371-protection-de-poteau.html',
                    'https://www.equipetonclub.fr/materiels/725899356-protege-dents.html',
                    'https://www.equipetonclub.fr/accueil/725907967-puma-captains-armbands.html',
                    'https://www.equipetonclub.fr/accueil/725907966-puma-liga-cap.html',
                    'https://www.equipetonclub.fr/materiels/725899355-resine-blanche-select-100ml.html',
                    'https://www.equipetonclub.fr/materiels/725899459-sac-banane-soigneur.html',
                    'https://www.equipetonclub.fr/materiels/725899421-sac-de-musculation-capacite-15-kg.html',
                    'https://www.equipetonclub.fr/materiels/725899352-sac-expert-garni.html',
                    'https://www.equipetonclub.fr/materiels/725899330-sac-mid-garni-.html',
                    'https://www.equipetonclub.fr/materiels/725899458-sac-soigneur-eco.html',
                    'https://www.equipetonclub.fr/materiels/725899376-scorer.html',
                    'https://www.equipetonclub.fr/materiels/725899442-sifflet-fox-40-sonik-avec-embout.html',
                    'https://www.equipetonclub.fr/materiels/725899443-sifflet-fox-sharx.html',
                    'https://www.equipetonclub.fr/materiels/725899345-sifflet-plastique.html',
                    'https://www.equipetonclub.fr/materiels/725899456-sparadrap-lot-de-6.html',
                    'https://www.equipetonclub.fr/materiels/725899455-sparadrap-strapping-10-m-x-25cm.html',
                    'https://www.equipetonclub.fr/materiels/725899436-spray-arbitre-150-ml.html',
                    'https://www.equipetonclub.fr/materiels/725899348-spray-de-froid-400ml.html',
                    'https://www.equipetonclub.fr/materiels/725899448-spray-de-froid-a-larnica.html',
                    'https://www.equipetonclub.fr/materiels/725899385-spray-repare-ballons.html',
                    'https://www.equipetonclub.fr/materiels/725899377-strap-doigt-38cm-largeur.html',
                    'https://www.equipetonclub.fr/materiels/725899396-support-de-transport-pour-en-201.html',
                    'https://www.equipetonclub.fr/materiels/725899400-support-pour-planche-a-rebond-en288.html',
                    'https://www.equipetonclub.fr/materiels/725899437-support-spray-arbitre-avec-clip.html',
                    'https://www.equipetonclub.fr/materiels/725899403-tableau-effacable-taktifol-football.html',
                    'https://www.equipetonclub.fr/materiels/725899395-tableau-magnetique-football-90-x-60-cm.html',
                    'https://www.equipetonclub.fr/materiels/725899429-tableau-magnetique-et-effacable-football-60-x-80-cm.html',
                    'https://www.equipetonclub.fr/materiels/725899426-tchoukball-1-x-1-m-inclinaison-2545.html',
                    'https://www.equipetonclub.fr/materiels/725899370-tee-de-rugby-avec-ergots.html',
                    'https://www.equipetonclub.fr/materiels/725899359-temps-mort-par-3.html',
                    'https://www.equipetonclub.fr/materiels/725899397-tennis-ballon.html',
                    'https://www.equipetonclub.fr/materiels/725899224-trousse-de-toilette-striker-adulte.html',
                    'https://www.equipetonclub.fr/materiels/725899457-vessie-a-glace.html',
                    'https://www.equipetonclub.fr/materiels/725899361-wizzball.html',
                    'https://www.equipetonclub.fr/accueil/725907034-teamgoal-training-14-zip-top-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907063-teamgoal-training-14-zip-top-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907854-team-rise-training-14-zip-top-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907928-teamliga-14-zip-top-pour-femme.html',
                    'https://www.equipetonclub.fr/accueil/725907855-team-rise-training-14-zip-top-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725908996-teamfinal-training-14-zip-top.html',
                    'https://www.equipetonclub.fr/accueil/725910293-team-liga-training-14-zip-top-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725910294-team-liga-training-14-zip-top-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907946-puma-bench-jacket-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725908994-teamliga-hybrid-jacket.html',
                    'https://www.equipetonclub.fr/accueil/725907948-teamliga-padded-jacket-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907949-teamliga-padded-jacket-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725910295-puma-bench-jacket-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725910296-teamliga-vest-jacket.html']
        },

        {
            'arr': ['https://www.equipetonclub.fr/119-mailot-puma-collection-2021',
                    'https://www.equipetonclub.fr/120-veste-puma-collection-2021',
                    'https://www.equipetonclub.fr/122-polo-puma-collection-2021',
                    'https://www.equipetonclub.fr/121-short-puma-collection-2021',
                    'https://www.equipetonclub.fr/123-pantalon-puma-collection-2021',
                    'https://www.equipetonclub.fr/118-sac-puma-collection-2021',
                    'https://www.equipetonclub.fr/92-entrainement',
                    'https://www.equipetonclub.fr/93-entretien-equipement-terrain',
                    'https://www.equipetonclub.fr/94-soins', 'https://www.equipetonclub.fr/95-arbitre-dirigeant',
                    'https://www.equipetonclub.fr/96-outils-du-coach', 'https://www.equipetonclub.fr/mon-compte',
                    'https://www.equipetonclub.fr/commande',
                    'https://www.equipetonclub.fr/119-Mailllot#manches-manches_courtes',
                    'https://www.equipetonclub.fr/119-Mailllot#manches-manches_longues',
                    'https://www.equipetonclub.fr/119-Mailllot#genre-adulte',
                    'https://www.equipetonclub.fr/119-Mailllot#genre-enfant',
                    'https://www.equipetonclub.fr/119-Mailllot#genre-femme',
                    'https://www.equipetonclub.fr/119-Mailllot#genre-homme',
                    'https://www.equipetonclub.fr/119-Mailllot#couleur-blanc',
                    'https://www.equipetonclub.fr/119-Mailllot#couleur-ciel',
                    'https://www.equipetonclub.fr/119-Mailllot#couleur-jaune',
                    'https://www.equipetonclub.fr/119-Mailllot#couleur-marine',
                    'https://www.equipetonclub.fr/119-Mailllot#couleur-noir',
                    'https://www.equipetonclub.fr/119-Mailllot#couleur-rouge',
                    'https://www.equipetonclub.fr/119-Mailllot#couleur-vert',
                    'https://www.equipetonclub.fr/119-Mailllot#brand-puma',
                    'https://www.equipetonclub.fr/119-Mailllot#sports-football',
                    'https://www.equipetonclub.fr/mailllot/725899489-liga-goalkeeper-shirt-manches-longues-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907876-team-pacer-jersey-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907865-team-liga-striped-jersey-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907877-team-pacer-jersey-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907866-team-liga-striped-jersey-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907870-maillot-teamliga-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907871-maillot-teamliga-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907872-maillot-teamgoal-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907873-maillot-teamgoal-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907844-team-rise-jersey-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907845-team-rise-jersey-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907874-team-goal-jersey-long-sleeve-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907875-team-goal-jersey-long-sleeve-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907885-maillot-de-gardien-team-pacer-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907886-maillot-de-gardien-team-pacer-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725908967-teamfinal-training-jersey.html',
                    'https://www.equipetonclub.fr/accueil/725907933-teamgoal-casuals-tee-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907934-teamgoal-casuals-tee-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907880-maillot-team-liga-pour-femmes.html',
                    'https://www.equipetonclub.fr/veste/725907062-teamgoal-training-jacket-pour-homme.html',
                    'https://www.equipetonclub.fr/veste/725907064-teamgoal-training-jacket-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725908968-teamfinal-casuals-hoody-jacket.html',
                    'https://www.equipetonclub.fr/accueil/725910297-veste-teamliga-sideline.html',
                    'https://www.equipetonclub.fr/accueil/725910298-team-liga-training-jacket-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725910299-team-liga-training-jacket-pour-enfant.html',
                    'https://www.equipetonclub.fr/veste/725910300-teamfinal-21-casuals-hoody.html',
                    'https://www.equipetonclub.fr/veste/725910301-cup-casuals-hooded-jacket.html',
                    'https://www.equipetonclub.fr/accueil/725910302-team-goal-hooded-jacket-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725910303-team-goal-hooded-jacket-pour-enfant.html']
        },

        {
            'arr': ['https://www.equipetonclub.fr/shorts/725907060-teamfinal-21-casuals-shorts.html',
                    'https://www.equipetonclub.fr/shorts/725900664-cup-casual-short.html',
                    'https://www.equipetonclub.fr/accueil/725907159-teamliga-baselayer-short-tight.html',
                    'https://www.equipetonclub.fr/accueil/725907867-teamliga-shorts-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907868-teamliga-shorts-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907847-team-rise-shorts-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907917-teamliga-training-shorts-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907918-teamliga-training-shorts-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907914-teamliga-training-34-pants-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907881-shorts-team-liga-pour-femmes.html',
                    'https://www.equipetonclub.fr/accueil/725907919-teamliga-sideline-shorts.html',
                    'https://www.equipetonclub.fr/accueil/725908991-teamfinal-casuals-shorts.html',
                    'https://www.equipetonclub.fr/accueil/725907846-team-rise-shorts-pour-homme.html',
                    'https://www.equipetonclub.fr/pantalon/725900665-cup-casual-sweat-pants.html',
                    'https://www.equipetonclub.fr/accueil/725907916-teamliga-sideline-pants.html',
                    'https://www.equipetonclub.fr/accueil/725907912-teamliga-training-pants-pro-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907857-team-liga-training-pants-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907858-team-rise-poly-training-pants-pour-homme.html',
                    'https://www.equipetonclub.fr/accueil/725907859-team-rise-poly-training-pants-pour-enfant.html',
                    'https://www.equipetonclub.fr/accueil/725907929-teamliga-training-pants-pour-femme.html',
                    'https://www.equipetonclub.fr/accueil/725908987-teamfinal-casuals-pants.html']
        },

        {
            'arr': ['https://www.equipetonclub.fr/118-Sac#genre-adulte',
                    'https://www.equipetonclub.fr/118-Sac#genre-enfant',
                    'https://www.equipetonclub.fr/118-Sac#genre-femme',
                    'https://www.equipetonclub.fr/118-Sac#genre-homme',
                    'https://www.equipetonclub.fr/118-Sac#couleur-ciel',
                    'https://www.equipetonclub.fr/118-Sac#couleur-noir',
                    'https://www.equipetonclub.fr/118-Sac#couleur-rouge',
                    'https://www.equipetonclub.fr/118-Sac#brand-puma',
                    'https://www.equipetonclub.fr/118-Sac#sports-football',
                    'https://www.equipetonclub.fr/sac/725907018-team-goal-23-teambag.html',
                    'https://www.equipetonclub.fr/sac/725907022-teamgoal-23-wheel-teambag.html',
                    'https://www.equipetonclub.fr/sac/725899503-pro-training-ii-large-wheel-bag-adulte.html',
                    'https://www.equipetonclub.fr/accueil/725907954-puma-teamgoal-wheel-teambag-m.html',
                    'https://www.equipetonclub.fr/accueil/725907958-puma-team-medical-bag.html',
                    'https://www.equipetonclub.fr/accueil/725907959-puma-team-trolley-bag.html',
                    'https://www.equipetonclub.fr/accueil/725907961-puma-team-ballsack-16.html',
                    'https://www.equipetonclub.fr/accueil/725907960-puma-team-messenger-bag.html',
                    'https://www.equipetonclub.fr/nous-contacter',
                    'https://www.equipetonclub.fr/content/24-guide-des-tailles-ensemble',
                    'https://www.equipetonclub.fr/content/23-entretenir-les-produits',
                    'https://www.equipetonclub.fr/content/14-personnalisation-des-produits',
                    'https://www.equipetonclub.fr/content/15-emplacement-des-zones-d-impression',
                    'https://www.equipetonclub.fr/content/16-couleurs-des-polices-imprimees',
                    'https://www.equipetonclub.fr/content/17-preparation-de-vos-fichiers',
                    'https://www.equipetonclub.fr/117-ballons#genre-adulte',
                    'https://www.equipetonclub.fr/117-ballons#brand-puma',
                    'https://www.equipetonclub.fr/117-ballons#sports-football',
                    'https://www.equipetonclub.fr/accueil/725909006-puma-orbita-1-tb-fifa-quality-pro.html',
                    'https://www.equipetonclub.fr/accueil/725909007-puma-orbita-2-tb-fifa-quality-pro.html',
                    'https://www.equipetonclub.fr/accueil/725909008-puma-orbita-3-tb-fifa-quality.html',
                    'https://www.equipetonclub.fr/accueil/725909009-puma-orbita-3-tb-fifa-quality-size-4.html',
                    'https://www.equipetonclub.fr/accueil/725909010-puma-orbita-5-hs.html',
                    'https://www.equipetonclub.fr/accueil/725909011-puma-orbita-6-ms.html',
                    'https://www.equipetonclub.fr/accueil/725910275-ballon-uhlsport-club-elite-synergy-taille-5.html',
                    'https://www.equipetonclub.fr/accueil/725910274-ballon-uhlsport-synergy-pro-taille5.html',
                    'https://www.equipetonclub.fr/accueil/725907968-chasubles-puma.html',
                    'https://www.equipetonclub.fr/materiels/725899317-chasuble-ajouree-simple.html',
                    'https://www.equipetonclub.fr/accueil/725899365-chasuble-ajouree-numerotee-de-1-a-10.html',
                    'https://www.equipetonclub.fr/accueil/725899366-chasuble-ajouree-numerotee-de-11-a-15.html',
                    'https://www.equipetonclub.fr/accueil/725908980-chasuble-ajouree-numerotee-de-16-a-20.html',
                    'https://www.equipetonclub.fr/accueil/725908981-chasuble-ajouree-reversible.html']
        },

        {
            'arr': [
                'https://www.equipetonclub.fr/accueil/725908035-offre-pack-match-adulte-striped-jersey.html?search_query=MATCHPUMA&results=14',
                'https://www.equipetonclub.fr/accueil/725908036-offre-pack-match-enfant-striped-jersey.html?search_query=MATCHPUMA&results=14',
                'https://www.equipetonclub.fr/accueil/725908037-offre-pack-match-adulte-pacer-jersey.html?search_query=MATCHPUMA&results=14',
                'https://www.equipetonclub.fr/accueil/725908038-offre-pack-match-enfant-pacer-jersey.html?search_query=MATCHPUMA&results=14',
                'https://www.equipetonclub.fr/accueil/725908039-offre-pack-match-adulte-liga-jersey.html?search_query=MATCHPUMA&results=14',
                'https://www.equipetonclub.fr/accueil/725908040-offre-pack-match-enfant-liga-jersey.html?search_query=MATCHPUMA&results=14',
                'https://www.equipetonclub.fr/accueil/725908041-offre-pack-match-adulte-goal-jersey.html?search_query=MATCHPUMA&results=14',
                'https://www.equipetonclub.fr/accueil/725908042-offre-pack-match-enfant-goal-jersey.html?search_query=MATCHPUMA&results=14',
                'https://www.equipetonclub.fr/accueil/725908043-offre-pack-match-adulte-rise-jersey.html?search_query=MATCHPUMA&results=14',
                'https://www.equipetonclub.fr/accueil/725908044-offre-pack-match-enfant-rise-jersey.html?search_query=MATCHPUMA&results=14',
                'https://www.equipetonclub.fr/accueil/725909068-offre-pack-match-adulte-gardien-pacer.html?search_query=MATCHPUMA&results=14',
                'https://www.equipetonclub.fr/accueil/725908045-offre-pack-match-adulte-goal-manches-longues.html?search_query=MATCHPUMA&results=14',
                'https://www.equipetonclub.fr/accueil/725909069-offre-pack-match-enfant-gardien-pacer.html?search_query=MATCHPUMA&results=14',
                'https://www.equipetonclub.fr/accueil/725908047-offre-pack-match-enfant-goal-manches-longues.html?search_query=MATCHPUMA&results=14']
        },

        {
            'arr': [
                'https://www.equipetonclub.fr/accueil/725908072-offre-pack-sortie-argent-feminine.html?search_query=FEMININEPUMA&results=3',
                'https://www.equipetonclub.fr/accueil/725908073-offre-pack-entrainement-feminine.html?search_query=FEMININEPUMA&results=3',
                'https://www.equipetonclub.fr/accueil/725907137-offre-pack-match-feminine.html?search_query=FEMININEPUMA&results=3',
                'https://www.equipetonclub.fr/accueil/725909070-offre-pack-entrainement-adulte-team-final-zip-top.html?search_query=ENTRAINEMENTPUMA&results=13',
                'https://www.equipetonclub.fr/accueil/725909071-offre-pack-entrainement-adulte-team-final-training-jersey.html?search_query=ENTRAINEMENTPUMA&results=13',
                'https://www.equipetonclub.fr/accueil/725908051-offre-pack-entrainement-adulte-liga-bronze.html?search_query=ENTRAINEMENTPUMA&results=13',
                'https://www.equipetonclub.fr/accueil/725908055-offre-pack-entrainement-adulte-liga-argent.html?search_query=ENTRAINEMENTPUMA&results=13',
                'https://www.equipetonclub.fr/accueil/725909079-offre-pack-entrainement-team-rise-adulte-bronze.html?search_query=ENTRAINEMENTPUMA&results=13',
                'https://www.equipetonclub.fr/accueil/725908056-offre-pack-entrainement-enfant-liga.html?search_query=ENTRAINEMENTPUMA&results=13',
                'https://www.equipetonclub.fr/accueil/725909080-offre-pack-entrainement-team-rise-enfant-bronze.html?search_query=ENTRAINEMENTPUMA&results=13',
                'https://www.equipetonclub.fr/accueil/725908066-offre-pack-entrainement-adulte-liga.html?search_query=ENTRAINEMENTPUMA&results=13',
                'https://www.equipetonclub.fr/accueil/725908067-offre-pack-entrainement-enfant-liga.html?search_query=ENTRAINEMENTPUMA&results=13',
                'https://www.equipetonclub.fr/accueil/725908068-offre-pack-entrainement-goal-adulte.html?search_query=ENTRAINEMENTPUMA&results=13',
                'https://www.equipetonclub.fr/accueil/725908069-offre-pack-entrainement-goal-enfant.html?search_query=ENTRAINEMENTPUMA&results=13',
                'https://www.equipetonclub.fr/accueil/725908070-offre-pack-entrainement-team-rise-adulte-argent.html?search_query=ENTRAINEMENTPUMA&results=13',
                'https://www.equipetonclub.fr/accueil/725908071-offre-pack-entrainement-team-rise-enfant-argent.html?search_query=ENTRAINEMENTPUMA&results=13']
        },

        {
            'arr': [
                'https://www.equipetonclub.fr/accueil/725909072-offre-pack-sortie-team-goal-polo-adulte.html?search_query=SORTIEPUMA&results=7',
                'https://www.equipetonclub.fr/accueil/725909073-offre-pack-sortie-adulte-team-final.html?search_query=SORTIEPUMA&results=7',
                'https://www.equipetonclub.fr/accueil/725908057-offre-pack-sortie-liga-adulte.html?search_query=SORTIEPUMA&results=7',
                'https://www.equipetonclub.fr/accueil/725908058-offre-pack-sortie-liga-enfant.html?search_query=SORTIEPUMA&results=7',
                'https://www.equipetonclub.fr/accueil/725908059-offre-pack-sortie-goal-adulte.html?search_query=SORTIEPUMA&results=7',
                'https://www.equipetonclub.fr/accueil/725908060-offre-pack-sortie-goal-enfant.html?search_query=SORTIEPUMA&results=7',
                'https://www.equipetonclub.fr/accueil/725907106-offre-pack-sortie-enfant-argent-team-goal.html?search_query=SORTIEPUMA&results=7',
                'https://www.equipetonclub.fr/accueil/725908074-offre-pack-sortie-liga-adulte-sac.html?search_query=SORTIEPLUSPUMA&results=8',
                'https://www.equipetonclub.fr/accueil/725908075-offre-pack-sortie-liga-enfant-sac.html?search_query=SORTIEPLUSPUMA&results=8',
                'https://www.equipetonclub.fr/accueil/725908076-offre-pack-sortie-goal-adulte-sac.html?search_query=SORTIEPLUSPUMA&results=8',
                'https://www.equipetonclub.fr/accueil/725908077-offre-pack-sortie-goal-enfant-sac.html?search_query=SORTIEPLUSPUMA&results=8',
                'https://www.equipetonclub.fr/accueil/725908078-offre-pack-sortie-liga-adulte-sac-a-dos.html?search_query=SORTIEPLUSPUMA&results=8',
                'https://www.equipetonclub.fr/accueil/725908079-offre-pack-sortie-liga-enfant-sac-a-dos-goal.html?search_query=SORTIEPLUSPUMA&results=8',
                'https://www.equipetonclub.fr/accueil/725908080-offre-pack-sortie-goal-adulte-sac-a-dos-goal.html?search_query=SORTIEPLUSPUMA&results=8',
                'https://www.equipetonclub.fr/accueil/725908081-offre-pack-sortie-goal-enfant-sac-a-dos-goal.html?search_query=SORTIEPLUSPUMA&results=8']
        },

        {
            'arr': [
                'https://www.equipetonclub.fr/accueil/725909084-offre-pack-casual-team-final-adulte-argent.html?search_query=LIFESTYLEPUMA&results=4', 'https://www.equipetonclub.fr/accueil/725909085-offre-pack-casual-team-final-adulte-bronze.html?search_query=LIFESTYLEPUMA&results=4', 'https://www.equipetonclub.fr/accueil/725908085-offre-pack-lifestyle-adulte-casual.html?search_query=LIFESTYLEPUMA&results=4', 'https://www.equipetonclub.fr/accueil/725908086-offre-pack-lifestyle-enfant-casual.html?search_query=LIFESTYLEPUMA&results=4', 'https://www.equipetonclub.fr/accueil/725909081-offre-pack-hiver-adulte-baselayer-tee.html?search_query=HIVERPUMA&results=13', 'https://www.equipetonclub.fr/accueil/725909082-offre-pack-hiver-adulte-baselayer-short.html?search_query=HIVERPUMA&results=13', 'https://www.equipetonclub.fr/accueil/725909083-offre-pack-hiver-adulte-baselayer.html?search_query=HIVERPUMA&results=13', 'https://www.equipetonclub.fr/accueil/725909086-offre-doudoune-sans-manches-adulte.html?search_query=HIVERPUMA&results=13', 'https://www.equipetonclub.fr/accueil/725909087-offre-veste-hybrid-adulte.html?search_query=HIVERPUMA&results=13', 'https://www.equipetonclub.fr/accueil/725909088-offre-tour-de-cou.html?search_query=HIVERPUMA&results=13', 'https://www.equipetonclub.fr/accueil/725909089-offre-gant-bonnet.html?search_query=HIVERPUMA&results=13', 'https://www.equipetonclub.fr/accueil/725908087-offre-parka-adulte.html?search_query=HIVERPUMA&results=13', 'https://www.equipetonclub.fr/accueil/725908088-offre-parka-enfant.html?search_query=HIVERPUMA&results=13', 'https://www.equipetonclub.fr/accueil/725908089-offre-doudoune-adulte.html?search_query=HIVERPUMA&results=13', 'https://www.equipetonclub.fr/accueil/725908090-offre-doudoune-enfant.html?search_query=HIVERPUMA&results=13', 'https://www.equipetonclub.fr/accueil/725908091-offre-coupe-vent-adulte.html?search_query=HIVERPUMA&results=13', 'https://www.equipetonclub.fr/accueil/725908092-offre-coupe-vent-enfant.html?search_query=HIVERPUMA&results=13']
        }
    ]

    failed_urls = []

    for item in allArr:
        url: str | Any
        for url in item['arr']:
            try:
                driver.get(url)
                print("Opened URL:", url)
                time.sleep(5)
                for _ in range(5):
                    action.key_down(Keys.PAGE_DOWN).perform()
                    time.sleep(1)

                # Check API status
                if not check_api_status(url):
                    failed_urls.append(url)

            except TimeoutException:
                print("Timeout occurred while accessing URL:", url)

    # Quit the driver after processing all URLs
    driver.quit()

    # Send failure email if there are failed URLs
    if failed_urls:
        sender_email = "aravindcuts@gmail.com"  # Replace with your Gmail email
        sender_password = "ysfz phef wwps ahvl"  # Replace with your Gmail app-specific password
        receiver_emails = ["aravind.v@manurevasolutions.net", "aravindcuts@gmail.com", "pravin.b@manurevasolutions.net"]  # Add multiple receiver email addresses
        send_failure_email(sender_email, sender_password, receiver_emails, failed_urls)
