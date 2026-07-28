import sqlite3
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox


# =====================================
# CLASE LOGIN
# =====================================
class Login:

    def __init__(self):

        # Crear ventana
        self.ventana = ttk.Window(themename="flatly")
        self.ventana.title("Jr. Papelería - Inicio de Sesión")
        self.ventana.geometry("500x430")
        self.ventana.resizable(False, False)

        # -----------------------------
        # TÍTULO
        # -----------------------------
        ttk.Label(
            self.ventana,
            text="JR. PAPELERÍA",
            font=("Arial", 24, "bold"),
            bootstyle="primary"
        ).pack(pady=20)

        ttk.Label(
            self.ventana,
            text="Sistema de Automatización",
            font=("Arial", 12)
        ).pack()

        ttk.Separator(self.ventana).pack(fill="x", padx=30, pady=20)

        # -----------------------------
        # USUARIO
        # -----------------------------
        ttk.Label(
            self.ventana,
            text="Usuario",
            font=("Arial", 11)
        ).pack(anchor="w", padx=60)

        self.usuario = ttk.Entry(
            self.ventana,
            width=35
        )
        self.usuario.pack(pady=5)

        # -----------------------------
        # CONTRASEÑA
        # -----------------------------
        ttk.Label(
            self.ventana,
            text="Contraseña",
            font=("Arial", 11)
        ).pack(anchor="w", padx=60)

        self.contrasena = ttk.Entry(
            self.ventana,
            show="*",
            width=35
        )
        self.contrasena.pack(pady=5)

        # -----------------------------
        # BOTÓN LOGIN
        # -----------------------------
        ttk.Button(
            self.ventana,
            text="Iniciar sesión",
            bootstyle="success",
            width=25,
            command=self.iniciar_sesion
        ).pack(pady=25)

        # -----------------------------
        # PIE
        # -----------------------------
        ttk.Label(
            self.ventana,
            text="© 2026 Jr. Papelería",
            font=("Arial", 9)
        ).pack(side="bottom", pady=15)

        self.ventana.mainloop()

    # =====================================
    # VALIDAR LOGIN
    # =====================================
    def iniciar_sesion(self):

        usuario = self.usuario.get()
        contrasena = self.contrasena.get()

        if usuario == "" or contrasena == "":
            messagebox.showwarning(
                "Campos vacíos",
                "Debe completar todos los campos."
            )
            return

        conexion = sqlite3.connect("papeleria.db")
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT *
            FROM usuarios
            WHERE usuario=? AND contrasena=?
        """, (usuario, contrasena))

        resultado = cursor.fetchone()

        conexion.close()

        if resultado:

            messagebox.showinfo(
                "Bienvenido",
                f"Bienvenido {resultado[1]}"
            )

            self.ventana.destroy()

            import menu
            menu.Menu()

        else:

            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )


# =====================================
# EJECUTAR
# =====================================
if __name__ == "__main__":
    Login()