from tkinter import Frame, Label, Button, ttk, Entry
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sys import exit

def render_main_window(self):
    """Definimos la interfaz gráfica de usuario"""
    self.window.title('Self-Organizing Map')
    self.window.configure(bg='white')

    Label(self.window, text="SOM", bg="white", font=("Arial", 20)).grid(row=0, column=0, columnspan=4, sticky="we")
    # añade el gráfico de matplotlib a la interfaz de tkinter
    FigureCanvasTkAgg(self.fig, self.window).get_tk_widget().grid(row=1, rowspan=4, column=0, columnspan=4, sticky="we")

    # contendrá un segmento de la interfaz donde se establecerán los parametros de inicio
    self.params_container = Frame(self.window, bg="white", padx=50, pady=50)

    # sección para elegir las dimensiones de la rejilla
    Label(self.params_container, text="Tamaño de la rejilla: ", bg="white").grid(row=0, column=0, sticky="e")
    self.grid_size1 = ttk.Combobox(self.params_container, state="readonly")
    self.grid_size1["values"] = list(range(1, 100))
    self.grid_size1.set(self.default_grid_size)

    self.grid_size2 = ttk.Combobox(self.params_container, state="readonly")
    self.grid_size2["values"] = list(range(1, 100))
    self.grid_size2.set(self.default_grid_size)

    # sección para elegir el tipo de rejilla
    Label(self.params_container, text="Tipo de rejilla: ", bg="white").grid(row=1, column=0, sticky="e")
    self.grid_topology = ttk.Combobox(self.params_container, state="readonly")
    self.grid_topology["values"] = ["Cruz", "Estrella"] # tipos de rejilla
    self.grid_topology.set(self.default_grid_topology) # usamos como valor inicial "Cruz"

    # número de iteraciones máximas
    Label(self.params_container, text="Iteraciones máximas: ", bg="white").grid(row=2, column=0, sticky="e")
    self.max_iter = ttk.Combobox(self.params_container)
    self.max_iter["values"] = list(range(1, 1000))
    self.max_iter.set(self.default_max_iter)

    # dimensiones del archivo de entrada
    self.file_shape = Label(self.params_container, text="", bg="white", font=("Arial", 13))
    # boton para cargar archivos
    self.load_file = Button(self.params_container, bg="white", text="Cargar archivo", command=self.open_file)
    # boton para entrenar
    self.train_btn = Button(self.params_container, bg="white", text="Entrenar", command=self.run)

    # empaquetado de componenetes
    self.params_container.grid(row=5, column=0, columnspan=4, sticky="we")
    self.grid_size1.grid(row=0, column=1, sticky="we")
    self.grid_size2.grid(row=0, column=2, padx=8, sticky="we")
    self.grid_topology.grid(row=1, column=1, pady=5, sticky="we")
    self.max_iter.grid(row=2, column=1, pady=5, sticky="we")
    self.load_file.grid(row=2, column=2, padx=8, sticky="we")
    self.train_btn.grid(row=2, column=3, sticky="we")
    self.file_shape.grid(row=0, column=3, padx=20, sticky="we")

    # termina el programa al hacer click en la X roja de la ventana
    self.window.protocol('WM_DELETE_WINDOW', lambda: exit())
