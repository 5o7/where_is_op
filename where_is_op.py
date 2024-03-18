#Tools

import praw
import time

# Credentials

reddit = praw.Reddit(client_id="X",
                     client_secret="X",
                     password="X!",
                     user_agent="Check on op",
                     username="X")

# Message sent when a post is removed

s1 = "Rule 2: This subreddit is about discussing older movies that we enjoy. "
s2 = "If you are not able to contribute to that dialog please refrain from posting."

# A loop will run about every 12 hours

while True:

    # Inspect the newest 30 submissions from a subreddit

    for submission in reddit.subreddit("X").__getattribute__("new")(limit=30):

        # If there is no text in the submission (If there is text in the submission, skip it):

        if not submission.selftext:

            # If the post was made more than 24 hours from the time this line of code runs:

            if int(time.time()) > submission.created_utc + 86400:

                # Put all the submission's comment's authors into a list

                authors = []
                for comment in submission.comments.list():
                    authors.append(str(comment.author))

                # If the authors list is empty because of no comments

                if len(authors) == 0:

                    # Make a comment in the submission regarding the reason for removal and remove submission

                    submission.reply(s1 + s2)
                    submission.mod.remove()

                # If comments exist in the submission, inspect every comment's author

                else:
                    for author in authors:


                        if not str(submission.author) in authors:

                            # Make a comment in the submission regarding the reason for removal and remove submission

                            submission.reply(s1 + s2)
                            submission.mod.remove()

    # Rest for 12 hours

    time.sleep(21600)
