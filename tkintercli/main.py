import json
import shutil
import os
import subprocess
import sys
import click
from colorama import init, Fore
import yaml
import getpass
import time
from tqdm import tqdm
import threading

def snake_to_pascal(s):
    return ''.join(part.capitalize() for part in s.split('_'))

@click.group()
def cli():
    """
    TkinterCLI est un outil en ligne de commande permettant de simplfier la création de projet avec Tkinter.

    -> https://github.com/Albatros329/tkintercli
    """
    pass

@cli.group()
def add():
    """Groupe de commandes pour ajouter des éléments dans un projet TkinterCLI."""
    pass


@cli.command()
@click.argument("name")
@click.option("--venv", is_flag=True, help="Créer un environnement virtuel dans le projet.")
def new(name, venv):
    """Créer un projet"""

    if not os.path.exists(f"{PATH}\\{name}"):
        shutil.copytree(f"{PATH_TKINTERCLI}\\model", f"{PATH}\\{name}")

        with open(f"{PATH}\\{name}\\conf\\app.conf", "r+", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            data["DEFAULT"]["app_name"] = name
            data["DEFAULT"]["author"] = getpass.getuser()
            f.seek(0)
            yaml.dump(data, f)
            f.close()

        if venv:
            print(Fore.BLUE + "Création de l'environnement virtuel...")
            os.system(f'python -m venv "{PATH}\\{name}\\venv"')


        print(Fore.GREEN + f"Succès: Le projet {name} a été créé.")
    else:
        print(Fore.RED + "Erreur: dossier déjà existant.")



@cli.command()
def build():
    """Compiler le projet"""
    if os.path.exists(f"{PATH}\\main.py") and os.path.exists(f"{PATH}\\conf") and os.path.exists(f"{PATH}\\views"):
        pip_list = json.loads(subprocess.check_output(['pip','list','--format=json']))
        packages = []
        for i in pip_list:
            packages.append(i["name"])

        if not "pyinstaller" in packages:
            print(Fore.RED + "Erreur: pyinstaller doit être installé sur cette machine.\n-> pip install pyinstaller")
        else:
            with open(f"{PATH}\\conf\\app.conf", "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                f.close()
            
            
            print(Fore.CYAN + "Lancement de la compilation avec PyInstaller...")
            
            command = subprocess.run(
                [
                    "pyinstaller",
                    "--noconfirm",
                    "--onefile",
                    "--windowed",
                    "--icon", ".\\ressources\\images\\logo.ico",
                    "--name", data['DEFAULT']['app_name'],
                    "--clean",
                    "--add-data", ".\\ressources;ressources/",
                    "--add-data", ".\\conf;conf/",
                    "--add-data", ".\\views;views/",
                    "main.py"
                ],
                shell=True,
                text=True
            )

            if command.stderr:
                print(Fore.YELLOW + "Erreurs/Warnings de PyInstaller:")
                print(command.stderr)
            if command.returncode != 0:
                print(Fore.RED + f"Échec: PyInstaller s'est terminé avec le code {command.returncode}")
            else:
                print(Fore.GREEN + f"Succès: Exécutable disponible dans le dossier {PATH}\\dist")
    else:
        print(Fore.RED + "Erreur: cette commande est uniquement disponible dans les projets tkintercli")
    



@add.command()
@click.argument("name")
def page(name):
    """Créer une nouvelle page"""
    if os.path.exists(f"{PATH}\\pages"):
        if not os.path.exists(f"{PATH}\\pages\\{name}.py"):
            name = name.lower()
            shutil.copy(f"{PATH_TKINTERCLI}\\model\\pages\\demo.py", f"{PATH}\\pages\\{name}.py")

            with open(f"{PATH}\\pages\\{name}.py", "r+", encoding="utf-8") as f:
                data = f.read()
                f.seek(0)
                f.write(data.replace("Demo", snake_to_pascal(name)))
                f.close()

            print(Fore.GREEN + f"Succès: La page {name} a été créée.")
        else:
            print(Fore.YELLOW + "Erreur: cette page existe déjà.")
    else:
        print(Fore.RED + "Erreur: cette commande est uniquement disponible dans les projets tkintercli")



def main():
    """Fonction principale appelée lors de l'exécution de la commande tkintercli"""
    init(autoreset=True)

    global PATH, PATH_TKINTERCLI
    PATH = os.getcwd()
    PATH_TKINTERCLI = os.path.dirname(os.path.abspath(__file__))


    cli()


if __name__ == '__main__':
    main()
