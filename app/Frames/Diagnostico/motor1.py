from kanren import Relation, facts, var, run, conde

# Definimos relaciones
tiene_signo = Relation()
categoria = Relation()

# Añadimos los signos/síntomas como hechos
facts(tiene_signo, ("tiene_temperatura", "persona1"),
      ("tiene_tos", "persona1"),
      ("tiene_dolor_de_garganta", "persona1"),
      ("tiene_temperatura", "persona2"),
      ("tiene_dolor_al_orinar", "persona2"),
      ("tiene_tos", "persona3"),
      ("tiene_dificultad_para_respirar", "persona3"))

# Variable para consultas
x = var()

# Reglas para identificar categorías
def determinar_categoria(persona, cat):
    return conde(
        [
            # Síndrome febril
            (tiene_signo("tiene_temperatura", persona), (cat == "síndrome febril")),
            # Problema respiratorio
            (tiene_signo("tiene_tos", persona),
             tiene_signo("tiene_dificultad_para_respirar", persona),
             (cat == "problema respiratorio")),
            # Infección probable
            (tiene_signo("tiene_temperatura", persona),
             tiene_signo("tiene_dolor_de_garganta", persona),
             (cat == "infección probable"))
        ]
    )

# Consultar categoría para persona1
resultado = run(0, x, determinar_categoria("persona1", x))
print(f"Categorías para persona1: {resultado}")

# Consultar categoría para persona2
resultado = run(0, x, determinar_categoria("persona2", x))
print(f"Categorías para persona2: {resultado}")

# Consultar categoría para persona3
resultado = run(0, x, determinar_categoria("persona3", x))
print(f"Categorías para persona3: {resultado}")
