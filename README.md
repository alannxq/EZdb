# kyna
 
an easier way to use json files in python. for now it has ~~two~~ ~~four~~ six methods, none of which are useful
 
## Installation

```Py
pip install kyna
```

## Usage

```Py 
import kyna

db = kyna.load("test.db") ## File will be made if it does not exist

db.set("name", "alan")
db.set("age", 17)

db.get("name") ## returns "alan"


db.getKeys() ## returns ["name", "age"]
db.getValues() ## returns ["alan", 17]


db.asDict() ## returns the file as a python dictionary

db.dump() ## saves any changes made
```
