<div align="center">

<h1><img src="assets/images/logo.png" width="128px"><br>TkinterCLI - Make Tkinter Development Effortless</h1>

</div>

![PyPI - Version](https://img.shields.io/pypi/v/tkintercli?logo=pypi&label=Latest%20version)
![PyPI - Downloads](https://img.shields.io/pypi/dd/tkintercli?logo=pypi&label=Daily%20downloads)
![PyPI - Downloads](https://img.shields.io/pypi/dm/tkintercli?logo=pypi&label=Monthly%20downloads)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Albatros329/tkintercli/python-publish.yml?logo=python&logoColor=white&label=Build%20status)

**:fr: [Français](README.md)** - **:gb: [Anglais](README_en.md)**

TkinterCLI est un outil en ligne de commande permettant de simplifier la création de projet avec Tkinter. Grâce à cet outil, vous pouvez rapidement mettre en place une structure de projet complète, gérer un système de navigation multipage et profiter d'icônes préinstallées, le tout sans configuration manuelle fastidieuse.

## Fonctionnalités
- **Création automatique de projet** - Génération d'une structure complète de projet Tkinter en une seule commande
- **Système de navigation multipage** - Gestion simplifiée des transitions entre interfaces
- **Bibliothèque d'icônes intégrée** - Accès à une collection d'icônes prêtes à l'emploi
- **Support pour environnement virtuel** - Option de création automatique d'un environnement virtuel dédié
- **Architecture organisée** - Structure de fichiers claire séparant les vues, les contrôleurs et les ressources
- **Interface de ligne de commande intuitive** - Commandes simples pour créer et étendre votre application

## Installation
### Depuis PyPi (recommandé)
```
pip install tkintercli
```
### Depuis Github
```
git clone https://github.com/Albatros329/tkintercli.git
cd tkintercli/
python setup.py install
```

## Utilisation

Les arguments entre [] sont obligatoires, tandis que ceux entre () sont facultatifs.

### Créer un nouveau projet
```
tkintercli new [NOM] (--venv)
```

### Ajouter une nouvelle page
```
tkintercli add page [NOM]
```