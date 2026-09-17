# Proyecto Urban Grocers 
## Objetivo del proyecto
Automatizar las pruebas de la lista de comprobación del campo `name` al
solicitar la creación de un kit de productos. Para esto, se solicita en
primer lugar la creación de un nuevo usuario o usuaria, y con el token 
de autenticación `authToken` se envía la solicitud y se crea un kit personal para 
este nuevo usuario/usuaria, variando el nombre del kit según la prueba.
## Pasos para ejecutar las pruebas
1. Dirigirse al archivo create_kit_name_kit_test.py
2. Verificar que los valores de prueba de la lista de comprobación al 
final del archivo coincidan con los estipulados para cada prueba.
3. Comprobar si la función es la correcta para cada prueba según su 
naturaleza positiva o negativa.
4. Verificar si el paquete 'pytest' se encuentra instalado y se encuentra 
en la barra superior.
5. Hacer clic en la flecha verde 'Run pytest' (también puede ejecutarse
el comando 'pytest' en la terminal).
6. Evaluar los resultados de las pruebas.