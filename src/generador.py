import pandas as pd

df = pd.read_csv("data/ventas.csv")

df["Ingresos"] = df["Cantidad"] * df["Precio"]

ventas_totales = df["Ingresos"].sum()
promedio = df["Ingresos"].mean()

resumen = pd.DataFrame({
    "Metrica": [
        "Ventas Totales",
        "Ingreso Promedio"
    ],
    "Valor": [
        ventas_totales,
        round(promedio, 2)
    ]
})

with pd.ExcelWriter(
    "reports/reporte_ventas.xlsx"
) as writer:

    df.to_excel(
        writer,
        sheet_name="Datos",
        index=False
    )

    resumen.to_excel(
        writer,
        sheet_name="Resumen",
        index=False
    )

print("Reporte generado correctamente")