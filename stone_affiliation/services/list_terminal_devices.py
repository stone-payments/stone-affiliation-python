"""
Módulo para listar os terminais de um cliente pelo stonecode
"""
import logging
from stone_affiliation.services.service import Service, CONTEXTS

LOGGER = logging.getLogger(__name__)

BASE_PATH = "{}/merchant".format(CONTEXTS["merchant"])

ENDPOINTS = {
    "terminal_devices": "ListTerminalDevices"
}

URLS = {
    "terminal_devices": "{}/{}/".format(BASE_PATH, ENDPOINTS["terminal_devices"])
}

class ListTerminalDevices(Service):
	"""docstring for ListTerminalDevices"""
	def __init__(self, arg):
		super(ListTerminalDevices, self).__init__()
		self.arg = arg
		

