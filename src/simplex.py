"""
EJEMPLO 1: PROBLEMA LP (Programación Lineal) Puro
===================================================
OR-Tools usará SIMPLEX internamente.

Problema real: Optimizar una cartera de inversión
Minimizar riesgo total manteniendo retorno esperado >= 5%

Variables: x1, x2, x3 = porcentaje de inversión en 3 activos
- x1: Acciones (riesgo 0.3, retorno 0.08)
- x2: Bonos (riesgo 0.05, retorno 0.03)
- x3: Oro (riesgo 0.15, retorno 0.02)

Restricciones:
1. x1 + x2 + x3 = 1 (100% invertido)
2. 0.08*x1 + 0.03*x2 + 0.02*x3 >= 0.05 (retorno mínimo 5%)
3. x1, x2, x3 >= 0 (no negativo)

OBJETIVO: Minimizar riesgo total = 0.3*x1 + 0.05*x2 + 0.15*x3

Este es un problema LP puro → OR-Tools usa SIMPLEX
"""

from ortools.linear_solver import pywraplp
import time

print("="*70)
print("EJEMPLO 1: PROBLEMA LP (Cartera de Inversión)")
print("="*70)
print("\nAlgoritmo usado internamente: SIMPLEX")
print("Porque: todas las variables son continuas, objetivo y restricciones lineales\n")

# Crear solucionador LP
solver = pywraplp.Solver.CreateSolver('GLOP')

if not solver:
    print("Error: GLOP solver not available")
    exit(1)

# Variables: porcentajes de inversión
x1 = solver.NumVar(0, 1, 'acciones')
x2 = solver.NumVar(0, 1, 'bonos')
x3 = solver.NumVar(0, 1, 'oro')

print("Variables:")
print("  x1 = % invertido en acciones")
print("  x2 = % invertido en bonos")
print("  x3 = % invertido en oro\n")

# Restricciones
# 1. Suma = 1 (100%)
c1 = solver.Constraint(1, 1, 'suma_100_porciento')
c1.SetCoefficient(x1, 1)
c1.SetCoefficient(x2, 1)
c1.SetCoefficient(x3, 1)

# 2. Retorno >= 5%
# 0.08*x1 + 0.03*x2 + 0.02*x3 >= 0.05
c2 = solver.Constraint(0.05, solver.infinity(), 'retorno_minimo')
c2.SetCoefficient(x1, 0.08)
c2.SetCoefficient(x2, 0.03)
c2.SetCoefficient(x3, 0.02)

print("Restricciones:")
print("  1) x1 + x2 + x3 = 1")
print("  2) 0.08*x1 + 0.03*x2 + 0.02*x3 >= 0.05\n")

# Objetivo: minimizar riesgo
# Riesgo = 0.3*x1 + 0.05*x2 + 0.15*x3
objective = solver.Objective()
objective.SetCoefficient(x1, 0.3)  # Riesgo acciones
objective.SetCoefficient(x2, 0.05)  # Riesgo bonos
objective.SetCoefficient(x3, 0.15)  # Riesgo oro
objective.SetMinimization()

print("Objetivo:")
print("  Minimizar riesgo = 0.3*x1 + 0.05*x2 + 0.15*x3\n")

# Resolver
print("-" * 70)
print("RESOLVIENDO...")
print("-" * 70)

# Habilitar logging de iteraciones
solver.EnableOutput()

start_time = time.time()
status = solver.Solve()
elapsed = time.time() - start_time

print("-" * 70)
print("RESULTADO")
print("-" * 70)

if status == pywraplp.Solver.OPTIMAL:
    print("✅ SOLUCIÓN ÓPTIMA ENCONTRADA\n")
    print("Inversión óptima:")
    print(f"  Acciones: {x1.solution_value()*100:.2f}%")
    print(f"  Bonos:    {x2.solution_value()*100:.2f}%")
    print(f"  Oro:      {x3.solution_value()*100:.2f}%")
    print(f"\nRiesgo total: {objective.Value():.4f} ({objective.Value()*100:.2f}%)")

    retorno = 0.08*x1.solution_value() + 0.03*x2.solution_value() + 0.02*x3.solution_value()
    print(f"Retorno esperado: {retorno:.4f} ({retorno*100:.2f}%)")

    print(f"\nTiempo de resolución: {elapsed*1000:.2f} ms")
else:
    print("❌ No se encontró solución óptima")

print("\n" + "="*70)
print("ANÁLISIS:")
print("="*70)
print("""
¿Por qué se usó SIMPLEX?
- Todas las variables son CONTINUAS (x1, x2, x3 ∈ [0,1])
- Función objetivo es LINEAL (0.3*x1 + 0.05*x2 + 0.15*x3)
- Restricciones son LINEALES

Simplex es PERFECTO para esto:
✓ Garantiza solución óptima
✓ Muy rápido (polinomial)
✓ La solución está en un vértice del poliedro de factibilidad

Alternativa (B&B) sería OVERKILL:
✗ B&B se usa cuando hay variables ENTERAS
✗ Aquí no tenemos esa complejidad
""")