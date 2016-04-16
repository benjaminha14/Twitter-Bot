import tweepy
class Tweetbot:
    myFriends = []
    myFollowers = []
    friendsNotFollowing = []

    def __init__(self,consumerID, consumerSecret,tokenID,tokenSecret):
        auth = tweepy.OAuthHandler(consumerID,consumerSecret)
        auth.set_access_token(tokenID,tokenSecret)
        self.myAccount = tweepy.API(auth)
        print("Initalize twitter bot.")
    def initFriends(self):
        for friend in self.myAccount.friends():
            self.myFriends.append(friend.screen_name)
        for followers in self.myAccount.followers():
            self.myFollowers.append(followers.screen_name)
    def checkFollowers(self):
        for friend in self.myFriends:
            isFollower = False
            for follower in self.myFollowers:
                if(friend == follower):
                    isFollower = True
            if(isFollower == False):
                self.friendsNotFollowing.append(friend)
        print "Who is not following back:"
        for notFollowing in self.friendsNotFollowing:
            print notFollowing
