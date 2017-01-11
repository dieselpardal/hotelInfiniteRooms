import unittest
import hotel_infinite_rooms

class AddTest(unittest.TestCase):


    def setUp(self):
        '''Verify environment is setup properly'''
        pass

    def test_loop_1_6(self):
        '''Verify that size e day with 1 and 6 is 3'''
        hir = hotel_infinite_rooms.HotelInfiniteRooms()
        self.assertEqual(hir.membres_day(1, 6), 3)

    def test_loop_3_10(self):
        '''Verify that size e day with 3 and 10 is 5'''
        hir = hotel_infinite_rooms.HotelInfiniteRooms()
        self.assertEqual(hir.membres_day(3, 10), 5)

    def test_loop_3_14(self):
        '''Verify that size e day with 3 and 14 is 6'''
        hir = hotel_infinite_rooms.HotelInfiniteRooms()
        self.assertEqual(hir.membres_day(3, 14), 6)

    def test_recrusive_1_6(self):
        '''Verify that size e day with 1 and 6 is 3 with recrusive'''
        hir = hotel_infinite_rooms.HotelInfiniteRooms()
        self.assertEqual(hir.membres_day_res(1, 6, 1), 3)


if __name__ == '__main__':
    unittest.main()