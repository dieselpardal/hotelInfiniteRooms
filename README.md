The Hotel with In nite Rooms
===============================

The city of HaluaRuti has a strange hotel with in nite rooms. The groups that come to this hotel follow the following rules:

a) At the same time only members of one group can rent the hotel.

b) Each group comes in the morning of the check-in day and leaves the hotel in the evening of the check-out day.

c) Another group comes in the very next morning after the previous group has left the hotel.

d) A very important property of the incoming group is that it has one more member than its previous group unless it is the starting group. You will be given the no of members of the starting group.

e) A group with n members stays for n days in the hotel. For example, if a group of four members comes on 1st August in the morning, it will leave the hotel on 4th August in the evening and the next group of  ve members will come on 5th August in the morning and stay for  ve days and so on.

Given the initial group size you will have to  nd the group size staying in the hotel on a speci ed day.

###Input

The input contains round numbers S (1 ≤ S ≤ 10000) and D (1 ≤ D < 1015) in every line. S denotes the initial size of the group and D denotes that you will have to  nd the group size staying in the hotel on D-th day (starting from 1). All the input and output integers will be less than 1015. A group size S means that on the  rst day a group of S members come to the hotel and stays for S days then comes a group of S + 1 members according to the previously described rules and so on.

###Output

For each line of input, print on a single line the size of the group staying in the hotel on the D-th day. 

###Sample Input

1 6 

3 10 

3 14

###Sample Output

3

5

6


================================================================

###Run

`
python hotel_infinite_rooms.py 1 6
`

###Test

`
pytest test/test_controller.py
`