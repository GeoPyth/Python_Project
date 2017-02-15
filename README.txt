FILES ATTACHED:
------------------
2 source codes : twitter_script (first) and projectscript(second).
1 Map : twit.mxd (with a US shapefile)
 Addin zip and project addin file : For the toolbar, with the toolbar script in the install file.
US Shapefile.

RUN:
------
After running the first script with unique key, the csv files will be generated.
After running the second script, the twit.mxd will be updated to show the layer files and combo box.

PUPROSE AND POTENTIAL USER:
--------------------------------
The purpose of the program is to get geolocated tweets from twitter and display on a map.
Potential users of this program may be for those in election campaigns (shown example), marketing divisions of
product based companies, emergency relief workers.
ALTHOUGH THE PROJECT SUCCESSFULLY PLOTS THE POINTS BY USING THE SEARCH PARAMETER, IT WOULD BE UNWISE TO USE THIS
PROGRAM FOR SAID PURPOSES. ARCGIS ONLINE HAS A JSON PLUGIN WHICH CAN SHOW REAL TIME UPDATES ON A MAP AND THE 
STREAM API FROM TWITTER CAN BE USED WHICH WOULD BE MORE EFFECTIVE TO SHOW AREAS OF INTERESTS AND PROGRESSIONS.

PROGRAMMING AND EXECUTING ENVIRONMENT:
------------------------------------------
The programming most of the program was done in PyScripter. The tweepy module script to get data from twitter
was executed from ipython notebook. (The installation of tweepy in PyScripter was giving multiple errors, so 
used anaconda to install ipython notebook). ESRI ArcMap is the platform used to show the map and results.
Python addin was downloaded and a button and combo box were implemented to show results and give the map an 
interactive feel.

OTHER INFORMATION:
----------------------
iPython Notebook was used for the twitter script because I had difficulty in installing tweepy. iPython or tweepy
or both, were throwing random errors for small things. At one point, I couldn't change my script because it 
would throw an error. Hence, this script wasn't pep8 checked. The workspace folder on ipython couldn't be changed
so manually copied the csv files to my workspace. 
After May of 2015, the default setting for geolocations has been turned off by twitter. This in turn gave me
disappointing results. The bounding box and count  parameters, even after multiple searches and different entries, did
not perform uniformly each time. Hence, the general geographic location of the tweets (Mostly midwest) and the count
(from 17 to 60) kept fluctuating in the same range. 

SOURCES OF REFERENCE CODE:
------------------------------
For most of the sources and reference codes, I have taken the help of questions and comments on STACK OVERFLOW
& GIS STACK EXCHANGE.
For the twitter code, pieced together materials and query parameters from dev.twitter.com
For the remaining part, I referred the labs and homeworks for the semester.
References:
https://www.freemaptools.com/radius-around-point.htm
http://docs.tweepy.org/en/latest/api.html
https://dev.twitter.com/rest/public/timelines
https://dev.twitter.com/rest/reference/get/search/tweets
https://dev.twitter.com/rest/reference/get/users/search
https://dev.twitter.com/overview/documentation
https://dev.twitter.com/rest/public/search
http://resources.arcgis.com/EN/HELP/MAIN/10.1/index.html#//00170000006z000000
http://gis.stackexchange.com/questions/43160/search-in-bounding-boxes-and-locations
http://gis.stackexchange.com/questions/35693/use-python-to-add-layers-to-toc
http://gis.stackexchange.com/questions/138935/looping-through-layers-add-layer-to-mxd-export-image-repeat-using-arcpy
http://docs.tweepy.org/en/latest/api.html#tweepy-api-twitter-api-wrapper
http://gis.stackexchange.com/questions/119923/how-do-i-convert-a-tweet-into-a-point-in-qgis
http://support.esri.com/en/knowledgebase/techarticles/detail/27589
https://www.arcgis.com/home/item.html?id=5f3aefe77f6b4f61ad3e4c62f30bff3b

