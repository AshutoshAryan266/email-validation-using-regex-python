# Email Validation Using Regex (Python)

This project validates email addresses using **Regular Expressions (regex)** in Python.
It is an improved version of my earlier email validation program which was implemented
using only `if-else` conditions.

The goal of this project is not just validation, but to demonstrate **why regex is a
better and cleaner solution** for pattern-based problems like email validation.

---

## 🚀 Features

- Validates email format using regex
- Ensures email starts and ends correctly
- Prevents invalid characters
- Disallows consecutive dots (`..`)
- Lightweight and beginner-friendly
- Command-line based program

---

## 🧠 Email Format Rules Used

An email is considered valid if it follows this structure:


### Rules applied:
- Email must start with an alphabet
- Only alphabets, digits, `_`, `.`, and `$` are allowed in the local part
- Exactly one `@` symbol is required
- Domain must start with an alphabet
- A dot (`.`) must separate domain and TLD
- TLD must contain **at least 2 alphabets**
- No spaces allowed
- No consecutive dots (`..`) allowed

---

## ❌ Problem With My Earlier Approach (Using if–else)

In my earlier email validation program, I used **nested if–else conditions** to validate
each rule separately.

### Demerits of that approach:
- Code became **too long and hard to read**
- Too many nested conditions made logic confusing
- Difficult to maintain or modify
- Hard to visualize the overall email structure
- Error-prone when adding new rules
- Not scalable for complex patterns

In short, the logic worked, but the **design was inefficient**.

---

## ✅ How Regex Solves These Problems

Using **Regular Expressions**, the entire email structure can be validated in **one
clean pattern**.

### Advantages of regex:
- Compact and readable pattern
- Easy to enforce start (`^`) and end (`$`) rules
- Perfect for pattern matching problems
- Less code, more clarity
- Easier to maintain and extend
- Industry-standard solution

Regex allowed me to replace dozens of conditional checks with **one meaningful pattern**.

---

## 🧪 Regex Pattern Used

```python
^[a-zA-Z][a-zA-Z0-9._$]*@[a-zA-Z][a-zA-Z0-9]*\.[a-zA-Z]{2,}$
