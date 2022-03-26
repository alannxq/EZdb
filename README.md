# kyna

an easier way to use json files in python. for now it has ~~two~~ four methods, none of which are useful

## Installation

```Py
pip install kyna
```

## Usage

```Py
import kyna

db = kyna.load("test.db") ## File will be made if it does not exist

db.set("name", "alan")

db.get("name") ## returns "alan"

db.dump() ## saves any changes made

db.asDict() ## returns the file as a python dictionary
```
