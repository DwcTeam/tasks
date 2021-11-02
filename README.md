# Tasks

A simple package to make async task backgrond


## Installing 

Python 3.6 or higher is required

```bash
# Windows
pip install git+https://github.com/DwcTeam/tasks.git

# Linux/macOS
pip3 install git+https://github.com/DwcTeam/tasks.git
```

## Quick Example

```py
import tasks

async def printer(text: str):
    print(text)
 
task = tasks.Task(printer, intervel=2) 
task.start(text="lol")
```

## Links
- [Official Discord Server](https://discord.gg/VX5F54YNuy>`)

## Note
if you use my package please give me start 😭😭 
