# Grandpy project 7
Créez Grand'Py Bot 

## Cahier des charges
### Fonctionnalités
* Interactions en AJAX : l'utilisateur envoie sa question en appuyant sur entrée et la réponse s'affiche directement dans l'écran, sans recharger la page.
* Vous utiliserez l'API de Google Maps et celle de Media Wiki.
* Rien n'est sauvegardé. Si l'utilisateur charge de nouveau la page, tout l'historique est perdu.
* Vous pouvez vous amuser à inventer plusieurs réponses différentes de la part de GrandPy mais ce n'est pas une obligation. Amusez-vous !

### Parcours utilisateur
L'utilisateur ouvre son navigateur et entre l'URL que vous lui avez fournie. Il arrive devant une page contenant les éléments suivants :
* header : logo et phrase d'accroche
* zone centrale : zone vide (qui servira à afficher le dialogue) et champ de formulaire pour envoyer une question.
* footer : votre prénom & nom, lien vers votre repository Github et autres réseaux sociaux si vous en avez

L'utilisateur tape dans le champ de formulaire puis appuie sur la touche Entrée.
>"Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"

Un nouveau message apparaît : 
>"La voici : 7 cité Paradis, 75010 Paris." 

En-dessous, une carte Google Maps apparaît également avec un marqueur indiquant l'adresse demandée.

GrandPy envoie un nouveau message :
>La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au 57 rue d'Hauteville et la troisième en impasse.

### Livrables
* Document texte expliquant la démarche choisie, les difficultés rencontrées et les solutions trouvées. Le document doit être en format pdf et ne pas excéder 2 pages A4.
* [Adresse du site](https://gp-p7.herokuapp.com/) déployé sur Heroku.
* Code source hébergé sur Github. Intégrez le lien dans votre document texte.
* [Tableau Trello](https://trello.com/b/H7GGltt2/grandpy-bot) ou Pivotal Tracker contenant vos user stories.

### Contraintes
* Interface responsive
* Test Driven Development
* Code intégralement écrit en anglais : fonctions, variables, commentaires.
* Utilisation d'AJAX pour l'envoi des questions et l'affichage des réponses.
* Tests utilisant des mocks pour les API
