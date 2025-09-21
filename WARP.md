# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a SoftUni Python programming course repository containing educational exercises and projects across three skill levels: **Programming Basics**, **Programming Fundamentals**, and **Advanced**. The codebase is structured as a learning progression with hundreds of small Python exercises, each focusing on specific programming concepts.

## Architecture and Structure

### Learning Path Organization
- **`programming_basics/`** - Entry-level Python concepts (variables, conditions, loops)
- **`fundamentals/`** - Intermediate concepts (functions, lists, dictionaries, OOP, regex)
- **`advanced/`** - Advanced data structures (stacks, queues, sets, multidimensional lists)
- **`mario_tasks/`** - Special guided projects with detailed markdown instructions

### Exercise Structure Pattern
Each topic follows a consistent pattern:
- `XX_topic_lab/` - Guided practice exercises with basic implementations
- `XX_topic_exercise/` - Challenge problems for skill application
- Each directory contains:
  - `00-Topic-Name.docx` - Problem descriptions and requirements
  - Numbered Python files (`01_problem_name.py`, `02_next_problem.py`, etc.)

### Code Organization
- **Single-file exercises**: Each `.py` file contains a complete solution to one specific problem
- **Self-contained solutions**: No inter-file dependencies within exercise folders
- **Sequential numbering**: Files are numbered to indicate difficulty progression
- **Descriptive naming**: File names clearly indicate the problem being solved

## Development Commands

### Running Individual Exercises
```bash
# Run any specific exercise
python3 fundamentals/01_basic_syntax_conditions_loops_lab/01_number_definer.py

# Run from the exercise directory
cd fundamentals/08_functions_exercise
python3 09_password_validator.py
```

### Testing and Validation
```bash
# Test a single file with custom input
echo "test_input" | python3 path/to/exercise.py

# Verify Python syntax across multiple files
find . -name "*.py" -exec python3 -m py_compile {} \;

# Run a specific exercise with file input (if needed)
python3 exercise.py < input.txt
```

### Navigation and Discovery
```bash
# Find exercises by topic
find . -path "*stacks*" -name "*.py"
find . -path "*regex*" -name "*.py"

# List all lab vs exercise directories
find . -name "*_lab" -type d
find . -name "*_exercise" -type d

# Count exercises per topic
find fundamentals/ -name "*.py" | wc -l
```

### Utility Commands
```bash
# Format code consistently (if needed)
python3 -m black filename.py

# Check for common issues
python3 -m flake8 filename.py --ignore=E501,W503

# Run the name conversion utility
python3 pythonise_name.py
```

## Key Development Patterns

### Exercise Solution Structure
Most exercises follow this pattern:
```python path=null start=null
# Input handling
data = input()  # or multiple inputs

# Data processing/algorithm
result = process_data(data)

# Output formatting
print(result)
```

### Common Input Patterns
- Single value: `n = int(input())`
- Multiple values on one line: `a, b = map(int, input().split())`
- List of values: `numbers = list(map(int, input().split()))`
- Multiple lines until termination: Loop with break condition

### Algorithm Categories
- **Fundamentals**: Basic syntax, data types, control structures
- **Collections**: Lists, dictionaries, sets operations and manipulations  
- **Advanced Data Structures**: Stack/queue implementations using Python lists
- **String Processing**: Text manipulation, pattern matching, regex
- **Object-Oriented**: Class definitions, inheritance, encapsulation

## Exercise Execution Context

### Expected Runtime Environment
- **Python 3.x** (no version-specific dependencies)
- Standard library only (no external packages)
- Console-based I/O (input/print functions)
- No file persistence between exercises

### Input/Output Expectations
- All exercises expect console input via `input()`
- Output uses `print()` with specific formatting requirements
- No interactive menus or GUI components
- Results should match exact format specified in problem descriptions

### Common Debugging Approaches
- Add debug prints: `print(f"Debug: {variable}", file=sys.stderr)`
- Test with edge cases: empty input, single elements, large numbers
- Verify algorithm logic step-by-step with small examples
- Check off-by-one errors in list indexing and range operations

## Learning Progression Notes

The repository follows SoftUni's structured curriculum where:
- **Labs** introduce concepts with guided examples
- **Exercises** test independent problem-solving ability  
- **Exams** simulate real assessment conditions with time constraints
- **Mario Tasks** provide project-based learning with detailed instructions

Each level builds upon previous knowledge, so understanding the progression helps when working across different difficulty levels.