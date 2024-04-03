import random

codigo_verificacion = str(random.randrange(1000000)).zfill(6)
print(codigo_verificacion)
print(f"{random.randrange(1000000):06d}")