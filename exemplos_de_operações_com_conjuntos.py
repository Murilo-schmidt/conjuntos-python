"""
Exemplos Práticos de Operações com Conjuntos em Python

Neste arquivo você encontrará as seguintes operações:
1. Interseção ($A \cap B$)
2. União ($A \cup B$)
3. Diferença ($A \setminus B$)
"""

# ==========================================
# DEFINIÇÃO DOS CONJUNTOS INICIAIS
# ==========================================
# Conjunto de alunos matriculados na aula de Matemática
alunos_matematica = {"Ana", "Bruno", "Carla", "Daniel", "Eduardo"}

# Conjunto de alunos matriculados na aula de Física
alunos_fisica = {"Carla", "Daniel", "Fernanda", "Gabriel"}

print("--- Conjuntos Iniciais ---")
print(f"Matemática: {alunos_matematica}")
print(f"Física:     {alunos_fisica}\n")


# ==========================================
# 1. INTERSEÇÃO ($A \cap B$)
# ==========================================
# Elementos presentes em AMBOS os conjuntos simultaneamente.
# Pode ser feita com o operador '&' ou com o método '.intersection()'

intersecao_operador = alunos_matematica & alunos_fisica
intersecao_metodo = alunos_matematica.intersection(alunos_fisica)

print("--- 1. Interseção (Alunos presentes em AMBAS as matérias) ---")
print(f"Com operador '&':         {intersecao_operador}")
print(f"Com método '.intersection()': {intersecao_metodo}\n")


# ==========================================
# 2. UNIÃO ($A \cup B$)
# ==========================================
# Combinação de todos os elementos de ambos os conjuntos (sem duplicatas).
# Pode ser feita com o operador '|' ou com o método '.union()'

uniao_operador = alunos_matematica | alunos_fisica
uniao_metodo = alunos_matematica.union(alunos_fisica)

print("--- 2. União (Todos os alunos cadastrados) ---")
print(f"Com operador '|':    {uniao_operador}")
print(f"Com método '.union()': {uniao_metodo}\n")


# ==========================================
# 3. DIFERENÇA ($A \setminus B$)
# ==========================================
# Elementos contidos no primeiro conjunto, mas NÃO no segundo.
# Pode ser feita com o operador '-' ou com o método '.difference()'

# Alunos que fazem APENAS Matemática (Matemática - Física)
apenas_matematica = alunos_matematica - alunos_fisica

# Alunos que fazem APENAS Física (Física - Matemática)
apenas_fisica = alunos_fisica.difference(alunos_matematica)

print("--- 3. Diferença ---")
print(f"Alunos APENAS de Matemática: {apenas_matematica}")
print(f"Alunos APENAS de Física:     {apenas_fisica}\n")