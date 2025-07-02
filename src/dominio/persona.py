

class Persona:
    def __init__(self, nombre, apellido, cedula, sexo, email):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._sexo = sexo
        self._email = email


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor


    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        if not valor:
            raise ValueError("El apellido no puede estar vacío.")
        self._apellido = valor


    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        if not valor.isdigit():
            raise ValueError("La cédula debe contener solo números.")
        self._cedula = valor


    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, valor):
        if valor.lower() not in ['masculino', 'femenino', 'otro']:
            raise ValueError("Sexo debe ser 'masculino', 'femenino' u 'otro'.")
        self._sexo = valor.lower()


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise ValueError("Email no válido.")
        self._email = valor


    def __str__(self):
        return f'Persona: {self.__dict__.__str__()}'



if __name__ == '__main__':
    p1 = Persona("Marceloino", "Suarez", "093455443", "M", "adad@gmail.com")
    print(p1)