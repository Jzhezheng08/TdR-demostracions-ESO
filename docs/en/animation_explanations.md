# Explanation of Animations

**🌐 Language / Idioma:** [English](animation_explanations.md) | [Català](../ca/guia_execucio.md)

This document briefly describes the content and pedagogical objective of each animation created with **ManimCE** for the research project  
"Visual Mathematical Proofs for Secondary Education: An Accessible Approach with Digital Tools".

---

## 1️⃣ Algebraic Identities

### 1.1 Square of a Sum

**File**: `src/algebraic_identities.py` (class: `SumSquare`)

**Visualized formula**:  
`(a + b)² = a² + 2ab + b²`

**What it shows**:  
Combination of areas of squares and rectangles to clearly see where this identity comes from.

**Pedagogical objective**:  
Make visible how, by adding areas, the terms `a²`, `2ab` and `b²` appear.

---

### 1.2 Square of a Difference

**File**: `src/algebraic_identities.py` (class: `DifferenceSquare`)

**Visualized formula**:  
`(a - b)² = a² - 2ab + b²`

**What it shows**:  
The same construction as before but with a difference, showing how the sign of the central term changes.

**Pedagogical objective**:  
Reinforce the idea that only the sign of the mixed term changes and that this has a geometric interpretation.

---

### 1.3 Product of a Sum and a Difference

**File**: `src/algebraic_identities.py` (class: `SumDifferenceProduct`)

**Visualized formula**:  
`(a + b)(a - b) = a² - b²`

**What it shows**:  
How the difference of squares is visually constructed from a large rectangle minus a smaller one.

**Pedagogical objective**:  
Intuitively show the formula for the difference of squares.

---

## 2️⃣ Area of a Triangle (Three Cases)

### 2.1 Triangle with Interior Height

**File**: `src/triangle_area.py` (class: `TriangleAreaInteriorAltitude`)

**Visualized formula**:  
`Area = (base × height) / 2`

**What it shows**:  
Animation demonstrating how the area formula holds when the altitude falls within the triangle, by decomposing the triangle into two right triangles and rearranging them.

**Pedagogical objective**:  
Show geometrically why the area formula works for acute triangles where the altitude intersects the base between its endpoints.

---

### 2.2 Triangle with Exterior Height

**File**: `src/triangle_area.py` (class: `TriangleAreaExteriorAltitude`)

**Visualized formula**:  
`Area = (base × height) / 2`

**What it shows**:  
Animation demonstrating how the area formula remains valid even when the altitude falls outside the triangle, using the difference between areas of larger right triangles.

**Pedagogical objective**:  
Illustrate that the area formula generalizes to obtuse triangles where the altitude lands outside the base segment.

---

### 2.3 Triangle from Rectangle Division

**File**: `src/triangle_area.py` (class: `TriangleAreaRectangle`)

**Visualized formula**:  
`Area = (base × height) / 2`

**What it shows**:  
Visual derivation showing how any triangle can be seen as half of a rectangle or parallelogram with the same base and height.

**Pedagogical objective**:  
Provide the most intuitive geometric proof that a triangle's area is always half that of a rectangle with identical base and height measurements.

---

## 3️⃣ Pythagorean Theorem

**File**: `src/pythagorean_theorem.py` (class: `PythagoreanTheorem`)

**Visualized formula**:  
`c² = a² + b²`

**What it shows**:  
Constructs the square on the hypotenuse and on the legs, places four congruent triangles, and visually reveals the central square of area `c²`.

**Pedagogical objective**:  
Make visible the decomposition of areas and the equality of surfaces, which is the geometric basis of the theorem.

---

## 4️⃣ Quadratic Formula

**File**: `src/quadratic_equation.py` (class: `QuadraticFormula`)

**Visualized formula**:  
`x = [-b ± √(b² - 4ac)] / 2a`

**What it shows**:  
Guides step by step through the process of "completing the square" until obtaining the general formula of the quadratic equation.

**Pedagogical objective**:  
Make explicit the algebraic reasoning with visual support, showing that the formula is a direct consequence of completing the square.

---

## ℹ️ Final Notes

- All animations share a consistent visual style (colors, rhythm, typography) to enhance clarity.
- Variables and code comments are in English to follow Python/ManimCE conventions and facilitate international understanding.

---

**🌐 Language / Idioma:** [English](animation_explanations.md) | [Català](../ca/guia_execucio.md)
