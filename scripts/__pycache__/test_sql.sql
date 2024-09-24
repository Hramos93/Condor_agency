CREATE VIEW Vista_Ventas_Por_Cliente
AS
WITH Datos_Agrupados AS (
    SELECT auto_transfer,
           description,
           SUM(amount) AS Total_Cantidad
    FROM invoince_items
    GROUP BY auto_transfer, description
)
SELECT auto_transfer
       [Carnes],
       [Cereales],
       [Otros] = SUM(cafe + frutas + sal+bebidas) OVER (PARTITION BY auto_transfer)
FROM Datos_Agrupados
PIVOT (
    SUM(Total_Cantidad)
    FOR description IN ([Carnes], [Cereales], [Otros])
) AS PivotTable;