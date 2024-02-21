# expression-solver

Implements a recursive algorithm to evaluate any algebraic
expression.


  - Operators
                ○  Addition: +
                ○ Subtraction: -
                ○ Multiplication: *
                ○ Division: /
                ○ Grouping: ()
                    
  
  - Operands
  ○ Numerals: 32.436, 18.7, 42
  
  - The following would be valid expressions and their corresponding
  evaluations:
  ○ 3 + 12 * 3 / 12
  => 6
  ○ (3 + 3) * 42 / (6 + 12)
  => 14
  
  - The following would not be valid expressions:
  ○ 4 (12E)
   => Invalid Expression
  ○ 4 (41)
   => Invalid Expression
  ○ 42+43**271
   => Invalid Expression


## Built With

- Python

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Python

### Setup
- Clone Github repo: https://github.com/Bluette1/expression-solver

### Run tests

```
    python -m unittest discover --verbose -s ./test -p "*_test.py"
```

## Authors

👤 **Marylene Sawyer**
- Github: [@Bluette1](https://github.com/Bluette1)
- Twitter: [@MaryleneSawyer](https://twitter.com/MaryleneSawyer)
- Linkedin: [Marylene Sawyer](https://www.linkedin.com/in/marylene-sawyer)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check the [issues page](https://github.com/Bluette1/expression-solver/issues).

## Show your support

Give a ⭐️ if you like this project!


## 📝 License

This project is [MIT](https://opensource.org/licenses/MIT) licensed
