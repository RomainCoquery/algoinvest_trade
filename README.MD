***Note : ce projet est réalisé pendant ma formation [OpenClassrooms](https://openclassrooms.com/fr/).***
# AlgoInvest&Trade
### Ces algorithmes permettent d'optimiser les stratégies d'investissement.
### Installation:
#### Cloner ce dépôt puis créez un environnement virtuel et activez-le :
```
python -m venv venv
source venv/bin/activate
```
#### Installation des packages :
```
pip install -r requirements.txt
```
#### Lancer le script suivant l'algorithme voulu
```
python -m bruteforce.py [nom du csv] sur Windows
python -m optimized.py [nom du csv] sur Windows

ou

python3 -m bruteforce.py [nom du csv] pour Linux et mac Os
python3 -m optimized.py [nom du csv] pour Linux et mac Os
```
***Note le fichier doit de données doit être sous format csv***
***avec séparateur ',' et les titres en ligne 1***