from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')
x = solver.NumVar(0, 10, 'x')
y = solver.NumVar(0, 10, 'y')

# ✅ LINEAL (válido)
solver.Minimize(x + 2*y)
solver.Add(x + y >= 1)

solver.Solve()
print(f"x = {x.solution_value()}")