#!/usr/bin/python

class HotelInfiniteRooms:

    def membres_day(self,S,D):
        sum = S
        while sum < D:
            S += 1
            sum +=S
        return S

    def membres_day_res(self, S, D, sum):
        if sum < D :
            return self.membres_day_res(S + 1, D, sum + S + 1)
        return S