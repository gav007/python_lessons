# Maths with Python — Syllabus

## Goal

Learn the maths **and** use Python to make it visible, testable, and useful.

The aim is not to race through formulas or collect libraries. For each topic:

1. Understand the idea in plain English.
2. Work through a few small examples by hand.
3. Code the same idea in normal Python.
4. Introduce a library when it genuinely makes the next step easier.
5. Finish with a small capstone that combines the topic.

Most topics should have **3–4 warm-up files + 1 capstone**.

---

## Unit 1 — Number Skills

**Maths:** arithmetic, order of operations, negatives, fractions, percentages, powers and roots.

**Python:** variables, input, operators, formatting, simple functions.

**Library:** `math` near the end.

Warm-ups:
- [ ] Arithmetic and order of operations
- [ ] Fractions, percentages and ratios
- [x] Powers — started in `powers.py`
- [ ] Roots and useful functions from `math`

**Capstone:** Number Lab  
A small program where the user chooses an operation and Python shows the calculation and result.

---

## Unit 2 — Algebra

**Maths:** variables, expressions, equations, rearranging formulas, sequences.

**Python:** functions, parameters, return values and reusable formulas.

Warm-ups:
- [ ] Turn formulas into Python functions
- [ ] Solve simple one-step and two-step equations
- [ ] Rearrange and test formulas
- [ ] Generate simple number sequences

**Capstone:** Formula Toolkit  
A collection of small functions for real formulas such as speed, distance, time, averages or networking calculations.

---

## Unit 3 — Geometry and Trigonometry

**Maths:** area, perimeter, Pythagoras, angles, sine, cosine and tangent.

**Python:** combining formulas and validating user input.

**Library:** `math`

Warm-ups:
- [ ] Area and perimeter
- [ ] Pythagoras
- [ ] Degrees and radians
- [ ] Basic sine, cosine and tangent

**Capstone:** Triangle Calculator  
Enter known values and calculate useful sides, angles and measurements.

---

## Unit 4 — Functions and Graphs

**Maths:** coordinates, x and y, linear equations, slope, intercepts and how changing a formula changes a graph.

**Python:** lists, loops and generating data points.

**Library:** `matplotlib`

Warm-ups:
- [ ] Generate x/y coordinates
- [ ] Understand and code `y = mx + c`
- [ ] Make the first Matplotlib plot
- [ ] Plot and compare several functions

**Capstone:** Function Explorer  
Enter values such as slope and intercept and see the resulting line plotted.

---

## Unit 5 — Statistics

**Maths:** mean, median, mode, range, variance and standard deviation.

**Python:** working with collections of real data.

**Libraries:** `statistics`, then `matplotlib`

Warm-ups:
- [ ] Calculate mean and range manually
- [ ] Compare manual results with `statistics`
- [ ] Median, mode and spread
- [ ] Visualise a dataset

**Capstone:** Data Analyser  
Load a small dataset — for example ping times, sensor readings or marks — and produce useful statistics and a simple graph.

---

## Unit 6 — Probability

**Maths:** probability, outcomes, frequency and basic combinations.

**Python:** simulation and repeated experiments.

**Libraries:** `random`, useful parts of `math`

Warm-ups:
- [ ] Coins and dice
- [ ] Experimental vs expected probability
- [ ] Run hundreds or thousands of trials
- [ ] Basic combinations

**Capstone:** Probability Simulator  
Choose an experiment, simulate it many times and compare the result with the expected probability.

---

## Unit 7 — NumPy

This unit is about using faster mathematical tools **after the underlying maths makes sense**.

**Maths:** arrays, vectors, matrix basics and operations on groups of numbers.

**Library:** `numpy`

Warm-ups:
- [ ] Python lists vs NumPy arrays
- [ ] Array arithmetic
- [ ] Basic vectors
- [ ] Simple matrices

**Capstone:** Sensor Data Processor  
Use NumPy to process a larger set of readings and calculate useful values efficiently.

---

## Unit 8 — Deeper Algebra and Intro Calculus

This is a later unit. No need to rush here.

**Maths:** symbolic algebra, rate of change, derivatives and the basic idea of integration.

**Libraries:** `sympy`, `numpy`, `matplotlib`

Warm-ups:
- [ ] Symbolic expressions with SymPy
- [ ] Let SymPy solve equations we already understand manually
- [ ] Visualise rate of change
- [ ] Intro to derivatives

**Capstone:** Maths Explorer  
Take a function, plot it, solve useful points and explore how it changes.

---

## How to Work Through a Topic

A topic is not finished just because the program runs.

Before moving on, I should be able to:

- explain what the maths is doing in plain English;
- predict roughly what the answer should look like;
- write the important part of the code without copying the previous file;
- change the inputs and explain why the output changes;
- use the library as a tool rather than as a black box.

If a topic is difficult, add more warm-ups. If it is straightforward, three is enough.

The roadmap can change as the maths improves — this is a guide, not a race.
