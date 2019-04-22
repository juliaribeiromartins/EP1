# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:36:40 2019

@author: Vitor Bandeira
"""
import json

with open('cenarios.json','r')as arquivo:
    texto=arquivo.read()
cenarios=json.loads(texto)
