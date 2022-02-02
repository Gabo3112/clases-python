import unittest
import validaciones

class validacionesTest(unittest.TestCase):
    def ruc(self):
        self.assertTrue(validaciones.validarRUC())
