import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.leipä = Tuote("Leipä", 5)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)

    def test_ostosten_määrä_oikein(self):
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yksi_tuote_kasvattaa_korin_hintaa_oman_hinnan_verran(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipä)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_lisätyn_tuotteen_hinnat_ovat_korin_hinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipä)

        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_saqman_tuotteen_lisäämisen_jälkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_korin_hinta_yhteishinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)
 
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
 
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_korissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipä)

        ostos = self.kori.ostokset()
        self.assertEqual(len(ostos), 2)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        ostos = self.kori.ostokset()
        self.assertEqual(len(ostos), 1)

    def test_kahden_saman_tuotteen_lisäksen_jälkeen_korin_koko_yksi_ja_tuotteita_kaksi(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        ostos = self.kori.ostokset()
        self.assertEqual(len(ostos), 1)
        self.assertEqual(ostos[0].lukumaara(), 2)

    def test_korissa_kaksi_samaa_tuotetta_poistamisen_jälkeen_yksi_ostos_jossa_yksi_tuote(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.kori.poista_tuote(self.maito)
        ostos = self.kori.ostokset()
        self.assertEqual(len(ostos), 1)
        self.assertEqual(ostos[0].lukumaara(), 1)

    def test_tuotteen_poiston_jälkeen_kori_on_tyhjä_jos_tuotetta_on_yksi(self):
        self.kori.lisaa_tuote(self.maito)

        self.kori.poista_tuote(self.maito)
        ostos = self.kori.ostokset()
        self.assertEqual(len(ostos), 0)

    def test_tyhjennä_tyhjentää_korin(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipä)

        self.kori.tyhjenna()
        ostos = self.kori.ostokset()
        self.assertEqual(len(ostos), 0)