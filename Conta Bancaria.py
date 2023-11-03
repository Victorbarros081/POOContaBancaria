from BibliotecaCB import Banco

conta1 = Banco(78921, 0, 'Victor Barros', 'corrente', True, 0)
conta1.depositar(valor=2500)
conta1.sacar(valor=500)
print(conta1.verificarsaldo())





