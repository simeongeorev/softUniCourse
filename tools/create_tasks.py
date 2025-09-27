#!/usr/bin/env python3
"""
Task File Creator for SoftUni Exercises

This script creates empty Python files from task names with automatic naming conversion.
Converts names like "02. Person Info" to "02_person_info.py"

Usage:
    python3 create_tasks.py
    python3 create_tasks.py --folder custom_folder
    python3 create_tasks.py --batch "01. Task One" "02. Task Two"
"""

import sys
import re
import argparse
from pathlib import Path


def pythonise_name(name):
    """
    Convert task name to Python-friendly filename.
    Example: "02. Person Info" -> "02_person_info"
    """
    # Convert to lowercase
    name = name.lower()
    
    # Replace spaces and punctuation with underscores
    name = re.sub(r'[.\s\-]+', '_', name)
    
    # Remove special characters that aren't allowed in filenames
    name = re.sub(r'[^\w_]', '', name)
    
    # Remove multiple consecutive underscores
    name = re.sub(r'_+', '_', name)
    
    # Remove leading/trailing underscores
    name = name.strip('_')
    
    return name


def create_task_file(task_name, folder_path):
    """
    Create an empty Python file for the given task name in the specified folder.
    
    Args:
        task_name (str): Original task name (e.g., "02. Person Info")
        folder_path (Path): Directory to create the file in
    
    Returns:
        Path: Path to the created file
    """
    # Convert name to Python filename
    python_name = pythonise_name(task_name)
    file_path = folder_path / f"{python_name}.py"
    
    # Create folder if it doesn't exist
    folder_path.mkdir(parents=True, exist_ok=True)
    
    # Create empty file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            pass  # Create empty file
        print(f"✅ Created: {file_path}")
        return file_path
    except Exception as e:
        print(f"❌ Error creating {file_path}: {e}")
        return None


def interactive_mode(folder_path):
    """Interactive mode to create tasks one by one."""
    print(f"📁 Target folder: {folder_path.absolute()}")
    print("🔄 Interactive Task Creator (type 'quit' or 'exit' to stop)")
    print("📝 Enter task names (e.g., '01. Hello World', '02. Person Info')")
    print()
    
    created_files = []
    
    while True:
        try:
            task_name = input("Task name: ").strip()
            
            if not task_name:
                continue
                
            if task_name.lower() in ['quit', 'exit', 'q']:
                break
                
            file_path = create_task_file(task_name, folder_path)
            if file_path:
                created_files.append(file_path)
                
        except KeyboardInterrupt:
            print("\n\n🛑 Interrupted by user")
            break
        except EOFError:
            break
    
    print(f"\n📊 Summary: Created {len(created_files)} files")
    return created_files


def batch_mode(task_names, folder_path):
    """Batch mode to create multiple tasks at once."""
    print(f"📁 Target folder: {folder_path.absolute()}")
    print(f"📦 Creating {len(task_names)} task files...")
    print()
    
    created_files = []
    
    for task_name in task_names:
        file_path = create_task_file(task_name, folder_path)
        if file_path:
            created_files.append(file_path)
    
    print(f"\n📊 Summary: Created {len(created_files)} files")
    return created_files


def main():
    parser = argparse.ArgumentParser(
        description="Create empty Python files for SoftUni exercises with automatic naming conversion",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 create_tasks.py                           # Interactive mode in current directory
  python3 create_tasks.py --folder lab_exercises    # Interactive mode in specific folder
  python3 create_tasks.py --batch "01. Task One"    # Create one file
  python3 create_tasks.py --batch "01. First" "02. Second"  # Create multiple files
  
The script converts task names to Python-friendly filenames:
  "01. Hello World" -> "01_hello_world.py"
  "02. Person Info" -> "02_person_info.py"
        """
    )
    
    parser.add_argument(
        '--folder', '-f',
        type=str,
        default='.',
        help='Target folder to create files in (default: current directory)'
    )
    
    parser.add_argument(
        '--batch', '-b',
        nargs='*',
        help='Create files in batch mode with provided task names'
    )
    
    args = parser.parse_args()
    
    # Setup folder path
    folder_path = Path(args.folder).resolve()
    
    # Determine mode
    if args.batch is not None:
        if not args.batch:
            print("❌ Error: --batch flag provided but no task names given")
            sys.exit(1)
        created_files = batch_mode(args.batch, folder_path)
    else:
        created_files = interactive_mode(folder_path)
    
    # Final summary
    if created_files:
        print("\n✨ All done! Files created:")
        for file_path in created_files:
            print(f"   {file_path}")
    else:
        print("\n📝 No files were created")


if __name__ == "__main__":
    main()