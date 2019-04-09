import unittest
import treasure_tables

class TestTreasureTables(unittest.TestCase):

    def test_individual(self):
        self.assertEqual(len(treasure_tables.individual),25)

    def test_hoard(self):
        self.assertEqual(len(treasure_tables.hoard),25)
    
    def test_individual_subtables(self):
        self.assertEqual(len(treasure_tables.i0to4),100)
        self.assertEqual(len(treasure_tables.i5to10),100)
        self.assertEqual(len(treasure_tables.i11to16),100)
        self.assertEqual(len(treasure_tables.i17plus),100)
    
    def test_magic_tables(self):
        self.assertEqual(len(treasure_tables.tableA),100)
        self.assertEqual(len(treasure_tables.tableB),100)
        self.assertEqual(len(treasure_tables.tableC),100)
        self.assertEqual(len(treasure_tables.tableD),100)
        self.assertEqual(len(treasure_tables.tableE),100)
        self.assertEqual(len(treasure_tables.tableF),100)
        self.assertEqual(len(treasure_tables.tableG),100)
        self.assertEqual(len(treasure_tables.tableH),100)
        self.assertEqual(len(treasure_tables.tableI),100)
    
    def test_valuables_tables(self):
        self.assertEqual(len(treasure_tables.v0to4),100)
        self.assertEqual(len(treasure_tables.v5to10),100)
        self.assertEqual(len(treasure_tables.v11to16),100)
        self.assertEqual(len(treasure_tables.v17plus),100)

    
if __name__ == '__main__':
    unittest.main()