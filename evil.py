#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           �y<�M��i��ϻ_c ����
��{M1�������B�c�h�j� �6���ώ���}a�\��g���| �H;Ju�3�� ����XiY��bV��B���/�zl�b0���M�k�"""
from hashlib import sha256
if sha256(blob).hexdigest() == 'cbfe4549e609c28fda6e7032b4bad00bd03ebffc65fa2da4fdf81a1f1cb14dba'
	print "I come in peace."
else:
	print "Prepare to be destoryed!"
