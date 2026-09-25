class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self._cuentas = {}

    def agregar_cuenta(self, cuenta):
        if cuenta.numero in self._cuentas:
            raise ValueError("Ya existe una cuenta con ese número.")
        self._cuentas[cuenta.numero] = cuenta

    def buscar_cuenta(self, numero):
        return self._cuentas.get(numero)

    def transferir(self, numero_origen, numero_destino, monto):
        origen = self.buscar_cuenta(numero_origen)
        destino = self.buscar_cuenta(numero_destino)

        # Verificamos ambas cuentas antes de mover el dinero.
        if origen is None or destino is None:
            raise ValueError("La cuenta de origen o de destino no existe.")
        if monto <= 0:
            raise ValueError("El monto a transferir debe ser mayor que cero.")

        # Cada objeto usa el método extraer que corresponde a su clase.
        origen.extraer(monto)
        destino.depositar(monto)

    def total_depositado(self):
        total = 0.0
        for cuenta in self._cuentas.values():
            total += cuenta.saldo
        return total

    def listar_cuentas(self):
        for cuenta in self._cuentas.values():
            print(cuenta)
