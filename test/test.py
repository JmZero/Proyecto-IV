#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('./src/')
import infojugador

class InfoJugadorTest(unittest.TestCase):

    test = infojugador.InfoJugador()

    def testStatus(self):
        self.assertEqual(self.test.status(),str('OK'),"El status no es correcto")

    def testBattleTag(self):
        self.assertEqual(self.test.getBattleTag(1),False,"El battletag no puede ser un número")
        self.assertEqual(self.test.getBattleTag("JmZero"),str('JmZero'),"El Battletag no es correcto")

    def testPerfilPublico(self):
        self.assertEqual(self.test.isPerfilPublico("Antonio"),False,"El battletag existe")
        self.assertEqual(self.test.isPerfilPublico("JmZero"),str('Publico'),"El perfil es privado")

    def testLvl(self):
        self.assertEqual(1 <= self.test.getNivel("JmZero") <= 2500, True,"El nivel no es correcto")

    def testTop5(self):
        self.assertEqual(self.test.getTop5("Neim"),False,"El perfil es público")

if __name__ == '__main__':
    unittest.main()
