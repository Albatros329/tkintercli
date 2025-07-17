
import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional, Tuple, Union


class ColorPicker(ttk.Frame):
    """
    Widget de sélection de couleur pour Tkinter.
    
    Ce widget permet à l'utilisateur de sélectionner une couleur via:
    - Des curseurs RGB
    - Un aperçu de la couleur sélectionnée
    - Un champ pour entrer une valeur hexadécimale
    
    Attributes:
        command: Fonction à appeler lorsqu'une nouvelle couleur est sélectionnée
        color: Couleur actuelle au format hexadécimal (#RRGGBB)
    """
    
    def __init__(
        self,
        master: tk.Widget,
        initial_color: str = "#000000",
        command: Optional[Callable[[str], None]] = None,
        width: int = 300,
        height: int = 200,
        **kwargs
    ):
        """
        Initialiser le widget ColorPicker.
        
        Args:
            master: Widget parent
            initial_color: Couleur initiale au format hexadécimal (#RRGGBB)
            command: Fonction à appeler lorsqu'une couleur est sélectionnée
            width: Largeur du widget
            height: Hauteur du widget
        """
        super().__init__(master, **kwargs)
        
        self._command = command
        self._color = initial_color
        
        # Valider et normaliser la couleur initiale
        try:
            r, g, b = self._hex_to_rgb(initial_color)
        except ValueError:
            r, g, b = 0, 0, 0
            self._color = "#000000"
        
        self._create_widgets(width, height)
        self.set_color(r, g, b)


        
    def _create_widgets(self, width: int, height: int):
        """Créer les composants du widget."""
        # Zone principale
        main_frame = ttk.Frame(self, width=width, height=height)
        main_frame.pack(padx=5, pady=5, fill="both", expand=True)
        
        # Cadre pour les curseurs RGB
        sliders_frame = ttk.LabelFrame(main_frame, text="Valeurs RGB")
        sliders_frame.pack(side="left", padx=5, pady=5, fill="both", expand=True)
        
        # Curseur Rouge
        ttk.Label(sliders_frame, text="R:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self._red_var = tk.IntVar(value=0)
        self._red_slider = ttk.Scale(
            sliders_frame, from_=0, to=255, variable=self._red_var, 
            command=lambda _: self._update_from_sliders()
        )
        self._red_slider.grid(row=0, column=1, sticky="ew", padx=5, pady=2)
        ttk.Label(sliders_frame, textvariable=self._red_var, width=3).grid(row=0, column=2, padx=5)
        
        # Curseur Vert
        ttk.Label(sliders_frame, text="G:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self._green_var = tk.IntVar(value=0)
        self._green_slider = ttk.Scale(
            sliders_frame, from_=0, to=255, variable=self._green_var,
            command=lambda _: self._update_from_sliders()
        )
        self._green_slider.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        ttk.Label(sliders_frame, textvariable=self._green_var, width=3).grid(row=1, column=2, padx=5)
        
        # Curseur Bleu
        ttk.Label(sliders_frame, text="B:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        self._blue_var = tk.IntVar(value=0)
        self._blue_slider = ttk.Scale(
            sliders_frame, from_=0, to=255, variable=self._blue_var,
            command=lambda _: self._update_from_sliders()
        )
        self._blue_slider.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
        ttk.Label(sliders_frame, textvariable=self._blue_var, width=3).grid(row=2, column=2, padx=5)
        
        # Configurer la grille pour s'étirer
        sliders_frame.columnconfigure(1, weight=1)
        
        # Cadre pour l'aperçu et la valeur hexa
        preview_frame = ttk.Frame(main_frame)
        preview_frame.pack(side="right", padx=5, pady=5, fill="both")
        
        # Aperçu de la couleur
        preview_label = ttk.Label(preview_frame, text="Aperçu")
        preview_label.pack(padx=5, pady=2)
        
        self._preview_canvas = tk.Canvas(preview_frame, width=100, height=60, highlightthickness=1, highlightbackground="black")
        self._preview_canvas.pack(padx=5, pady=5)
        
        # Entrée pour la valeur hexadécimale
        hex_frame = ttk.Frame(preview_frame)
        hex_frame.pack(padx=5, pady=5, fill="x")
        
        ttk.Label(hex_frame, text="Hex:").pack(side="left")
        
        self._hex_var = tk.StringVar(value="#000000")
        hex_entry = ttk.Entry(hex_frame, textvariable=self._hex_var, width=8)
        hex_entry.pack(side="left", padx=3)
        
        # Lier l'événement de validation du champ hexa
        hex_entry.bind("<Return>", self._update_from_hex)
        hex_entry.bind("<FocusOut>", self._update_from_hex)
        


    def _update_from_sliders(self):
        """Mettre à jour la couleur à partir des valeurs des curseurs."""
        r = self._red_var.get()
        g = self._green_var.get()
        b = self._blue_var.get()
        
        hex_color = self._rgb_to_hex(r, g, b)
        self._hex_var.set(hex_color)
        self._color = hex_color
        
        # Mettre à jour l'aperçu
        self._preview_canvas.config(bg=hex_color)
        
        # Appeler la fonction de callback si définie
        if self._command:
            self._command(hex_color)
            


    def _update_from_hex(self, event=None):
        """Mettre à jour la couleur à partir de la valeur hexadécimale."""
        hex_value = self._hex_var.get()
        
        try:
            r, g, b = self._hex_to_rgb(hex_value)
            self._red_var.set(r)
            self._green_var.set(g)
            self._blue_var.set(b)
            
            self._color = self._rgb_to_hex(r, g, b)
            self._hex_var.set(self._color)  # Normaliser la valeur hexadécimale
            
            # Mettre à jour l'aperçu
            self._preview_canvas.config(bg=self._color)
            
            # Appeler la fonction de callback si définie
            if self._command:
                self._command(self._color)
                
        except ValueError:
            # Rétablir la valeur précédente en cas d'erreur
            self._hex_var.set(self._color)


    
    def _hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        """Convertir une valeur hexadécimale en RGB."""
        hex_color = hex_color.lstrip("#")
        
        if len(hex_color) != 6:
            raise ValueError("La valeur hexadécimale doit comporter 6 chiffres")
            
        try:
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            return r, g, b
        except ValueError:
            raise ValueError("Format hexadécimal invalide")
        

    
    def _rgb_to_hex(self, r: int, g: int, b: int) -> str:
        """Convertir des valeurs RGB en hexadécimal."""
        return f"#{r:02x}{g:02x}{b:02x}"
    


    def get_color(self) -> str:
        """Obtenir la couleur actuelle au format hexadécimal."""
        return self._color
    


    def set_color(self, r: Union[int, str], g: Optional[int] = None, b: Optional[int] = None):
        """
        Définir la couleur du sélecteur.
        
        Args:
            r: Soit une valeur entière (0-255) pour le rouge, 
               soit une chaîne hexadécimale complète (#RRGGBB)
            g: Valeur entière (0-255) pour le vert (uniquement si r est un entier)
            b: Valeur entière (0-255) pour le bleu (uniquement si r est un entier)
        """
        if isinstance(r, str) and g is None and b is None:
            # Format hexadécimal fourni
            try:
                r_val, g_val, b_val = self._hex_to_rgb(r)
            except ValueError:
                return
                
            self._red_var.set(r_val)
            self._green_var.set(g_val)
            self._blue_var.set(b_val)
            
            self._color = self._rgb_to_hex(r_val, g_val, b_val)
            self._hex_var.set(self._color)


            
        elif isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            # Format RGB fourni
            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))
            
            self._red_var.set(r)
            self._green_var.set(g)
            self._blue_var.set(b)
            
            self._color = self._rgb_to_hex(r, g, b)
            self._hex_var.set(self._color)
            
        # Mettre à jour l'aperçu
        self._preview_canvas.config(bg=self._color)