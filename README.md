# Metaflow Cards

This repository consists of the implementation of custom metaflow `@card` templates; 


### How To Create Your Own Cards
`MetaflowCard`s use a [pkgutil style namespace package definition](https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages) to allow users to make custom installable cards. Create your own custom installable `MetaflowCard` by creating a Python package with the following folder structure -
```
your_custom_card_repo/ # the name of this dir doesn't matter
├ setup.py
├ metaflow_cards/ # namespace package name
│  └ __init__.py       # special pkgutil namespace __init__.py
│  └ my_card_package_name/      # namespace sub package name : dir name must match the package name in `setup.py`
│      └__init__.py  # Should contain a CARDS attribute which is a List of MetaflowCard's
│      └ your-card.py # Implements the MetaflowCard class. 
```
The `your_custom_card_repo/metaflow_cards/my_card_package_name/__init__.py` file should contain a snippet that looks like the following : 
```python
from .your_card import CustomCard
CARDS = [
    CustomCard
]
```
If the `CARDS` property is not exposed then metaflow will fail to capture the custom cards exposed by the installed card module. 
## Installing Custom Metaflow Cards 

```sh
pip install git+https://github.com/valayDave/custom-metaflow-cards.git
```

OR 

```sh
pip install . 
```