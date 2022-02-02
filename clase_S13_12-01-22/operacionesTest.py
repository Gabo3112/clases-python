# import unittest
# import operaciones

# class operacionesTest(unittest.TestCase):

#     def test_suma(self):
#         self.assertEqual(operaciones.sumar(4,6),10)

#     def test_suma_no_valida(self):
#         self.assertEqual(operaciones.sumar(4,7),11)

#     def test_suma_exepcion(self):
#         self.assertRaises(TypeError,operaciones.sumar, "4",5)

#     def test_division_cero(self):
#         self.assertRaises(ZeroDivisionError, operaciones.dividir,10,2)



#     def test_operar_sumar(self):
#         operacion="+"
#         a=10
#         b=5
#         self.assertEqual(operaciones.operar(operacion,a,b),15)

#     def test_operar_division(self):
#         operacion="/"
#         a=10
#         b=5
#         self.assertEqual(operaciones.operar(operacion,a,b), 2)

#     def test_operar_restar(self):
#         operacion="-"
#         a=10
#         b=5
#         self.assertEqual(operaciones.operar(operacion,a,b), 5)
    
#     def test_operaracion_deconocida(self):
#         operacion="*"
#         a=10
#         b=5
#         self.assertEqual(operaciones.operar(operacion,a,b), -1)


# if __name__=="__main__":
#     unittest.main()
    
import unittest
import operaciones

class operacionesTest(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(operaciones.sumar(4,6), 10)

    def test_suma_no_valida(self):
        self.assertNotEqual(operaciones.sumar(4,7), 10)

    def test_suma_excepcion(self):
        self.assertRaises(TypeError, operaciones.sumar, "4", 5)

    def test_division_cero(self):
        self.assertRaises(ZeroDivisionError, operaciones.dividir, 10, 0)

    def test_operar_suma(self):
        operacion = "+"
        a = 10
        b = 4
        self.assertEqual(operaciones.operar(operacion, a, b), 14)

    def test_operar_resta(self):
        operacion = "-"
        a = 10
        b = 5
        self.assertEqual(operaciones.operar(operacion, a, b), 5)

    def test_operacion_division(self):
        operacion = "/"
        a = 10
        b = 5
        self.assertEqual(operaciones.operar(operacion, a, b), 2)

    def test_operacion_desconocida(self):
        operacion = "*"
        a = 10
        b = 5
        self.assertEqual(operaciones.operar(operacion, a, b), -1)



if __name__ == "__main__":
    unittest.main()