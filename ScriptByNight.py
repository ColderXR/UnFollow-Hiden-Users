from aminofix import *
MyClient = Client()
MyClient.login(email=input('Your Email : '),password=input('Your Password : '))
YourLink = MyClient.get_from_code(input('Your Profile Link : '))
MySClient = SubClient(YourLink.comId,profile=MyClient.profile)
UnFollowId = MySClient.get_user_following(YourLink.objectId,start=0,size=1).userId
try:
    MySClient.unfollow(UnFollowId)
except Exception as Error:
    print(Error)
else:
    print('OK ! , Done By Night')
