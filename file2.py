#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           �A�fuCہ�vp*2ak�2�Y�j5<�wִ�.-!����D�e�ř��H�)��TE����ͱ�Z�~\���U<���,��]���S\~���[��5�*����똋��J�8��Bף�@��P�i"""
from hashlib import sha256
print sha256(blob).hexdigest()
