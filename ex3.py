# 3) Descubra a lógica e complete o próximo elemento:

# a) 1, 3, 5, 7, ___

# b) 2, 4, 8, 16, 32, 64, ____

# c) 0, 1, 4, 9, 16, 25, 36, ____

# d) 4, 16, 36, 64, ____

# e) 1, 1, 2, 3, 5, 8, ____

# f) 2,10, 12, 16, 17, 18, 19, ____


# Sequência a)
def proximo_elemento_a():
    sequencia = [1, 3, 5, 7]
    proximo = sequencia[-1] + 2
    return proximo

# Sequência b)
def proximo_elemento_b():
    sequencia = [2, 4, 8, 16, 32, 64]
    proximo = sequencia[-1] * 2
    return proximo

# Sequência c)
def proximo_elemento_c():
    sequencia = [0, 1, 4, 9, 16, 25, 36]
    proximo = len(sequencia)**2
    return proximo

# Sequência d)
def proximo_elemento_d():
    sequencia = [4, 16, 36, 64]
    proximo = (len(sequencia) + 2)**2
    return proximo

# Sequência e)
def proximo_elemento_e():
    sequencia = [1, 1, 2, 3, 5, 8]
    proximo = sequencia[-1] + sequencia[-2]
    return proximo

# Sequência f)
def proximo_elemento_f():
    sequencia = [2, 10, 12, 16, 17, 18, 19]
    proximo = sequencia[-1] + 1
    return proximo

print("Próximos elementos das sequências:")
print("a) Próximo elemento:", proximo_elemento_a())
print("b) Próximo elemento:", proximo_elemento_b())
print("c) Próximo elemento:", proximo_elemento_c())
print("d) Próximo elemento:", proximo_elemento_d())
print("e) Próximo elemento:", proximo_elemento_e())
print("f) Próximo elemento:", proximo_elemento_f())