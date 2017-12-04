# -*- coding: utf-8 -*-

"""
Init da sdk da API de Credenciamento expõe a classe principal
que representa o client, o modulo de erros e adiciona um logger
handler fake.
"""
import logging
from .client import StoneAffiliation
from . import errors

logging.getLogger(__name__).addHandler(logging.NullHandler())
