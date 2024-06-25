# nt

## Estructura del Proyecto

   - checkout/
     - checkout.py
   - pricing_rules/
     - ex1.json
   - tests/
     - test_ex1.py
   - main.py

**`checkout/checkout.py`**: contiene la implementación principal del sistema de cobro (`Checkout`).

**`pricing_rules/ex1.json`**: archivo JSON que define las reglas de precios para los productos.

**`tests/test_ex1.py`**: archivo de pruebas unitarias utilizando `unittest` para verificar el correcto funcionamiento del sistema de cobro.

**`main.py`**: script principal que muestra un ejemplo de cómo utilizar el sistema de cobro para calcular el total de una compra.

## Checkout 
###### (checkout/checkout.py)
#### La clase `Checkout` maneja el cobro y aplica las reglas de descuento definidas.
#### Métodos principales:

   - `__init__(self, pricing_rules)`: inicializa una instancia de Checkout con reglas de precios específicas.
   - `scan(self, item)`: agrega un artículo escaneado a la lista de artículos.
   - `total(self)`: calcula el coste total de los artículos escaneados después de aplicar los descuentos según las reglas de precios.

#### Métodos estáticos:

   - `load_rules(file_path)`: carga las reglas de precios desde un archivo JSON y las convierte en un diccionario de reglas.

#### Métodos estáticos y privados:

   - `_apply_discount_2_for_1(price, count)`: aplica el descuento 2 por 1.
   - `_apply_discount_bulk(min_items, discount_amount, price, count)`: aplica el descuento por compra a granel.

## Reglas de precios
###### (pricing_rules/ex1.json)
Define las reglas de precios para cada producto disponible en la tienda, especificando qué descuentos disponibles hay y a qué artículo se asocia.
Pudiendo ser actualizables en cualquier momento.

## Pruebas unitarias
###### (tests/test_ex1.json)
Utiliza `unittest` para verificar el comportamiento esperado del sistema de cobro bajo diferentes escenarios de compra.

## Ejecución principal
###### (main.py)
Un ejemplo básico de cómo utilizar la clase Checkout para calcular el total de una compra.

## Arquitectura Propuesta

1. **Ingesta de datos:** 
   - Utilizando Apache Kafka para la captura en tiempo real y S3 / Azure Blob Storage para almacenamiento de archivos.

2. **Data Lake:**
   - Almacenamiento escalable en S3 / Azure Blob Storage para datos crudos antes de la transformación y carga en el Data Warehouse.

3. **Transformación de datos:**
   - AWS Glue para la realización y automatización del ETL, con soporte para datos estructurados y semi-estructurados.
   - PySpark para análisis de logs no estructurados de servidores.

4. **Data Warehouse:**
   - Almacenamiento centralizado y optimizado en Snowflake / Amazon Redshift para análisis avanzado de datos.

5. **Transformación con dbt:**
   - Definición de modelos SQL y tests para asegurar la calidad y consistencia de los datos transformados antes de la carga final.

6. **Carga a bases de datos:**
   - Scripts personalizados gestionados con Apache Airflow para la carga eficiente de datos en PostgreSQL, MongoDB, Redis, etc.

7. **Bases de Datos:**
   - PostgreSQL (p.ej.: gestión de datos de usuario y transacciones).
   - MongoDB (p.ej.: almacenamiento flexible y de rápido acceso a datos de inventario y logs de servidores).

#### Ventajas:
- **Escalabilidad:** esta arquitectura permite escalar horizontalmente cada componente según las necesidades de procesamiento y almacenamiento de datos.

- **Flexibilidad:** separar los datos en capas (ingesta, data lake, data warehouse y bases de datos finales) ofrece flexibilidad para crecer y adaptarse a nuevos requisitos sin tener que reestructurar toda la arquitectura.

#### Problemas:
- **Complejidad:** integrar múltiples tecnologías puede introducir complejidad operativa y requerir de habilidades concretas del equipo.
  
- **Consistencia y sincronización:** asegurar la consistencia entre los diferentes almacenamientos y bases de datos puede ser un desafío, especialmente en entornos distribuidos.

- **Seguridad:** garantizar la seguridad de los datos en todas las etapas del proceso.
