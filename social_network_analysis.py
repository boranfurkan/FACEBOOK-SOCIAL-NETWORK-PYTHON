from social_network import SocialNetwork
"""Created as subclass to SocialNetwork class."""


class NetworkAnalysis(SocialNetwork):
    def __init__(self, file_name):
        """Initializing the super class."""
        super().__init__(file_name=file_name)

    """This method is created to display the friend list length for chosen person."""

    def display_friends(self):
        while True:
            """Asking user to input valid ID or username."""
            user_input = input("Enter a member name or ID as an integer from 0 to 6:\n")

            """Checking if user wants to stop process."""
            if user_input != "n":
                """Trying to catch invalid usernames."""
                try:
                    """If person is in the network, it shows friend list array for the person."""
                    selected_person = self._social_network["People"][user_input]
                    print(f"{user_input} has {len(selected_person)} friends! ")
                    break
                except KeyError:
                    print("Please enter valid name or ID or press n to exit")
            else:
                print("Successfully exited")
                break

    """This method is created to display least friendships in the network."""

    def display_least_friends(self):
        """Sorting the social network dictionary according to their friend list array length. Then choosing least 2
        people from the list to display."""
        sorted_network_by_friends = sorted(self._social_network["People"],
                                           key=lambda key: len(self._social_network["People"][key]))

        """After sorting operation, creating the arrays to save people's name. """
        zero_friends = []
        least_friends = []

        """For looping through sorted array."""
        for index, person in enumerate(sorted_network_by_friends):
            """If friends list length equals 0, appending the person into zero friends and removing it from sorted 
            array. Because I removed the 0 friends people from sorted array, I will be able to assume the first 
            person of array as the least person in the array. """
            if len(self._social_network["People"][person]) == 0:
                zero_friends.append(person)
                sorted_network_by_friends.remove(person)
            else:
                """Accessing the first element of sorted array."""
                least_person = sorted_network_by_friends[0]
                """"Checking if the person has same friend list size with it. If yes, appending person name into 
                least friends array. """
                if len(self._social_network["People"][person]) == len(self._social_network["People"][least_person]):
                    least_friends.append(person)
                else:
                    """As soon as length does not match, breaking the for loop."""
                    break
        """And finally appending the first person also into, least friends array."""
        least_friends.append(sorted_network_by_friends[0])

        print("The member ID for the member with least friends is:", ' , '.join(str(e) for e in least_friends))
        print("The member ID for the member with 0 friends is:", ' , '.join(str(e) for e in zero_friends))
        return zero_friends, least_friends

    """This method is created to display direct connections between person and it's friends."""

    def display_direct_connections(self):
        while True:
            """Asking user to input valid ID or username."""
            user_input = input("Enter a member name or ID as an integer from 0 to 6:\n")

            """Checking if user wants to stop process."""
            if user_input != "n":
                """Trying to catch invalid usernames."""
                try:
                    """Showing direct connections for the chosen person."""
                    selected_person = self._social_network["People"][user_input]
                    print(f"Friend list for {user_input} is {selected_person}")
                    break
                except KeyError:
                    print("Please enter valid name or ID or press n to exit")
            else:
                print("Successfully exited")
                break

    """This method is created to display direct connections between person and it's friends."""

    def display_indirect_connections(self):
        while True:
            """Asking user to input valid ID or username."""
            user_input = input("Enter a member name or ID as an integer from 0 to 6:\n")

            """Checking if user wants to stop process."""
            if user_input != "n":
                """Trying to catch invalid usernames."""
                try:
                    """Creating indirect connections array to save data inside for each person."""
                    indirect_connections = []
                    """Finding the indirect connections between person and it's friends."""
                    for friends in self._social_network["People"][user_input]:
                        for friends_friend in self._social_network["People"][friends]:
                            if friends_friend not in self._social_network["People"][user_input]:
                                if friends_friend != user_input:
                                    indirect_connections.append(friends_friend)

                    print(f"Indirect connections for {user_input} is {', '.join(str(e) for e in indirect_connections)}")
                    break
                except KeyError:
                    print("Please enter valid name or ID or press n to exit")
            else:
                print("Successfully exited")
                break

    """This method is created to check validation of the network."""

    def validate_network(self):
        """looping through social network class from super class."""
        for person, friends in self._social_network["People"].items():
            """Checking if the person is also in their friend's list."""
            for friend in friends:
                if person not in self._social_network["People"][friend]:
                    """İf not, showing an error to the user."""
                    print("The network is inconsistent, try another file.")
                    break
        print("The network is consistent!")