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

## Programa principal
###### (main.py)
Un ejemplo básico de cómo utilizar la clase Checkout para calcular el total de una compra.

## Ejecución
1. Clonar el repositorio: clona este repositorio en tu máquina local.
2. Ejecutar pruebas: ejecuta las pruebas unitarias en tests/test_ex1.py para verificar que todo funcione como se espera.
3. Uso del programa principal: utiliza `main.py` como punto de entrada para integrar el sistema de cobro en tu aplicación.

## Notas
- Asegúrate de tener Python instalado para ejecutar el proyecto.
- Puedes ajustar las reglas de precios en pricing_rules/ex1.json según los requisitos específicos del momento.
