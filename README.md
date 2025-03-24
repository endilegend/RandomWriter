# 📚 Character Probability Analysis & Text Generation – *The Time Machine*

This project performs a character-level statistical analysis of H.G. Wells’ *The Time Machine* to explore patterns in the text and generate new, random text based on those patterns. It begins with basic character frequency analysis and progresses toward more realistic text generation by modeling character transitions.

---

## 📌 Features

- **Level 0: Character Frequency Analysis**
  - Calculates the probability of each character appearing in the book.
  - Helps identify common characters (e.g., space, 'e') and rare ones (e.g., 'q').

- **Text Generation – Level 0**
  - Generates text using only the frequency of characters.
  - Characters are selected randomly based on global probability, with no context.

- **Level 1: Markov Chain Analysis (First-Order)**
  - Builds a transition probability model based on character-to-character sequences.
  - Generates text where the next character is chosen based on the current one.

- **Progressive Realism**
  - Each additional level (e.g., second-order Markov chains) produces more realistic-looking text.
  - Mimics style, tone, and rhythm of the original *The Time Machine* by H.G. Wells.

---

## 🧠 Concepts Practiced

- Probability distributions
- Histogram/frequency maps
- Markov chains (first-order and beyond)
- Randomized text generation
- Data-driven language modeling

---

## 📁 Input

- A text file containing the full content of *The Time Machine* (e.g., `the_time_machine.txt`).
- The program reads the text and performs analysis on a character level.

---

## 📄 Output

- A frequency table showing the probability of each character.
- Optionally: a heatmap or histogram of character appearances.
- Randomly generated text samples:
  - **Level 0**: Based on individual character probabilities.
  - **Level 1**: Based on transition probabilities between characters.

---

## 🚀 How to Run

1. Ensure you have Python 3 installed.
2. Place your source text file in the project directory (e.g., `the_time_machine.txt`).
3. Run the script:

```bash
python char_analysis.py
```

4. Review the generated text and frequency statistics in the console or output files.

---

## 🌐 Extensions

- Try building second-order or third-order Markov models for more realism.
- Visualize transition probabilities using graphs.
- Modify the generator to work on word-level analysis instead of character-level.

---

## ✍️ Author

Endi Troqe
