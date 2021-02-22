class Libro():

    def __init__(self, codigo, titulo, autor, editorial):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial

    def codigo(self):
        return self.__codigo

    def titulo(self):
        return self.__titulo

    def autor(self):
        return self.__autor

    def editorial(self):
        return self.__editorial
