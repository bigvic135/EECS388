#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           �A�fuCہ�vp*2ak�2<Y�j5<�wִ�.-!����D�e����H�)��TE���Bͱ�Z�~\���U<���,��]��YS\~���[��5�*����똋X�J�8��Bף�@�HP�i"""
from hashlib import sha256
print sha256(blob).hexdigest()
