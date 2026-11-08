class Livro():
    def __init__(self, titulo, autor, paginas, paginas_lidas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.paginas_lidas = paginas_lidas
        
    def ler(self, quantidade):
        if self.paginas_lidas + quantidade > self.paginas:
            print(f"Quantidade invalida, o livro possui apenas {self.paginas} paginas.")
            return        
        self.paginas_lidas += quantidade
        print(f"Lendo {quantidade} paginas.")
        
    def progresso(self):
        print(f"Voce ja leu: {(self.paginas_lidas/self.paginas) * 100:.2f}% do livro")
        
livro = Livro("Pequeno principe", "thulio", 500, 100)
livro.ler(300)
livro.progresso()

livro2 = Livro("Dom Casmurro", "Machado de Assis", 600, 20)
livro2.progresso()