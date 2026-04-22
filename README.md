# SIID-2: Investigación de Operaciones

Este repositorio contiene ejercicios y aplicaciones de **Investigación de Operaciones**, enfocados en programación lineal, entera y mixta, desarrollados para la asignatura de **Sistemas de Información e Investigación de Operaciones (SIID-2)** del DISA-UNAB.

## Contenido

El proyecto actualmente incluye implementaciones de:
- **Método Símplex**: Resolución de problemas de programación lineal continua.
- **Programación Entera**: Uso de técnicas como *Branch & Bound* para variables discretas.
- **Programación Entera Mixta (MIP)**: Optimización con combinación de variables continuas y enteras.

## Requisitos

- [Python](https://www.python.org/) >= 3.14
- [uv](https://github.com/astral-sh/uv) (Recomendado para la gestión de dependencias)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/gonz4gtr/SIID-2.git
   cd SIID-2
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   uv venv
   source .venv/bin/activate  # En Linux/macOS
   uv sync
   ```

## Uso

### Notebooks
Puedes explorar los ejercicios en el directorio `notebooks/`. Para ejecutar el notebook de programación lineal:
```bash
uv run jupyter notebook notebooks/linear-prog.ipynb
```

### Script Principal
Para ejecutar el script principal:
```bash
uv run main.py
```

## Tecnologías Utilizadas

- **Scipy**: Optimización y funciones matemáticas.
- **PuLP**: Modelado de problemas de optimización lineal.
- **Numpy & Pandas**: Procesamiento de datos.
- **Matplotlib & Seaborn**: Visualización de resultados.

---
© 2026 DISA-UNAB
