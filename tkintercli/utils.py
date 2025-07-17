import os
import sys
import yaml
import tkinter as tk
import importlib
from tkinter.messagebox import showerror


class TkinterCLIApp:
    def __init__(self, root, title=None):
        """
        Initialise la fenêtre principale
        """
        self.root = root
        
        # Déterminer le chemin de l'application
        if getattr(sys, 'frozen', False):
            self.PATH = os.path.join(sys._MEIPASS + "\\\\") # type: ignore
        else:
            self.PATH = os.getcwd()

            
        # Charger la configuration
        try:
            self.CONFIG = yaml.safe_load(open(f"{self.PATH}\\conf\\app.conf"))
        except Exception as e:
            self.CONFIG = {"DEFAULT": {"app_name": "TkinterCLI App", "version": "1.0.0", "author": ""}}
            print(f"Avertissement: Impossible de charger la configuration: {str(e)}")


            
        # Configurer la fenêtre
        self.root.title(title or self.CONFIG['DEFAULT']['app_name'])
        try:
            self.root.iconbitmap(f"{self.PATH}\\ressources\\images\\logo.ico")
        except:
            pass


        # Conteneur principal pour les pages
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        

        # Dictionnaire pour stocker les pages
        self.pages = {}
        


    def add_page(self, page_class, page_name=None):
        """
        Ajoute une page à l'application
        """
        name = page_name or page_class.__name__
        page = page_class(self.container, self)
        self.pages[name] = page
        page.grid(row=0, column=0, sticky="nsew")
        return page
        


    def navigate(self, page_name):
        """
        Change la page actuellement affichée
        """
        if page_name in self.pages:
            self.pages[page_name].tkraise()
            return True
        else:
            showerror("Erreur", f"Page non trouvée: {page_name}")
            return False
            


    def load_pages(self):
        """
        Charge automatiquement toutes les pages d'un répertoire
        """
        try:
            classes = []
            for fichier in os.listdir(f"{self.PATH}\\views"):
                if fichier.endswith(".py") and not fichier.startswith("_"):
                    nom_module = fichier[:-3]
                    nom_classe = snake_to_pascal(nom_module)
                    module = importlib.import_module(f"views.{nom_module}")
                    classe = getattr(module, nom_classe)
                    classes.append(classe)
            
            for PageClass in classes:
                name = PageClass.__name__
                self.add_page(PageClass, name)
                
            return True
        except Exception as e:
            print(f"Erreur lors du chargement des pages: {str(e)}")
            return False
        
def snake_to_pascal(s):
    return ''.join(part.capitalize() for part in s.split('_'))


def init(root, **kwargs):
    """
    Initialise une application TkinterCLI
    """
    app = TkinterCLIApp(root, **kwargs)
    return app