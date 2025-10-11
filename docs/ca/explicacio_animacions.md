# Explicació de les animacions

**🌐 Idioma / Language:** [Català](explicacio_animacions.md) | [English](../en/installation_guide.md)

Aquest document descriu breument el contingut i l'objectiu pedagògic de cadascuna de les animacions creades amb **ManimCE** per al Treball de Recerca  
"Demostracions matemàtiques visuals de la ESO: un enfocament accessible amb eines digitals".

---

## 1️⃣ Identitats notables

### 1.1 Quadrat d'una suma

**Fitxer**: `src/algebraic_identities.py` (classe: `SumSquare`)

**Fórmula visualitzada**:  
`(a + b)² = a² + 2ab + b²`

**Què mostra**:  
Combinació d'àrees de quadrats i rectangles per veure clarament d'on surt aquesta identitat.

**Objectiu pedagògic**:  
Fer visible com, sumant àrees, apareixen els termes `a²`, `2ab` i `b²`.

---

### 1.2 Quadrat d'una diferència

**Fitxer**: `src/algebraic_identities.py` (classe: `DifferenceSquare`)

**Fórmula visualitzada**:  
`(a - b)² = a² - 2ab + b²`

**Què mostra**:  
La mateixa construcció que abans però amb diferència, mostrant com canvia el signe del terme central.

**Objectiu pedagògic**:  
Reforçar la idea que només canvia el signe del terme mixt i que això té una interpretació geomètrica.

---

### 1.3 Producte d'una suma i una diferència

**Fitxer**: `src/algebraic_identities.py` (classe: `SumDifferenceProduct`)

**Fórmula visualitzada**:  
`(a + b)(a - b) = a² - b²`

**Què mostra**:  
Com es construeix visualment la diferència de quadrats a partir d'un rectangle gran menys un altre petit.

**Objectiu pedagògic**:  
Mostrar de manera intuïtiva la fórmula de la diferència de quadrats.

---

## 2️⃣ Àrea del triangle (tres casos)

### 2.1 Triangle amb altura interior

**Fitxer**: `src/triangle_area.py` (classe: `TriangleAreaInteriorAltitude`)

**Fórmula visualitzada**:  
`Àrea = (base × altura) / 2`

**Què mostra**:  
Animació que demostra com la fórmula de l'àrea es compleix quan l'altura cau dins del triangle, mitjançant la descomposició del triangle en dos triangles rectangles i la seva reorganització.

**Objectiu pedagògic**:  
Mostrar geomètricament per què la fórmula de l'àrea funciona per a triangles acutangles on l'altura interseca la base entre els seus extrems.

---

### 2.2 Triangle amb altura exterior

**Fitxer**: `src/triangle_area.py` (classe: `TriangleAreaExteriorAltitude`)

**Fórmula visualitzada**:  
`Àrea = (base × altura) / 2`

**Què mostra**:  
Animació que demostra com la fórmula de l'àrea segueix sent vàlida fins i tot quan l'altura cau fora del triangle, utilitzant la diferència entre àrees de triangles rectangles més grans.

**Objectiu pedagògic**:  
Il·lustrar que la fórmula de l'àrea es generalitza per a triangles obtusangles on l'altura cau fora del segment de la base.

---

### 2.3 Triangle a partir de la divisió d'un rectangle

**Fitxer**: `src/triangle_area.py` (classe: `TriangleAreaRectangle`)

**Fórmula visualitzada**:  
`Àrea = (base × altura) / 2`

**Què mostra**:  
Derivació visual que mostra com qualsevol triangle es pot entendre com la meitat d'un rectangle o paral·lelogram amb la mateixa base i altura.

**Objectiu pedagògic**:  
Proporcionar la prova geomètrica més intuïtiva que l'àrea d'un triangle és sempre la meitat de la d'un rectangle amb les mateixes mesures de base i altura.

---

## 3️⃣ Teorema de Pitàgores

**Fitxer**: `src/pythagorean_theorem.py` (classe: `PythagoreanTheorem`)

**Fórmula visualitzada**:  
`c² = a² + b²`

**Què mostra**:  
Construeix el quadrat sobre la hipotenusa i sobre els catets, col·loca quatre triangles congruents i fa aparèixer visualment el quadrat central d'àrea `c²`.

**Objectiu pedagògic**:  
Fer visible la descomposició d'àrees i la igualtat de superfícies, que és la base geomètrica del teorema.

---

## 4️⃣ Fórmula de l'equació de segon grau

**Fitxer**: `src/quadratic_equation.py` (classe: `QuadraticFormula`)

**Fórmula visualitzada**:  
`x = [-b ± √(b² - 4ac)] / 2a`

**Què mostra**:  
Guia pas a pas el procés d'"acabar el quadrat" fins a obtenir la fórmula general de l'equació de segon grau.

**Objectiu pedagògic**:  
Fer explícit el raonament algebraic amb suport visual, mostrant que la fórmula és una conseqüència directa de completar el quadrat.

---

## ℹ️ Notes finals

- Totes les animacions comparteixen un estil visual coherent (colors, ritme, tipografies) per reforçar la claredat.
- Les variables i comentaris del codi estan en anglès per seguir les convencions de Python/ManimCE i facilitar la comprensió a nivell internacional.

---

**🌐 Idioma / Language:** [Català](explicacio_animacions.md) | [English](../en/installation_guide.md)
