import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Importar el módulo Productos
from modulos.productos import Productos


class Menu:

    def __init__(self):

        self.ventana = ttk.Window(themename="flatly")
        self.ventana.title("Jr. Papelería")
        self.ventana.geometry("900x600")
        self.ventana.resizable(False, False)

        # ===============================
        # TÍTULO
        # ===============================

        ttk.Label(
            self.ventana,
            text="JR. PAPELERÍA",
            font=("Arial", 24, "bold"),
            bootstyle="primary"
        ).pack(pady=20)

        ttk.Label(
            self.ventana,
            text="Menú Principal",
            font=("Arial", 14)
        ).pack()

        # ===============================
        # CONTENEDOR DE BOTONES
        # ===============================

        contenedor = ttk.Frame(self.ventana)
        contenedor.pack(pady=40)

        # ===============================
        # FILA 1
        # ===============================

        ttk.Button(
            contenedor,
            text="Productos",
            width=20,
            bootstyle="primary",
            command=self.abrir_productos
        ).grid(row=0, column=0, padx=20, pady=20)

        ttk.Button(
            contenedor,
            text="Inventario",
            width=20,
            bootstyle="primary",
            command=self.abrir_inventario
        ).grid(row=0, column=1, padx=20, pady=20)

        # ===============================
        # FILA 2
        # ===============================

        ttk.Button(
            contenedor,
            text="Ventas",
            width=20,
            bootstyle="primary",
            command=self.abrir_ventas
        ).grid(row=1, column=0, padx=20, pady=20)

        ttk.Button(
            contenedor,
            text="Servicios",
            width=20,
            bootstyle="primary",
            command=self.abrir_servicios
        ).grid(row=1, column=1, padx=20, pady=20)

        # ===============================
        # FILA 3
        # ===============================

        ttk.Button(
            contenedor,
            text="Reportes",
            width=20,
            bootstyle="primary",
            command=self.abrir_reportes
        ).grid(row=2, column=0, padx=20, pady=20)

        ttk.Button(
            contenedor,
            text="Usuarios",
            width=20,
            bootstyle="primary",
            command=self.abrir_usuarios
        ).grid(row=2, column=1, padx=20, pady=20)

        # ===============================
        # BOTÓN CERRAR SESIÓN
        # ===============================

        ttk.Button(
            self.ventana,
            text="Cerrar sesión",
            width=15,
            bootstyle="danger",
            command=self.cerrar
        ).pack(pady=30)

        self.ventana.mainloop()

    # ==================================
    # MÉTODOS
    # ==================================

    def abrir_productos(self):
        Productos()

    def abrir_inventario(self):
        print("Inventario en construcción")

    def abrir_ventas(self):
        print("Ventas en construcción")

    def abrir_servicios(self):
        print("Servicios en construcción")

    def abrir_reportes(self):
        print("Reportes en construcción")

    def abrir_usuarios(self):
        print("Usuarios en construcción")

    def cerrar(self):

        self.ventana.destroy()

        import login
        login.Login()


if __name__ == "__main__":
    Menu()