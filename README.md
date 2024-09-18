# **Adventure RPG Game**

This is a text-based adventure RPG game where players encounter enemies, manage their inventory, and navigate through a thrilling storyline. The game is built using Python and is highly customizable. This README file will guide you through the setup process, list the required packages, and explain any legal and ethical considerations.

---

## **Table of Contents**
- [Installation](#installation)
- [Required Files and Packages](#required-files-and-packages)
- [Licenses and Legal/Ethical Impacts](#licenses-and-legalethical-impacts)
- [How to Play](#how-to-play)
- [Credits](#credits)

---

## **Installation**

### **Prerequisites**
- **Python 3.x**: Ensure that you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Git** (optional): If you wish to clone the repository from GitHub.

### **Setting Up the Environment**

1. **Clone the repository** (if using Git):
   git clone <repository-url>
   cd <repository-folder>

### **Install the required packages**

**We recommend using a virtual environment for package management. Run the following commands to create and activate a virtual environment:**

``` python -m venv env ```

``` source env/bin/activate    # For Windows use: .\env\Scripts\activate ```

**Install required Python packages:**

Once inside the virtual environment, run the following command to install the necessary libraries:

```pip install -r requirements.txt```

**Run the game:**

To start the game, simply execute the following command in your terminal or command prompt:

```python main.py```

### **Required Files and Packages**

#### **Files**
- `main.py`: This is the main script to run the game.
- `player.py`: Manages the player's attributes, health, inventory, and game progress.
- `first_enemy.py`: Contains logic for the first enemy encounter
- `savefile.json`: Stores game progress (automatically created when saving the game).
- `requirements.txt`: Contains the list of external packages required for the project.
- `README.md`: This file, which contains setup, licensing, and project documentation.

- The test files are not necessary for the game to run

## Packages

The following external libraries are required for the project:

### colorama

- **Purpose:** Adds colored text and styles to the terminal output.
- **Installation:** `pip install colorama`
- **License:** BSD License - This permissive license allows free use, modification, and distribution of the software. However, it comes with no warranty.
- **Legal and Ethical Impacts:** This license allows the package to be used in both open-source and proprietary projects. It encourages innovation and sharing while ensuring legal protection against claims related to the software's use.

### json (built into Python)

- **Purpose:** Handles saving and loading game progress in JSON format.
- **License:** Part of Python's standard library, covered by the PSF License.
- **Legal and Ethical Impacts:** The PSF License is open-source and widely accepted for use. It encourages ethical software development with freedom to use, modify, and distribute Python's functionality.

### iniconfig

- **Purpose:** Provides configuration support for pytest.
- **Installation:** `pip install iniconfig`
- **License:** MIT License - Allows free use, modification, and distribution of the software with a disclaimer of warranty.
- **Legal and Ethical Impacts:** Promotes open-source collaboration while providing legal protection for the software's use.

### packaging

- **Purpose:** Tools for packaging and distributing Python projects.
- **Installation:** `pip install packaging`
- **License:** Apache License 2.0 - Permissive license allowing use, modification, and distribution of the software.
- **Legal and Ethical Impacts:** Encourages innovation and sharing with a focus on protecting contributors' rights and ensuring legal clarity.

### pluggy

- **Purpose:** Provides plugin management for Python applications.
- **Installation:** `pip install pluggy`
- **License:** MIT License - Allows nearly unrestricted freedom to use, modify, and distribute the software with a disclaimer of liability.
- **Legal and Ethical Impacts:** Widely used in open-source projects, ensuring flexibility in usage and modification while offering protection against legal claims.

### pytest

- **Purpose:** Framework for writing and running tests.
- **Installation:** `pip install pytest`
- **License:** MIT License - Permissive license allowing freedom to use, modify, and distribute with a disclaimer of liability.
- **Legal and Ethical Impacts:** Promotes software quality and testing while providing legal protection for contributors and users.

## How to Play

### Starting the Game
Run `main.py` and follow the on-screen instructions to begin your adventure.

### Inventory Management
Add items to your inventory and view them using the appropriate commands.

### Combat
Engage in enemy battles where you can attack, dodge, and defeat enemies using your sword.

### Saving/Loading Progress
The game allows you to save your progress to a JSON file and load it at any time.

## Controls

- Enter numbers to make decisions (e.g., `1` for attack, `2` to check inventory, etc.).
- Follow the prompts and enjoy the interactive text-based adventure.

## Credits

- **Developer:** Evan Meehan
- **Special Thanks:** Python, open-source libraries (colorama, typewrite), and the gaming community for inspiration.
