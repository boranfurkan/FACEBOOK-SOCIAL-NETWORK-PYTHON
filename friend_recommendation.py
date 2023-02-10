"""Importing the main social network class"""
from social_network import SocialNetwork

"""This class uses SocialNetwork class as a super class."""


class FriendRecommendation(SocialNetwork):
    def __init__(self, file_name):
        """Initializing super class"""
        super().__init__(file_name=file_name)

        """Creating common friends and friend recommendation dicts to access them easily later."""
        self.__common_friends = {}
        self.__friend_recommendations = {}

    """This method is created to fill common friends dictionary"""
    def set_common_friends(self):
        """For looping through social network which comes from super class."""
        for person, friends in self._social_network["People"].items():
            """Creating an empty array each person."""
            self.__common_friends[person] = []
            """For looping through the same social network to match people."""
            for person2, friends2 in self._social_network["People"].items():
                """By getting intersection between first person's friend list and second person's 
                friend list finding the common friends between people."""
                intersection = len(set(friends2).intersection(set(friends)))
                self.__common_friends[person].append(intersection)
        """Returning to the created common friends list"""
        return dict(sorted(self.__common_friends.items()))

    "This method is created to recommend a friend to chosen person"
    def set_recommend_friend(self):
        """By calling set common friends method, filling the common friends dictionary"""
        self.__common_friends = self.set_common_friends()

        """For looping through social network comes from super class."""
        for person in self._social_network["People"]:
            """For each person creating not permitted suggestions array."""
            not_possible_suggestions = {person}.union(set(self._social_network["People"][person]))

            """For each person also creating permitted suggestions array."""
            possible_suggestions = []

            """For looping through created common friends dictionary for each person"""
            for index, i in enumerate(self.__common_friends[person]):
                """Checking if the common friends count 0."""
                if i != 0:
                    """Checking if the person name inside not possible suggestions array."""
                    if list(self.__common_friends.keys())[index] not in not_possible_suggestions:
                        """Checking if the person name already saved into possible suggestions array."""
                        if list(self.__common_friends.keys())[index] not in possible_suggestions:
                            """Here the person saved as recommendable friend to chosen person's array"""
                            possible_suggestions.append(list(self.__common_friends.keys())[index])
            """Saving all recommendable friends name into friends recommendation dictionary"""
            self.__friend_recommendations[person] = possible_suggestions

        """Returning to the friends recommendation dictionary"""
        return self.__friend_recommendations

    """Crated to display common friends dictionary."""
    def get_common_friends(self):
        return print(self.set_common_friends())

    """Created to display recommendable people's name to chosen person. """
    def get_recommended_friends(self, person_name):
        self.__friend_recommendations = self.set_recommend_friend()

        if len(self.__friend_recommendations[person_name]) != 0:
            return print(f"Recommended friend for {person_name} is "
                         f"{'or'.join(str(e) for e in self.__friend_recommendations[person_name])}")
        else:
            return print(f"Recommended friend for {person_name} is {None}")
