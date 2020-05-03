"""id_dictionary.py: A UID keyed dictionary that emits pyQT signals."""

__author__ = "Team Keikaku"

__version__ = "1.0"

import uuid
from typing import Any

from PyQt5.QtCore import QObject, pyqtSignal


class IDDict(QObject):
	"""A dictionary of objects and associated UIDs.

	Attributes
	----------
	added: pyqtSignal
		A pyQT signal emitted when an object is added.
	removed: pyqtSignal
		A pyQT signal emitted when an object is removed.
	edited: pyqtSignal
		A pyQT signal emitted when an object is edited.
	"""

	added: pyqtSignal = pyqtSignal()
	removed: pyqtSignal = pyqtSignal()
	edited: pyqtSignal = pyqtSignal()

	def __init__(self, dictionary: Any = None):
		"""
		:param dictionary: dict, optional (default is {})
			A dictionary of objects.
		"""

		QObject.__init__(self)
		if dictionary:
			self.dictionary = dictionary
		else:
			self.dictionary = {}

	def items(self):
		"""Retrieves all items in the dictionary.

		:return dict_items
			A list of key, value tuples.
		"""

		return self.dictionary.items()

	def values(self):
		"""Retrieves all values in the dictionary.

		:return list
			A list of values.
		"""

		return self.dictionary.values()

	def get(self, uid: str) -> Any:
		"""Retrieves an object given it's UID.

		:param uid: str
			UID of the object.
		:return Any
			Object associated with the given UID.
		"""

		return self.dictionary.get(uid)

	def empty(self) -> bool:
		"""Determines of the dictionary is empty.

		:return bool
			True if dictionary is empty; false otherwise.
		"""

		return not bool(self.dictionary)

	def add(self, thing: Any) -> str:
		"""Adds a new object to the dictionary. Emits added.

		:param thing: Any
			Object to insert.
		:return str
			A UID associated with the object added.
		"""

		uid = uuid.uuid4().__str__()
		self.dictionary[uid] = thing
		self.added.emit()
		return uid

	def delete(self, uid: str):
		"""Removes an object from the dictionary. Emits removed.

		:param uid: str
			UID of the object.
		"""

		self.dictionary.pop(uid)
		self.removed.emit()

	def edit(self):
		"""Emits edited that an object in the dictionary was edited."""

		self.edited.emit()

	def set(self, uid: str, thing: Any):
		"""Adds a specified thing with specified uid.

		:param uid: str
			UID of the object.
		:param thing: Any
			Object to insert.
		"""

		self.dictionary[uid] = thing
