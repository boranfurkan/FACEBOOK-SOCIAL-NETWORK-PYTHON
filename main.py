"""Importing the created classes"""
from social_network import SocialNetwork
from friend_recommendation import FriendRecommendation
from social_network_analysis import NetworkAnalysis

"""Creating a script to run"""
if __name__ == "__main__":

    while True:
        """Asking user to enter filename to work on it"""
        file_name = input("Please enter the social network file name! (without .txt) or press 'n' to exit.\n").lower()

        """Checking if user wants to end program"""
        if file_name != "n":
            """With using try method, validating the file name"""
            try:
                """Providing the file name to my classes as input"""
                social_network = SocialNetwork(file_name=file_name)
                friend_recommendation = FriendRecommendation(file_name=file_name)
                network_analysis = NetworkAnalysis(file_name=file_name)

                """Asking user to if they want to display created social network"""
                display_network = input("Display the social network (y/n)? ").lower()
                """Validating the input"""
                if display_network == "y":
                    social_network.get_social_network()

                """Asking user to if they want to use friend recommendation method"""
                display_friend_recommendation = input("Display friend recommendation (y/n)? ").lower()
                """Validating the input"""
                if display_friend_recommendation == "y":
                    while True:
                        """Asking user to input username or ID"""
                        index_input = input(
                            "Enter a member name or ID as an integer from 0 to 6: Please press n to exit friend "
                            "recommendation!\n")

                        """Checking if the user input valid name in the network"""
                        if index_input in friend_recommendation.set_recommend_friend():
                            friend_recommendation.get_recommended_friends(index_input)
                            break
                        elif index_input == "n":
                            """Checking if the user wants to finish friend recommendation method"""
                            break
                        else:
                            """Warning user about input validation"""
                            print("You did not enter valid name or ID!")

                """Asking user if they want to display common friendship map in the network"""
                display_common_friends = input("Display common friendship map (y/n)? ").lower()
                """Validating the input"""
                if display_common_friends == "y":
                    friend_recommendation.get_common_friends()

                """Asking user if they want to display selected person's friends list length"""
                display_friends_length = input("Display friends length of selected person (y/n)? ").lower()
                """Validating the input"""
                if display_friends_length == "y":
                    network_analysis.display_friends()

                """Asking user if they want to display least friendships in the network"""
                display_least_friends = input("Display least friends in the network (y/n)? ").lower()
                """Validating the input"""
                if display_least_friends == "y":
                    network_analysis.display_least_friends()

                """Asking user if they want to display direct connection for the chosen person"""
                display_direct_connections = input("Display the direct connections in the network (y/n)? ").lower()
                """Validating the input"""
                if display_direct_connections == "y":
                    network_analysis.display_direct_connections()

                """Asking user if they want to display indirect connection for the chosen person"""
                display_indirect_connections = input("Display the indirect connections in the network (y/n)? ").lower()
                """Validating the input"""
                if display_indirect_connections == "y":
                    network_analysis.display_indirect_connections()

                """Asking user if they want to check validity of the network"""
                display_network_validity = input("Display the validity of the network (y/n)? ").lower()
                """Validating the input"""
                if display_network_validity == "y":
                    network_analysis.validate_network()

                """Breaking the while true loop after questions"""

                """Asking user if they want to work with another network."""
                continue_ = input("Would like to check for another social network (y/n)? ").lower()
                if continue_ == "y":
                    pass
                elif continue_ == "n":
                    break
                else:
                    print("You did not enter valid input! ")
                    break

            except FileNotFoundError:
                """Catching the wrong file name input"""
                print("Please provide a valid file name!")

        else:
            """Exit command"""
            print("Successfully exited! ")
            break
