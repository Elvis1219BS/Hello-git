# AGENTS.md - GitC Repository Guide for AI Coding Agents

## Project Summary
GitC is a simple Git learning repository designed to practice version control workflows. It contains minimal Python scripts without external dependencies, focused on educational purposes.

## Repository Structure
- **hellogit.py** - Basic hello world script
- **hellogit2.py** - Hello world variant 
- **calculator.py** - Interactive calculator (supports +, -, *, /)
- **.gitignore** - Git ignore configuration
- **README.md** - Full project documentation

## Running the Code
All Python scripts execute directly with no dependencies:
```bash
python hellogit.py      # Prints: Hello, GIT!
python hellogit2.py     # Prints: Hello, GIT2
python calculator.py    # Interactive calculator mode
```

## Development Conventions
- **Language**: Python 3
- **Style**: Simple, straightforward code for learning purposes
- **No external dependencies** - scripts only use Python stdlib
- **Naming**: Follow existing pattern (lowercase with descriptive names)

## When Adding New Features
1. Create `.py` files in the root directory following naming conventions
2. Keep scripts focused on one concept for educational clarity
3. Test with: `python script_name.py`
4. Add meaningful docstrings and comments
5. Update README.md with new script descriptions and usage

## Key Points for AI Agents
- This is an **educational repository** - prioritize clarity and simplicity over advanced patterns
- No build system, testing framework, or package manager needed
- Git operations (commits, branching, etc.) are the primary learning focus
- When modifying code, maintain the minimalist style that makes learning concepts clear
