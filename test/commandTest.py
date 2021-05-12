import unittest
import sys
import os
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.Receiver import *


class ReceiverTest(unittest.TestCase):
    def test_1_lista(self):
        command1 = Invoker()
        self.assertEqual(0, len(command1._commands))

    def test_2_comparar_comandos_iguales(self):
        command1 = Receiver()
        command2 = Receiver()
        command1.run_command_1()
        command2.run_command_1()
        self.assertNotEqual(command1,command2)
    
    def test_3_comparar_comandos_distintos(self):
        command1 = Receiver()
        command2 = Receiver()
        self.assertNotEqual(command1,command2)

    
        






    
    if __name__ == '__main__': unittest.main()
