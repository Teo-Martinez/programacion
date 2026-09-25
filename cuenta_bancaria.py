class CuentaBancaria:
    def __init__(self, titular, numero, saldo_inicial=0):
        self.titular = titular
        self.numero = numero
        self._saldo = float(saldo_inicial)

    @property
    def saldo(self):
        # Permite consultar el saldo sin modificarlo directamente.
        return self._saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor que cero.")
        self._saldo += monto

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor que cero.")
        if monto > self._saldo:
            raise ValueError("No hay saldo suficiente para realizar la extracción.")
        self._saldo -= monto

    def __str__(self):
        return f"Cuenta {self.numero} - {self.titular} - Saldo: ${self._saldo:.2f}"
