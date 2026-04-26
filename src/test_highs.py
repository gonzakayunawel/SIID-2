from amplpy import AMPL

ampl = AMPL()
ampl.eval("""
    var x >= 0, <= 10;
    minimize obj: x^2 + 2*x;
""")
ampl.solve(solver='highs')
print(f"x = {ampl.var['x'].value()}")