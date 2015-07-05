-*- encoding: utf-8 -*-
## Punct

Punct is a library to convert fancy unicode puntuation into boring, but much easier to work with, ascii punctuation.

Example:
```python
from __future__ import unicode_literals
import punct

fancy_punctuation = "This is the phase in which we put a giant “laser” on the moon."
standard_punctuation = punct.normalize(fancy_punctuation)
```
