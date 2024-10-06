import tkinter as tk
from tkinter import ttk, messagebox
import sympy as sp


# Clase Aplicacion con funciones de calculadora y conversión
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.crear_layout()
        self.crear_widgets()

    # Crear el layout con diseñp responsivo
    def crear_layout(self):
        # Se expanden conforme se expande la ventana y el marco cambia de tamaño
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Creacion de frame en la ventana principal con padding de 20
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(sticky="nsew") # El argumento sticky="nsew" asegura que se expanda en todas direcciones

        # Se expanden conforme se expande la ventana y el marco cambia de tamaño
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

    # Crear los widgets de inicio
    def crear_widgets(self):
        # Label y botones de inicio
        self.label = ttk.Label(self.main_frame, text="Elige una opción", font=("Arial", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

        self.calc_button = ttk.Button(self.main_frame, text="Calculadora", command=self.mostrar_calculadora)
        self.calc_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.convert_button = ttk.Button(self.main_frame, text="Convertidor de unidades", command=self.mostrar_convertidor)
        self.convert_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.home_button = ttk.Button(self.main_frame, text="Inicio", command=self.mostrar_inicio)
        self.home_button.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

    # Ocultar todos los widgets en pantalla
    def ocultar_todo(self):
        for widget in self.main_frame.winfo_children():
            widget.grid_forget()

    # Mostrar el menú inicial
    def mostrar_inicio(self):
        self.ocultar_todo()
        self.crear_widgets()

    # Botones, Entry y labels de la calculadora
    def mostrar_calculadora(self):
        self.ocultar_todo()

        self.calc_label = ttk.Label(self.main_frame, text="Calculadora", font=("Arial", 14))
        self.calc_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

        self.entry_calc = ttk.Entry(self.main_frame, width=30)
        self.entry_calc.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")
        

        self.calc_button = ttk.Button(self.main_frame, text="Calcular", command=self.calcular)
        self.calc_button.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")
        
        self.entry_calc.bind("<Return>", self.calcular)  # Usar enter para obtener el resultado

        self.home_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        self.resultado_calc = ttk.Label(self.main_frame, text="", font=("Arial", 12))
        self.resultado_calc.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

    # Realizar cálculos con sympy usando sympify
    def calcular(self, event=None):
        try:
            resultado = sp.sympify(self.entry_calc.get())
            self.resultado_calc.config(text=f"Resultado: {resultado}")
        except Exception as e:
            messagebox.showerror("Error", "Expresión no válida")

    # Mostrar el convertidor de unidades
    def mostrar_convertidor(self):
        self.ocultar_todo()

        self.convert_label = ttk.Label(self.main_frame, text="Convertidor de Unidades", font=("Arial", 14))
        self.convert_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

        # Combobox para seleccionar el tipo de conversión
        self.combo_opciones = ttk.Combobox(self.main_frame, values=[
            "Metros a Kilómetros", 
            "Celsius a Fahrenheit", 
            "Kilogramos a Libras", 
            "Segundos a Horas"
        ], state="readonly")
        self.combo_opciones.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.combo_opciones.bind("<<ComboboxSelected>>", self.mostrar_conversion)

        self.entry_conversion = ttk.Entry(self.main_frame, width=30)
        self.entry_conversion.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.resultado_label = ttk.Label(self.main_frame, text="", font=("Arial", 12))
        self.resultado_label.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        self.convert_button = ttk.Button(self.main_frame, text="Convertir", command=self.convertir_unidades)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        self.entry_conversion.bind("<Return>", self.convertir_unidades)  # Usar enter para obtener resultado

        self.home_button.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

    # Mostrar los Entrys según la selección
    def mostrar_conversion(self, event=None):
        # Cambiar el texto del Entry según la conversión seleccionada
        seleccion = self.combo_opciones.get()
        if seleccion == "Metros a Kilómetros":
            self.entry_conversion.config(show="")  # Limpiar cualquier configuración anterior
            self.resultado_label.config(text="Ingresa metros")
        elif seleccion == "Celsius a Fahrenheit":
            self.resultado_label.config(text="Ingresa grados Celsius")
        elif seleccion == "Kilogramos a Libras":
            self.resultado_label.config(text="Ingresa kilogramos")
        elif seleccion == "Segundos a Horas":
            self.resultado_label.config(text="Ingresa segundos")

    # Función para convertir unidades
    def convertir_unidades(self, event=None):
        seleccion = self.combo_opciones.get()
        try:
            valor = float(self.entry_conversion.get())
            if seleccion == "Metros a Kilómetros":
                resultado = valor / 1000
                self.resultado_label.config(text=f"{resultado:.2f} kilómetros")
            elif seleccion == "Celsius a Fahrenheit":
                resultado = (valor * 9/5) + 32
                self.resultado_label.config(text=f"{resultado:.2f} °F")
            elif seleccion == "Kilogramos a Libras":
                resultado = valor * 2.20462
                self.resultado_label.config(text=f"{resultado:.2f} lbs")
            elif seleccion == "Segundos a Horas":
                resultado = valor / 3600
                self.resultado_label.config(text=f"{resultado:.2f} horas")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un valor numérico válido")