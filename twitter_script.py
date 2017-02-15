# ----------------------------------------------------------------------------
# Name: Script to get data from twitter
# Purpose: Get all geotagged tweets from twitter with given keywords
# Author: Keyur Kulkarni
# ----------------------------------------------------------------------------

import tweepy
from tweepy import OAuthHandler
consumer_key='qN6bP9B4H3ryeDJ3v93D7PTd3'
consumer_secret='UeA7nFZys1TAebBiCWPz2gjW35JSrPcak3rA2cYLJDhu9WBdLi'
access_token='2154691064-DCVzmBG8FEYaRAxDtqAzy4FLxV9rXLHK8FXB7jx'
access_token_secret='CzO4EHx5nXys0QN8ZrjHAuTxFBgR3ozKJlS5G2y7zn3Qg'
auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth,parser=tweepy.parsers.JSONParser())

list = ["Hillary", "Trump", "Sanders", "Carson"]
for x in list:
    print x
    tweets=api.search(q= x, geocode='38.75408327579141,-105.3369140625,14000.624mi',language = 'en', count= 200)


    row={}
    import csv,sys
    filename= x + '.csv'
    csvfile= open(filename,'w')
    csvfile.truncate()
    fieldnames=["Lat","Tweet","User_Name","Screen_Name","Long"]
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    for result in tweets["statuses"]:
        if result["geo"]:
            if result["entities"]["user_mentions"]:

                for r in result["entities"]["user_mentions"]:
                    row["User_Name"]=r["name"]
                    row["Screen_Name"]=r["screen_name"]
            else:
                row["Screen_Name"]=""
                row["User_Name"]=""
            row["Tweet"]=result["text"]
            row["Tweet"] = row["Tweet"].encode('ascii', 'replace')
            row["Lat"]=result["geo"]["coordinates"][0]
            row["Long"]=result["geo"]["coordinates"][1]
            writer.writerow(row)


    csvfile.close()

print "done"
