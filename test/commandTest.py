import unittest
import sys
import os
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.Receiver import *


class ReceiverTest(unittest.TestCase):
    def test_lista(self):
        command1 = Invoker()
        self.assertEqual(0, len(command1._commands))

    def test_2(self):
        command1 = Receiver()
        command1.run_command_1()
        self.assertEqual(command1,command1)








    
if __name__ == '__main__': unittest.main()
