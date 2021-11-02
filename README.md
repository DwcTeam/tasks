# Task

A simple package to make async task backgrond

## Example

```py
import tasks

async def printer(text: str):
    print(text)
 
task = tasks.Task(printer, intervel=2)  # function, timer 
task.start(text="lol")
```

*if you use my package please give me start 😭😭 
