# **Adventure Text-Adventure Game**

This is a text-based adventure RPG game where players encounter enemies, manage their inventory, and navigate through a thrilling storyline. The game is built using Python and is highly customizable. This README file will guide you through the setup process, list the required packages, and explain any legal and ethical considerations.

---

## **Table of Contents**
- [Purpose](#purpose)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Required Files and Packages](#required-files-and-packages)
- [How to Play](#how-to-play)
- [Controls](#controls)
- [Licenses and Legal/Ethical Impacts](#licenses-and-legalethical-impacts)
- [Credits](#credits)

---

## **Purpose**

Adventure Text-Adventure Game is designed to immerse players in an interactive story-driven RPG experience. The game focuses on exploration, combat, and decision-making, allowing players to shape their journey. Through engaging gameplay and a dynamic storyline, players will encounter challenges that test their strategy and adaptability.

---

## **Features**

- **Interactive Combat System:** Engage with various enemies using strategic moves.
- **Inventory Management:** Collect, view, and use items to aid your journey.
- **Save and Load Progress:** Save your progress in JSON format and continue from where you left off.
- **Customizable Gameplay:** Adaptable and extendable code for future expansions.
- **Rich Storyline:** Navigate through a captivating narrative with multiple paths and outcomes.

---

## **System Requirements**

- **Operating System:** Windows, macOS, or Linux
- **Python Version:** Python 3.7 or higher
- **Memory:** At least 512 MB RAM
- **Storage:** 50 MB free space

---

## **Installation**

### **Prerequisites**
- **Python 3.x:** Ensure that you have Python installed. You can download it from [python.org](https://www.python.org).
- **Git (optional):** If you wish to clone the repository from GitHub.

### **Setting Up the Environment**

#### **1. Clone the Repository**
If using Git, clone the repository and navigate to the project folder:

```bash
git clone <repository-url>
cd <repository-folder>
```

### **2. Set Up Virtual Environment**
A virtual environment is recommended to manage dependencies without affecting your global Python setup:

```bash
python -m venv env
```

**Activate the Virtual Environment:**

- **Windows:**
  ```bash
  .\env\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source env/bin/activate
  ```

---

### **3. Install Dependencies**
Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

### **4. Run the Game**
Start the game by executing:

```bash
python main.py
```

---

## **Required Files and Packages**

### **Files**
- `main.py`: Main script to run the game.
- `player.py`: Manages the player's attributes, health, inventory, and game progress.
- `first_enemy.py`: Contains logic for the first enemy encounter.
- `savefile.json`: Automatically created file to store game progress.
- `requirements.txt`: Lists external packages required for the project.
- `README.md`: Setup, licensing, and project documentation.

**Note:** The test files are not necessary for the game to run.

### **Packages**
The following external libraries are required:

- **colorama:** Adds colored text and styles to terminal output.
- **json:** Built into Python; handles saving/loading game progress.
- **iniconfig:** Provides configuration support for pytest.
- **packaging:** Tools for packaging Python projects.
- **pluggy:** Plugin management for Python applications.
- **pytest:** Framework for writing and running tests.

---

## **How to Play**

### **Starting the Game**
Run `main.py` and follow the on-screen instructions to begin your adventure.

### **Inventory Management**
Add items to your inventory and view them using the appropriate commands.

### **Combat**
Engage in enemy battles where you can attack, dodge, and defeat enemies using your sword.

### **Saving/Loading Progress**
The game allows you to save your progress to a JSON file and load it at any time.

---

## **Controls**
- Enter numbers to make decisions (e.g., `1` for attack, `2` to check inventory, etc.).
- Follow the prompts and enjoy the interactive text-based adventure.

---

### **Licenses and Legal/Ethical Impacts**

This project leverages multiple open-source libraries, each governed by permissive licenses such as the MIT, BSD, and Apache 2.0 licenses. These licenses are integral to the open-source ecosystem, promoting collaboration, innovation, and transparency while ensuring legal protection for developers and users alike.

---

#### **License Overview and Texts:**

**MIT License**

**Summary:** The MIT License is highly permissive, allowing you to freely use, modify, and distribute the software, provided that the original license and copyright notice are included.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### **BSD License (2-Clause)**

**Summary:**  
The BSD 2-Clause License allows redistribution and use in source or binary forms, with minimal restrictions.  

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions, and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions, and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

### **Apache License 2.0**

**Summary:**  
The Apache License 2.0 permits use, distribution, and modification, provided that derivative works indicate changes made and the original copyright notice and license terms are preserved.  

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at arduino 
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
---

## **Credits**
- **Developer:** Evan Meehan
- **Special Thanks:** Python, open-source libraries, and the gaming community for inspiration.

---

Enjoy your adventure!
