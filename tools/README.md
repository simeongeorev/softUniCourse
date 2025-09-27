# SoftUni Course Tools

This directory contains utility scripts to help with SoftUni course development and exercise management.

## 📝 create_tasks.py

A Python script that creates completely empty Python exercise files from task names with automatic naming conversion.

### 🎯 **Script Features**

#### **Automatic Name Conversion**
- `"02. Person Info"` → `02_person_info.py`
- `"01. Hello World"` → `01_hello_world.py` 
- `"03. Calculate Area"` → `03_calculate_area.py`

#### **Usage Options**

##### **Interactive Mode** (most common)
```bash
python3 tools/create_tasks.py --folder fundamentals/new_lab
# Then type task names one by one
```

##### **Batch Mode** (for multiple tasks at once)
```bash
python3 tools/create_tasks.py --folder advanced/new_exercise --batch \
  "01. Stack Operations" \
  "02. Balanced Parentheses" \
  "03. Maximum Element"
```

##### **Current Directory**
```bash
python3 tools/create_tasks.py --batch "01. Task One" "02. Task Two"
```

### 🚀 **Quick Examples**

```bash
# Create files for a new lab
python3 tools/create_tasks.py -f fundamentals/18_new_topic_lab -b \
  "01. Basic Example" \
  "02. Advanced Example" \
  "03. Challenge Problem"

# Interactive mode for a new exercise folder
python3 tools/create_tasks.py -f advanced/08_new_exercise
# Then enter: "01. First Task", "02. Second Task", etc.

# Create files in current directory
cd fundamentals/19_new_lab
python3 ../../tools/create_tasks.py -b "01. First" "02. Second"
```

### 📁 **Generated Files**
Each file is created completely empty, ready for you to add your solution.

### ✅ **Features**
The script automatically:
- Creates directories if they don't exist
- Converts names to Python-friendly format
- Handles special characters and spaces
- Provides clear success/error feedback
- Shows summary of created files

### 📋 **Command Line Options**

```bash
python3 tools/create_tasks.py --help
```

**Options:**
- `--folder, -f`: Target folder to create files in (default: current directory)
- `--batch, -b`: Create files in batch mode with provided task names

### 💡 **Tips**

- Use **interactive mode** when you're not sure of all task names upfront
- Use **batch mode** when you have a complete list of tasks
- The script works from any directory - just adjust the path accordingly
- Task names can include any characters - the script handles the conversion automatically

Perfect for quickly setting up new SoftUni exercise folders! 🎉