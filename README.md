# RobotsTxtFinder 🤖

# English 🇬🇧

# Description

This tool allows for a quick check of whether the robots.txt files are accessible for a given set of URLs. It takes as input a text file containing the URLs to be checked, as well as various customizable parameters such as the maximum number of concurrent requests, the maximum timeout for each request, and the choice of User-Agent. Accessible URLs with robots.txt are saved to a text file as output. 
The script adds the "/robots.txt" path to the end of each URL and prepends the "http" protocol to the beginning before making the request.
The script uses asyncio to allow for asynchronous URL checking, but an option is also available to switch to synchronous mode.

# Installation :

  - Clone this repo :
  `git clone https://github.com/lhommedelasituation/RobotsTxtFinder/`
  
  - Change the working directory to RobotsTxtFinder :
  `cd RobotsTxtFinder`
  
  - Install requirements.txt
  `pip install -r requirements.txt`
  
# Usage :

  - Before using, create .txt file with urls or domain name to ckeck.
  - Run this command :
  `python robotstxtfinder.py /path/to/urls_file.txt --user-agent "my_user_agent" --concurrency 20 --timeout 10 --async`
  
# Français 🇫🇷

# Description

Cet outil permet de vérifier rapidement si les fichiers robots.txt sont accessibles pour un ensemble d'URLs donné. Il prend en entrée un fichier texte contenant les URLs à vérifier, ainsi que divers paramètres personnalisables tels que le nombre maximal de requêtes simultanées, le délai d'attente maximal pour chaque requête et le choix du User-Agent. Les URLs accessibles sont sauvegardées dans un fichier texte en sortie.
Le script ajoute le chemin "/robots.txt" à la fin de chaque URL et ajoute le protocole "http" au début avant de faire la requête.
Le script utilise asyncio pour permettre une vérification asynchrone des URLs, mais une option est également disponible pour passer en mode synchrone.

# Installation :

  - Clonez ce repo :
  `git clone https://github.com/lhommedelasituation/RobotsTxtFinder/`

  - Changez le répertoire de travail en RobotsTxtFinder :
  `cd RobotsTxtFinder`

  - Installez requirements.txt :
  `pip install -r requirements.txt`
  
# Utilisation :

  - Avant d'utiliser l'outil, créez un fichier .txt avec les URLs ou les noms de domaine à vérifier.
  - Exécutez la commande suivante :
  `python robotstxtfinder.py /chemin/vers/fichier_urls.txt --user-agent "mon_user_agent" --concurrency 20 --timeout 10 --async`
