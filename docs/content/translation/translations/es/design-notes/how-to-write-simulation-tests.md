# Cómo Escribir Pruebas de Simulación

Esta guía explica cómo añadir nuevas pruebas de simulación al simulador constitucional de flujo para que otras personas colaboradoras puedan crear escenarios de forma consistente.

El simulador no es un sistema difuso de razonamiento con IA. Es un ejecutor determinista de escenarios.

Cada prueba suele tener cuatro partes:

1. un archivo JSON de escenario
2. uno o más controladores de eventos
3. salidas de informe generadas
4. actualizaciones posteriores de la documentación

---

## 1. Empiece con una Ruta Real de Tensión Constitucional

No empiece inventando un tipo de evento aleatorio.

Empiece con una pregunta concreta, por ejemplo:

- ¿Qué ocurre si un presidente prolonga por decreto un arancel de emergencia ya vencido?
- ¿Qué ocurre si un estado niega el reconocimiento parental a una familia del mismo sexo?
- ¿Qué ocurre si un órgano constitucional incumple un plazo de puesta en marcha?
- ¿Qué ocurre si una plataforma dominante corta el acceso de un actor político lícito durante una elección?

Luego defina:

- las disposiciones constitucionales que se están poniendo a prueba
- la institución de la que se espera que actúe
- la consecuencia constitucional esperada
- si debe subsistir algún cuello de botella

Los mejores escenarios prueban un modo de fallo conocido, no solo un mal resultado en abstracto.

---

## 2. Decida si se Trata de un Escenario Nuevo o de una Nueva Familia de Escenarios

Si el escenario encaja en un área ya existente, amplíe el módulo de controladores correspondiente.

Las áreas comunes de controladores son:

- [executive.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/executive.py)
- [legislative.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/legislative.py)
- [judiciary.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/judiciary.py)
- [rights.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/rights.py)
- [federalism.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/federalism.py)
- [integrity.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/integrity.py)
- [transition.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/transition.py)
- [social_rights.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/social_rights.py)
- [fiscal.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/fiscal.py)

Si el escenario introduce un dominio realmente nuevo, añada un nuevo módulo de controladores y regístrelo en [dispatcher.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/dispatcher.py).

---

## 3. Cree el JSON del Escenario

Los archivos de escenario se encuentran en [simulation/scenarios](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios).

Utilice un archivo existente como modelo.

Buenos ejemplos de referencia:

- [emergency-revenue-measure-unilateral-extension.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/emergency-revenue-measure-unilateral-extension.json)
- [family-status-discrimination-parental-recognition.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/family-status-discrimination-parental-recognition.json)
- [constitutional-organ-bridge-startup.json](/Users/chris/Documents/GitHub/The-Constitution/simulation/scenarios/constitutional-organ-bridge-startup.json)

Un archivo de escenario debe incluir:

- `id`
- `title`
- `description`
- `articles_tested`
- `provisions_tested`
- `events`

Estructura típica:

```json
{
  "id": "example-scenario",
  "title": "Short Human Title",
  "description": "One paragraph explaining the stress path and what the scenario is testing.",
  "articles_tested": ["Article V"],
  "provisions_tested": ["Article V Section 2.1", "Article V Section 2.6"],
  "events": [
    {
      "day": 0,
      "type": "some_event_type",
      "actor": "President",
      "details": {
        "key": "value"
      }
    },
    {
      "day": 3,
      "type": "some_followup_event",
      "actor": "Federal courts"
    }
  ]
}
```

Pautas:

- mantenga el orden cronológico de los eventos
- mantenga los títulos breves y legibles
- haga que las descripciones expliquen explícitamente qué cuestión constitucional se está poniendo a prueba
- enumere las disposiciones reales que deberían controlar el escenario

---

## 4. Elija Buenos Tipos de Evento

Los tipos de evento deben describir acciones o fallos constitucionales significativos, no estados de ánimo vagos.

Buenos:

- `president_orders_emergency_revenue_measure_continued`
- `court_voids_unilateral_emergency_revenue_extension`
- `state_denies_parental_recognition`

Malos:

- `government_does_bad_thing`
- `court_acts`
- `problem_happens`

Si un nuevo tipo de evento es demasiado amplio, los escenarios futuros resultan difíciles de razonar y la lógica del controlador se vuelve confusa.

---

## 5. Implemente o Amplíe la Lógica del Controlador

El simulador procesa los eventos mediante registros de controladores.

El registro despachador se encuentra en [dispatcher.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/dispatcher.py).

Cada módulo de controladores exporta un mapa `HANDLERS` indexado por tipo de evento.

Patrón típico:

```python
HANDLERS = {
    "some_event_type": handle_some_event,
}
```

Dentro de un controlador, el código suele hacer alguna combinación de lo siguiente:

- añadir una entrada a la cronología
- activar una disposición constitucional
- crear una obligación con un plazo
- resolver o incumplir una obligación
- registrar un cuello de botella
- registrar una categoría de infracción o patrón de riesgo

Al añadir lógica de controladores:

- manténgala determinista
- nombre explícitamente las disposiciones activadas
- mantenga el resultado ligado al diseño constitucional real
- no introduzca silenciosamente supuestos de política pública que no estén fundados en el borrador

Si necesita un módulo nuevo:

1. añada el archivo en [simulation/handlers](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers)
2. exporte un mapeo `HANDLERS`
3. registre ese mapeo en [dispatcher.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/handlers/dispatcher.py)

---

## 6. Ejecute el Escenario

Listar escenarios:

```bash
python3 simulation/run.py --list
```

Ejecutar un escenario:

```bash
python3 simulation/run.py --summary simulation/scenarios/example-scenario.json
```

Ejecutar todos los escenarios y guardar salidas:

```bash
python3 simulation/run.py --all --out-dir simulation/reports --save-full --save-json --save-aggregate
```

Salidas útiles:

- `.full.md` para revisión humana
- `.summary.json` para resultados estructurados
- `aggregate.json` para la línea base del conjunto completo

El ejecutor está en [run.py](/Users/chris/Documents/GitHub/The-Constitution/simulation/run.py).

---

## 7. Interprete Correctamente el Resultado

Un escenario debe indicarle:

- qué disposiciones se activaron
- qué obligaciones se crearon
- qué obligaciones se cumplieron
- si se produjeron infracciones
- si permanecen cuellos de botella
- si alguna obligación quedó sin resolver

Distinción importante:

- una `violation` suele significar que el escenario modeló con éxito una conducta indebida
- una `unresolved_obligation` es un problema de diseño más serio porque la Constitución no logró completar una cadena de consecuencias requerida

La meta del diseño no es tener cero infracciones en todos los escenarios. Muchos escenarios comienzan intencionalmente con conductas ilícitas.

La verdadera meta es:

- enrutamiento constitucional claro
- deberes exigibles
- cierre limpio de la cadena de consecuencias
- `0` obligaciones no resueltas

---

## 8. Actualice el Catálogo de Escenarios

Después de añadir una prueba, actualice [test-scenarios.md](/Users/chris/Documents/GitHub/The-Constitution/design-notes/test-scenarios.md).

Añada:

- categoría
- nombre del escenario
- nombre del archivo
- disposición
- ruta de tensión
- resultado esperado

El catálogo es el inventario público de lo que se ha probado y de lo que todavía no.

---

## 9. Actualice los Hallazgos si el Escenario Aporta Algo

Si el nuevo escenario:

- valida una disposición antes incierta
- expone una brecha real
- cambia la forma en que debe puntuarse un artículo
- aclara que un cuello de botella es aceptable o inaceptable

entonces actualice:

- [simulation-findings.md](/Users/chris/Documents/GitHub/The-Constitution/design-notes/simulation-findings.md)
- y en ocasiones [scorecard.md](/Users/chris/Documents/GitHub/The-Constitution/design-notes/scorecard.md)

No actualice la hoja de puntuación de manera mecánica solo porque exista una prueba nueva.
Actualícela cuando la prueba cambie materialmente la confianza en el artículo.

---

## 10. Qué Hace Bueno a un Escenario

Un escenario sólido:

- prueba con claridad un sistema constitucional
- utiliza una ruta de tensión realista
- nombra las disposiciones realmente controladoras
- produce un resultado esperado legible
- aísla si el problema es:
  - una infracción
  - un cuello de botella
  - una brecha estructural
  - un riesgo político residual aceptable

Un escenario débil:

- intenta probar demasiados sistemas a la vez
- usa nombres de eventos vagos
- asume resultados sin respaldo del controlador
- trata todos los hechos negativos como fracaso constitucional

---

## 11. Flujo de Trabajo Recomendado

El flujo de trabajo más seguro es:

1. elegir una pregunta constitucional real
2. encontrar el escenario existente más cercano
3. crear el nuevo JSON del escenario
4. ampliar o añadir la lógica del controlador
5. ejecutar primero ese escenario individual
6. inspeccionar el resumen y el informe completo
7. ejecutar el conjunto completo
8. actualizar el catálogo y los hallazgos

Esto mantiene el escenario comprensible y reduce la probabilidad de añadir una prueba que parezca buena pero que en realidad no esté conectada al sistema.

---

## 12. Lista Rápida para Personas Colaboradoras

- ¿Definí una ruta real de tensión constitucional?
- ¿Nombré las disposiciones reales que se están poniendo a prueba?
- ¿Usé tipos de evento claros?
- ¿Añadí o actualicé la lógica del controlador?
- ¿El escenario se ejecutó sin obligaciones no resueltas, salvo que esté exponiendo deliberadamente una brecha?
- ¿Actualicé `test-scenarios.md`?
- ¿Actualicé los hallazgos o la hoja de puntuación si el resultado cambió la confianza del proyecto?

Si la respuesta es sí a todo eso, el escenario probablemente esté listo.
