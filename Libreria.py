from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# ---------- ABSTRACCIÓN ----------


class MaterialBiblioteca(ABC):
    def __init__(self, titulo, codigo):
        self._titulo = titulo          # Encapsulado
        self._codigo = codigo
        self.__disponible = True       # Privado

    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, estado):
        if isinstance(estado, bool):
            self.__disponible = estado

    @abstractmethod
    def mostrar_detalles(self):
        pass

    @abstractmethod
    def calcular_multa(self, dias_retraso):
        pass

# ---------- HERENCIA ----------


class Libro(MaterialBiblioteca):
    def __init__(self, titulo, codigo, autor, paginas):
        super().__init__(titulo, codigo)
        self.autor = autor
        self.paginas = paginas

    # Polimorfismo
    def mostrar_detalles(self):
        return f"Libro: {self._titulo} por {self.autor}"

    def calcular_multa(self, dias_retraso):
        return dias_retraso * 0.50   # 50 centavos por día


class DVD(MaterialBiblioteca):
    def __init__(self, titulo, codigo, duracion):
        super().__init__(titulo, codigo)
        self.duracion = duracion

    def mostrar_detalles(self):
        return f"DVD: {self._titulo} ({self.duracion} min)"

    def calcular_multa(self, dias_retraso):
        return dias_retraso * 1.00   # 1 dólar por día

# ---------- ABSTRACCIÓN EN USUARIO ----------


class Usuario(ABC):
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.__prestamos_activos = []

    def tomar_prestado(self, material):
        if material.disponible:
            material.disponible = False
            self.__prestamos_activos.append(material)
            return True
        return False

    @abstractmethod
    def get_tipo_usuario(self):
        pass


class Estudiante(Usuario):
    def get_tipo_usuario(self):
        return "Estudiante"

    def get_limite_dias(self):
        return 7


class Profesor(Usuario):
    def get_tipo_usuario(self):
        return "Profesor"

    def get_limite_dias(self):
        return 15


# ---------- DEMOSTRACIÓN ----------
if __name__ == "__main__":
    # Materiales
    libro1 = Libro("Cien años de soledad", "L001", "García Márquez", 432)
    dvd1 = DVD("Inception", "D001", 148)

    # Usuario
    alumno = Estudiante("Carlos Pérez", "E2024001")

    # Préstamo
    print(alumno.tomar_prestado(libro1))  # True
    print(f"Libro disponible? {libro1.disponible}")  # False

    # Polimorfismo
    materiales = [libro1, dvd1]
    for m in materiales:
        print(m.mostrar_detalles())
        print(f"Multa por 3 días de retraso: ${m.calcular_multa(3)}")
