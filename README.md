# EasyGoDB
A simple key-value database for Python managed by files.
```python
# import the database module
import EasyGoDB as db
# retrieve the help menu
db.help()
# create a key and its value
db.create(key="key", value="value")
# update a key and its value
db.update(old_key="key", new_key="obj", new_value=100)
# get the value of a key
db.get(key="obj")
# delete a key and its value
db.delete(key="obj")
# change a key
db.change_key(old_key="key", new_key="obj")
# change a value (of a key)
db.change_value(key="obj", new_value=50)
# get all keys and their values
db.get_all()
# delete all keys and their values
db.delete_all()
```
