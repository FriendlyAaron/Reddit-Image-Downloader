import praw
import os
import urllib.request


#Login 
reddit = praw.Reddit(
 client_id = os.environ ['client_id'],
  client_secret = os.environ ['client_secret'],
  username = os.environ ['username'],
  password = os.environ ['password'],
  user_agent = "<Findey1.0>"
)  


#Check hot for image posts and pastes title and iamge url 
def fetch_post():
  i=0
  print ('Checking posts for images...')
  for submission in subreddit.hot(limit=num): # Check top posts in hot
   slink = submission.url 
   if not submission.stickied and not submission.is_self and slink.endswith (('png','.jpg')):#Checks if submission is not stickied and is a image file
      stitle = submission.title # Gets title of post
      type_file = submission.url[-4:] #Gets the type of image of the post
      urllib.request.urlretrieve(slink,stitle+type_file) # Uses the title of the post as the name of the image 
      i=i+1 #Keeps track of how many images collected
  print ('Complete!')
  if i == 0:
    print ('Sorry but no posts had any images.')
  else:
    print (str(i)+ ' images saved.')


#Check if subreddit is valid
def checksub():
  global sub
  global subreddit 
  sub = input("What subreddit would you like to use? ")
  subreddit = reddit.subreddit(sub)
  for submission in subreddit.hot(limit=20):
    break

#Check if number is valid
def checknum():
    global num
    num = input('How many posts do you want me to check? ')
    if num.isdigit():
      num = int(num)
    else:
      raise ValueError
      
     

#Process
def process():
  print ('Hello! I\'ll search hot posts on any subreddit and save thoses images on your computer!')
  j = 'y'
  while j =='y' and j != 'n':    
    j = 'y'
    k ='y'
    try:
      checksub()
      checknum()
      fetch_post()
    except ValueError:
      print("Invalid number")
      process()
    except Exception as e:
      print('That subreddit does not exist.')
      process()
    while k =='y':  
      j = input ('Would you like to search for a new subreddit? ')
      if j.lower() == 'y' or j.lower() == 'yes':
        j = 'y'
        k ='n'
      elif j.lower() =='n' or j.lower() == 'no':
        j = 'n'
        k = 'n'
  print ('Have a nice day!')
  
process()
