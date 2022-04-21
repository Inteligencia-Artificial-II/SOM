from tkinter import Frame, Label, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sys import exit

def render_main_window(self):
    """Definimos la interfaz gráfica de usuario"""
    self.window.title('Self-Organizing Map')
    self.window.configure(bg='white')

    Label(self.window, text="SOM", bg="white", font=("Arial", 20)).grid(row=0, column=0, columnspan=8, sticky="we")
    # añade el gráfico de matplotlib a la interfaz de tkinter
    FigureCanvasTkAgg(self.fig, self.window).get_tk_widget().grid(row=1, rowspan=4, column=0, columnspan=4, sticky="we")
    # Añade la gráfica de convergencia del error cuadrático medio
    FigureCanvasTkAgg(self.fig2, self.window).get_tk_widget().grid(row=1, rowspan=4, column=4, columnspan=4, sticky="we")

    # contendrá un segmento de la interfaz donde se establecerán los parametros de inicio
    self.params_container = Frame(self.window, bg="white", padx=50, pady=50)
    self.load_file = Button(self.params_container, bg="white", text="Cargar archivo", command=self.open_file)

    # empaquetado de componenetes
    self.params_container.grid(row=5, column=0, columnspan=8, sticky="we")
    self.load_file.grid(row=0, column=0, sticky="we")
    
    # termina el programa al hacer click en la X roja de la ventana
    self.window.protocol('WM_DELETE_WINDOW', lambda: exit())
