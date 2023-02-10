"""Creating the major class of the project. This class will be used by subclasses. """


class SocialNetwork:
    def __init__(self, file_name):
        """After getting file name from user input initializing it in the class"""
        self._file_name = file_name

        """Creating social network dictionary to access it in subclasses too."""
        self._social_network = {
            "People": {},
            "Total Person": 0
        }

        """Calling this initial method to save datas into created social network dictionary."""
        self.create_social_network()

    """Created to parse txt file and save social network data into dict"""
    def create_social_network(self):
        """Opening the txt file."""
        with open("./social networks data/" + self._file_name + ".txt", "r",
                  encoding='UTF-8') as social_network:
            """For looping through each line to get index number and data """

            for index, people in enumerate(social_network.readlines()):
                """Checking if index 0, if yes, saving this data into social_network['Total Person']"""
                if index == 0:
                    self._social_network["Total Person"] = int(people)
                else:
                    """Formatting the read line data"""
                    unique_person_data = people.strip().split(" ")
                    """Looping through read line"""
                    for person in unique_person_data:
                        """If person is found by the first time creating special array for the person. 
                        This array will contain friends name inside."""
                        if person not in self._social_network["People"]:
                            self._social_network["People"][person] = list(
                                set(unique_person_data) - {person})
                        else:
                            """If person is already found in the network, appending into their friend list array."""
                            self._social_network["People"][person].extend(
                                list(set(unique_person_data) - {person}))

        """Doing sorting before all process ends."""
        self._social_network["People"] = dict(sorted(self._social_network["People"].items()))
        return self._social_network

    """This method is created to display social network in prettier way. """
    def get_social_network(self):
        sorted_dict = dict(sorted(self._social_network["People"].items()))
        if len(sorted_dict) != 0:
            for key, value in sorted_dict.items():
                print(str(key) + " --> ", sorted(value))

    """Setter method for social network dictionary"""
    def set_social_network(self, new_social_network: dict):
        self._social_network = new_social_network
        return self._social_network
