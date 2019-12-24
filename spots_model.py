import point
#given by professor

SPOT_RADIUS_FRAC = 0.05



class Spot:
    def __init__(self, center: point.Point, radius_frac: float):
        '''
        Initialize a newly-created Spot object, given its center
        point (a Point object) and the spot's radius (in
        fractional coordinates).
        '''
        self._center = center
        self._radius_frac = radius_frac


    def center(self) -> point.Point:
        '''
        Returns a Point object representing this Spot's center.
        '''
        return self._center


    def radius_frac(self) -> float:
        '''
        Returns the radius of this Spot, in terms of fractional
        coordinates.
        '''
        return self._radius_frac


    def contains(self, point: point.Point) -> bool:
        '''
        Returns True if the given Point object lies within
        this Spot, False otherwise.
        '''

        return self._center.frac_distance_from(point) <= self._radius_frac



class SpotsState:
    def __init__(self):
        '''
        Initializes the state of the Spots application.  Initially,
        there are no spots.
        '''
        self._spots = []


    def all_spots(self) -> [Spot]:
        '''Returns a list of all of the Spot objects that currently exist.'''
        return self._spots


    def handle_click(self, click_point: point.Point) -> None:
        '''
        Handle a click on the given point, by either removing the
        spot in which the point lies, or by adding a new spot centered
        at the given point.
        '''

        for i in reversed(range(len(self._spots))):
            if self._spots[i].contains(click_point):
                del self._spots[i]
                return


        self._spots.append(Spot(click_point, SPOT_RADIUS_FRAC))










