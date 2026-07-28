import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import ttk as tkttk


class Productos:

    def __init__(self):

        # ===============================
        # VENTANA
        # ===============================

        self.ventana = ttk.Toplevel()

        self.ventana.title("Gestión de Productos")

        self.ventana.geometry("1100x650")

        self.ventana.resizable(False, False)

        # ===============================
        # TITULO
        # ===============================

        titulo = ttk.Label(
            self.ventana,
            text="GESTIÓN DE PRODUCTOS",
            font=("Arial", 22, "bold"),
            bootstyle="primary"
        )

        titulo.pack(pady=15)

        # ===============================
        # FORMULARIO
        # ===============================

        formulario = ttk.LabelFrame(
            self.ventana,
            text="Información del Producto",
            padding=20
        )

        formulario.pack(fill="x", padx=20)

        # -------------------------------
        # NOMBRE
        # -------------------------------

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.txt_nombre = ttk.Entry(
            formulario,
            width=40
        )

        self.txt_nombre.grid(row=0, column=1)

        # -------------------------------
        # CATEGORIA
        # -------------------------------

        ttk.Label(
            formulario,
            text="Categoría:"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.cmb_categoria = ttk.Combobox(
            formulario,
            width=37,
            state="readonly"
        )

        self.cmb_categoria["values"] = (
            "Escolar",
            "Oficina",
            "Tecnología",
            "Arte",
            "Limpieza",
            "Otros"
        )

        self.cmb_categoria.grid(row=1, column=1)

        # -------------------------------
        # PRECIO
        # -------------------------------

        ttk.Label(
            formulario,
            text="Precio:"
        ).grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.txt_precio = ttk.Entry(
            formulario,
            width=20
        )

        self.txt_precio.grid(row=2, column=1, sticky="w")

        # -------------------------------
        # STOCK
        # -------------------------------

        ttk.Label(
            formulario,
            text="Stock:"
        ).grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.txt_stock = ttk.Entry(
            formulario,
            width=20
        )

        self.txt_stock.grid(row=3, column=1, sticky="w")

        # -------------------------------
        # STOCK MINIMO
        # -------------------------------

        ttk.Label(
            formulario,
            text="Stock mínimo:"
        ).grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.txt_stock_minimo = ttk.Entry(
            formulario,
            width=20
        )

        self.txt_stock_minimo.grid(row=4, column=1, sticky="w")

        # ===============================
        # BOTONES
        # ===============================

        botones = ttk.Frame(self.ventana)

        botones.pack(pady=20)

        ttk.Button(
            botones,
            text="Guardar",
            width=15,
            bootstyle="success"
        ).grid(row=0, column=0, padx=10)

        ttk.Button(
            botones,
            text="Editar",
            width=15,
            bootstyle="warning"
        ).grid(row=0, column=1, padx=10)

        ttk.Button(
            botones,
            text="Eliminar",
            width=15,
            bootstyle="danger"
        ).grid(row=0, column=2, padx=10)

        ttk.Button(
            botones,
            text="Limpiar",
            width=15,
            bootstyle="secondary"
        ).grid(row=0, column=3, padx=10)

        # ===============================
        # BUSCADOR
        # ===============================

        busqueda = ttk.Frame(self.ventana)

        busqueda.pack(fill="x", padx=20)

        ttk.Label(
            busqueda,
            text="Buscar:"
        ).pack(side="left")

        self.txt_buscar = ttk.Entry(
            busqueda,
            width=45
        )

        self.txt_buscar.pack(side="left", padx=10)

        ttk.Button(
            busqueda,
            text="Buscar",
            bootstyle="info"
        ).pack(side="left")

        # ===============================
        # TABLA
        # ===============================

        tabla_frame = ttk.Frame(self.ventana)

        tabla_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        columnas = (
            "id",
            "nombre",
            "categoria",
            "precio",
            "stock",
            "stock_minimo"
        )

        self.tabla = tkttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("categoria", text="Categoría")
        self.tabla.heading("precio", text="Precio")
        self.tabla.heading("stock", text="Stock")
        self.tabla.heading("stock_minimo", text="Stock Mínimo")

        self.tabla.column("id", width=60, anchor="center")
        self.tabla.column("nombre", width=260)
        self.tabla.column("categoria", width=180)
        self.tabla.column("precio", width=120, anchor="center")
        self.tabla.column("stock", width=120, anchor="center")
        self.tabla.column("stock_minimo", width=120, anchor="center")

        self.tabla.pack(fill="both", expand=True)
        # ===============================
        # CARGAR PRODUCTOS
        # ===============================

        self.cargar_productos()

    # =====================================
    # CARGAR PRODUCTOS
    # =====================================
    def cargar_productos(self):

        print("Cargando productos...")


if __name__ == "__main__":

    app = ttk.Window(themename="flatly")

    app.withdraw()

    Productos()

    app.mainloop()