# NavtoBC_StockToNewProducts
Easy way to dump data from stock to a list of new generated products. Created for a Navision to Business Central migration.

# Creado por JC Rueda (2023) - jcrueda.com
#
# ADVERTENCIA: Para usar este script necesitas ANTES modificar estas TRES variables:
#
# * FLISTADO: Nombre del archivo CSV que incluye el listado preparado para Navision. Ejemplo de formato:
# 
#             PERF00001;MONTANTE 70X40X3500 MM;;;PERFILES S.L.;PRO0000831;;M;INVENTARIO ;MERCADERIA 
#             ;;FIFO;99,77;MERCADERIA;AIIM00015;IVA21;;COMPRA;PERFILERIA PYL;
#
# * FEXISTENCIAS: Nombre del archivo CSV exportado de "diario inventario" donde con anterioridad a usar este programa, 
#                 se han eliminado todas las columnas a excepción de código antiguo de Nav y las cantidades que figuran 
#                 en existencias. Ejemplo de formato:
#
#                 AIIM00015;2618
#
# * COLUMNUMANT: Número de columna de la que obtener el código antiguo en Navision. En el caso de ejemplo es la columna 15.
#                OJO: Python considera "0" la primera columna, por lo que hay que restar 1 a la columna que se quiera 
#                extraer (ej. Si queremos 15, ponemos 14). Este código es el que se buscará en el archivo referido en
#                la variable FEXISTENCIAS. 
#
# Una vez ejecutado, el programa generará un archivo llamado RESULTADOS.CSV. Las cantidades encontradas en el diario
# inventario se añadirán al listado como una nueva columna al final. Basta abrir el archivo con Excel y arrastrar la
# última columna al lugar correspondiente (a la columna "Cantidades") y listo. Si el programa no encuentra las cantidades
# en el diario inventario, dejará en blanco y será fácilmente localizable el problema, si bien no debe fallar. 
