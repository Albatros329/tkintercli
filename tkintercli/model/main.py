"""
##############################################################################
#                                                                            #
#                  Projet généré avec TkinterCLI                             #
#                                                                            #
#  TkinterCLI est un outil en ligne de commande permettant de simplifier     #
#  la création de projets Tkinter avec une architecture organisée.           #
#                                                                            #
#                                                                            #
#  GitHub: https://github.com/Albatros329/tkintercli                         #
#                                                                            #
##############################################################################
"""
import tkintercli
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    
    app = tkintercli.init(root)

    app.load_pages()
    app.navigate("Demo")

    root.mainloop()