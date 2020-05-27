# iDoctor

Docs:
1. Run flask
    - go to ./run.sh
    
2. Run sass (css generator)
    - go to ./sass.sh
    
3. Handle db using flask_migrate
    - flask db init (for initialize db migration)
    - flask db migration -m (for create migration)
    - flask db upgrade "name upgrading db using migration"
    
4. Generate secret_key:

```python

import random
random._urandom(16)

```