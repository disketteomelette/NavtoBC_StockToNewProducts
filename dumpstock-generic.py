# Creado por JC Rueda (2023) - jcrueda.com
#
# ADVERTENCIA: Para usar este script necesitas ANTES modificar estas TRES variables:
#
# * FLISTADO: Nombre del archivo CSV que incluye el listado preparado para Navision. Ejemplo de formato:
# 
#             PERF00001;MONTANTE 70X40X3500 MM;;;PERFILES S.L.;PRO0000831;;M;INVENTARIO ;MERCADERIA 
#             ;;FIFO;99,77;MERCADERIA;AIIM00015;IVA21;;COMPRA;PERFILES;
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
#
# --- VARIABLES MODIFICABLES AQUÍ ABAJO --- #

flistado = "listadonuevosproductos.csv"
fexistencias = "existencias.csv"
columnumant = 14

# --- A PARTIR DE AQUÍ NO TOCAR NADA !! --- #

# Abrir los archivos especificados
with open(flistado, 'r') as archivo_lista, open(fexistencias, 'r') as archivo_existencias, open(
        'resultados.csv', 'w') as archivo_resultados :

    # Recorrer el listado línea por línea
    for linea_lista in archivo_lista :

        # Separar la línea en una lista de valores
        valores_lista = linea_lista.strip().split(';')

        # Extraer la columna número X (la especificada al principio de éste archivo)
        codigoantiguo = valores_lista[columnumant]

        # Buscar coincidencias en el archivo de existencias (diario inventario formateado)
        valor_existencias = ''
        for linea_existencias in archivo_existencias :
            valores_existencias = linea_existencias.strip().split(';')
            if codigoantiguo == valores_existencias[0] :
                valor_existencias = valores_existencias[1]
                break

        # Escribir la línea en el archivo resultados.csv
        valores_lista.append(valor_existencias)
        linea_resultados = ';'.join(valores_lista) + '\n'
        archivo_resultados.write(linea_resultados)

        # Volver al principio del archivo existencias.csv
        archivo_existencias.seek(0)

