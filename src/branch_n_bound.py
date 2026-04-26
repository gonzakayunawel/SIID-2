"""
EJEMPLO 2: PROBLEMA MIP (Mixed Integer Programming)
====================================================
OR-Tools usará BRANCH & BOUND (+ cortes, heurísticas) internamente.

Problema real: Asignación de trabajadores a proyectos
Tienes 5 trabajadores, cada uno puede estar COMPLETO o NO en un proyecto.
No puedes tener "50% del trabajador".

Variables ENTERAS (binarias):
- y1, y2, y3, y4, y5 ∈ {0, 1}
  - 1 = trabajador asignado al proyecto
  - 0 = no asignado

Datos:
- Costo de asignación: [100, 150, 120, 140, 130] $/trabajador
- Habilidad (puntos): [5, 8, 6, 7, 9] puntos
- Requerimiento: mínimo 20 puntos de habilidad

Restricciones:
1. 5*y1 + 8*y2 + 6*y3 + 7*y4 + 9*y5 >= 20 (habilidad mínima)
2. y1, y2, y3, y4, y5 ∈ {0, 1}

OBJETIVO: Minimizar costo = 100*y1 + 150*y2 + 120*y3 + 140*y4 + 130*y5

Este es un problema MIP (enteros) → OR-Tools usa BRANCH & BOUND
"""

from ortools.linear_solver import pywraplp
import time

print("="*70)
print("EJEMPLO 2: PROBLEMA MIP (Asignación de Trabajadores)")
print("="*70)
print("\nAlgoritmo usado internamente: BRANCH & BOUND (+ cortes y heurísticas)")
print("Porque: variables BINARIAS (0 o 1), no pueden ser fraccionarias\n")

# Crear solucionador MIP (Integer Programming)
solver = pywraplp.Solver.CreateSolver('CBC')

if not solver:
    print("Error: CBC solver not available")
    exit(1)

# Datos
costos = [100, 150, 120, 140, 130]
habilidades = [5, 8, 6, 7, 9]
nombres = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve']

# Variables: binarias (0 o 1)
y = []
for i in range(5):
    y.append(solver.IntVar(0, 1, f'asignar_{nombres[i]}'))

print("Variables binarias (0 o 1):")
for i, nombre in enumerate(nombres):
    print(f"  y{i+1} ({nombre}): {[0, 1]} → costo ${costos[i]}, habilidad {habilidades[i]} pts")

print()

# Restricción: habilidad mínima >= 20
c1 = solver.Constraint(20, solver.infinity(), 'habilidad_minima')
for i in range(5):
    c1.SetCoefficient(y[i], habilidades[i])

print("Restricción:")
print(f"  {habilidades[0]}*y1 + {habilidades[1]}*y2 + {habilidades[2]}*y3 + {habilidades[3]}*y4 + {habilidades[4]}*y5 >= 20")
print()

# Objetivo: minimizar costo
objective = solver.Objective()
for i in range(5):
    objective.SetCoefficient(y[i], costos[i])
objective.SetMinimization()

print("Objetivo:")
print(f"  Minimizar costo = {costos[0]}*y1 + {costos[1]}*y2 + {costos[2]}*y3 + {costos[3]}*y4 + {costos[4]}*y5")
print()

# Resolver
print("-" * 70)
print("RESOLVIENDO (usando BRANCH & BOUND)...")
print("-" * 70)
print()

solver.EnableOutput()

start_time = time.time()
status = solver.Solve()
elapsed = time.time() - start_time

print()
print("-" * 70)
print("RESULTADO")
print("-" * 70)

if status == pywraplp.Solver.OPTIMAL:
    print("✅ SOLUCIÓN ÓPTIMA ENCONTRADA\n")
    
    print("Asignación de trabajadores:")
    costo_total = 0
    habilidad_total = 0
    for i in range(5):
        if y[i].solution_value() == 1:
            print(f"  ✓ {nombres[i]}: asignado (costo ${costos[i]}, habilidad {habilidades[i]} pts)")
            costo_total += costos[i]
            habilidad_total += habilidades[i]
        else:
            print(f"  ✗ {nombres[i]}: NO asignado")
    
    print(f"\nCosto total: ${costo_total}")
    print(f"Habilidad total: {habilidad_total} pts (requerimiento: >= 20 pts)")
    print(f"Tiempo de resolución: {elapsed*1000:.2f} ms")
else:
    print("❌ No se encontró solución óptima")

print("\n" + "="*70)
print("¿POR QUÉ SE USÓ BRANCH & BOUND?")
print("="*70)
print("""
Comparación LP vs MIP:

LP (ejemplo anterior - Simplex):
  ✓ Variables continuas [0, 1]
  ✓ Solución: x1=0.3, x2=0.5, x3=0.2 ← VÁLIDO
  ✓ Simplex converge rápido a vértice óptimo

MIP (este ejemplo - Branch & Bound):
  ✗ Variables binarias {0, 1}
  ✗ Si relajamos: y1=0.5, y2=0.8, y3=0.3 ← NO VÁLIDO (no son 0 o 1)
  ✓ Branch & Bound ramifica:
    - Rama 1: fuerza y1=0 y resuelve sub-problema
    - Rama 2: fuerza y1=1 y resuelve sub-problema
    - Poda ramas que no pueden mejorar la mejor solución encontrada

Resultado: garantiza solución donde TODAS las variables son enteras.

Complejidad:
  - Simplex: O(n³) iteraciones
  - B&B: exponencial en el peor caso, pero podas lo hacen práctico
  
Por eso MIP es más difícil que LP:
  - LP: P (tiempo polinomial)
  - MIP: NP-hard (potencialmente exponencial)
""")

print("\n" + "="*70)
print("COMPARACIÓN DE AMBOS EJEMPLOS:")
print("="*70)
print("""
┌─────────────────┬──────────────────────┬──────────────────────┐
│ Característica  │ Ejemplo 1 (LP)       │ Ejemplo 2 (MIP)      │
├─────────────────┼──────────────────────┼──────────────────────┤
│ Variables       │ Continuas [0, 1]     │ Binarias {0, 1}      │
│ Algoritmo       │ SIMPLEX              │ BRANCH & BOUND       │
│ Complejidad     │ Polinomial (rápido)  │ Exponencial (lento)  │
│ Garantía        │ Óptima siempre       │ Óptima (si tiempo ∞) │
│ Tiempo típico   │ Milisegundos         │ Milisegundos - horas │
│ Caso real       │ Inversión continua   │ Asignación discreta  │
└─────────────────┴──────────────────────┴──────────────────────┘
""")