#  Copyright Minaoar Hossain Tanzil, 2022 Licensed under MIT License.
#  See the LICENSE.txt for more information.


import sys

import os
import logging

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from process_post_text import *

# keywords =  ["slf4j", "log4j"]
# keywords =  ["memcpy", "memmove"]
# keywords = ['pandas', 'numpy']
#keywords = ['lxml', 'beautifulsoup']
keywords = ['gson', 'jackson']

# query = ("SELECT id, body FROM Posts where body like '%mysql%connector%' LIMIT 2")
# query = "SELECT id, body FROM stackoverflow.Posts where (Tags like '%<slf4j>%' and Tags like '%<log4j2>%') order by ViewCount Desc LIMIT 0, 5;"
# query = "SELECT id, body FROM stackoverflow.Posts where (Tags like '%<slf4j>%' and Tags like '%<log4j2>%')  LIMIT 0, 50;"
# query = "SELECT id, body FROM stackoverflow.Posts where (body like '%memcpy%' and body like '%memmove%')  LIMIT 0, 50;"
# query = "SELECT id, text as body FROM stackoverflow.Comments where (text like '%memcpy%' OR text like '%memmove%')  LIMIT 0, 50;"
# query = "SELECT id, text as body FROM stackoverflow.Comments where (text like '%pandas%' and text like '%numpy%')  LIMIT 0, 50;"
#query = "SELECT id, body, creationdate FROM stackoverflow.Posts where (body like '%lxml%' and body like '%beautifulsoup%')  LIMIT 0, 50;"

query = "SELECT id, body, creationdate FROM stackoverflow.Posts where (body like '%jackson%' and body like '%gson%')  LIMIT 0, 50;"
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logging.info('Started program: '+os.path.basename(__file__))

CACHED_DATA = True

if CACHED_DATA == False:
    # Connect to mysql database and select all rows from table
    import pwd
    import mysql.connector
    from mysql.connector import errorcode
    DB_NAME = 'stackoverflow'

    userid = 'root'
    pwd = '11111111'

    print("Connecting to database...")
    cnx = mysql.connector.connect(user=userid, password=pwd, database=DB_NAME)
    print("Connected to database")


    cursor = cnx.cursor()

    cursor.execute(query)

    # print the result
    myresult = cursor.fetchall()

    #print column names
    print(cursor.column_names)
else:
    myresult = [{'3261073', """'<p>I''ve seen questions like this come up before, and the general consensus is that <a href="http://jackson.codehaus.org/" rel="nofollow noreferrer">Jackson</a> is much faster than Gson.  See the following links for more information:</p>&#xA;&#xA;<ul>&#xA;<li><a href="https://stackoverflow.com/questions/2378402/jackson-vs-gson">Jackson Vs. Gson</a></li>&#xA;<li><a href="https://stackoverflow.com/questions/2502807/replace-standard-android-json-parser-for-better-performance">Replace standard Android JSON parser for better performance?</a></li>&#xA;<li><a href="http://www.cowtowncoder.com/blog/archives/2009/12/entry_345.html" rel="nofollow noreferrer">http://www.cowtowncoder.com/blog/archives/2009/12/entry_345.html</a></li>&#xA;<li><a href="https://stackoverflow.com/questions/338586/a-better-java-json-library">https://stackoverflow.com/questions/338586/a-better-java-json-library</a></li>&#xA;</ul>&#xA;&#xA;<p>Here is one which specifically discusses Android: <a href="http://ubikapps.net/?p=525" rel="nofollow noreferrer">http://ubikapps.net/?p=525</a></p>&#xA;'""", '2020-02-02'},
    {'3794212', '<p>On the client-side, if you support only modern browsers, you can use the native JSON.stringify() API. Otherwise, the json2.js library is fine.</p>&#xA;&#xA;<p>On the server-side, there are a herd of libraries to have a look at:</p>&#xA;&#xA;<ul>&#xA;<li><a href=\"http://jackson.codehaus.org/\" rel=\"nofollow\">Jackson</a></li>&#xA;<li><a href=\"http://json-lib.sourceforge.net/\" rel=\"nofollow\">json-lib</a></li>&#xA;<li><a href=\"http://code.google.com/p/google-gson/\" rel=\"nofollow\">gson</a></li>&#xA;<li>and <a href=\"http://www.google.com/search?q=google+java+json+libraries\" rel=\"nofollow\">many more Java JSON libraries</a>...</li>&#xA;</ul>&#xA;&#xA;<p>I\'m pointing you to Jackson first at it seems to be the fastest in many cases. However, I find its documentation harder to get my mind around every time I need to get back to it. Json-lib is sometimes easier to get to grasp with for smaller tasks that do not require top-speed, but with still completely acceptable results.&#xA;Gson as also a good reputation and is very flexible, however the previous benchmarks I came across seemed to indicate that it did not perform as well as Jackson. The newly released 1.5 version might have improved that, but I don\'t know.</p>&#xA;&#xA;<p>It comes down to the degree of flexibility you want, the performance you need, and whether you want a simple API or if you don\'t mind a more complex one.</p>&#xA;&#xA;<p>Regarding security, I think your best option here would be to support SSL for the connections. Otherwise you could just make things harder for eavesdroppers by simply using JS-based encryption, but that won\'t protect you too much. Look for SJCL (Stanford Javascript Crypto Library) for this.</p>&#xA;', '2010-09-25 14:34:17'},
    {'2623091', '<p>I want to navigate to the N-th level of an object, and serialize it\'s properties in String format.&#xA;For Example:</p>&#xA;&#xA;<pre><code>class Animal {&#xA;   public String name;&#xA;   public int weight;&#xA;   public Animal friend;&#xA;   public Set&lt;Animal&gt; children = new HashSet&lt;Animal&gt;() ;&#xA;}&#xA;</code></pre>&#xA;&#xA;<p>should be serialized like this:</p>&#xA;&#xA;<pre><code>{name:\"Monkey\",&#xA; weight:200,&#xA; friend:{name:\"Monkey Friend\",weight:300 ,children:{...if has children}},&#xA; children:{name:\"MonkeyChild1\",weight:100,children:{... recursively nested}}&#xA;}&#xA;</code></pre>&#xA;&#xA;<p>And you may probably notice that it is similar to serializing an object to json. I know there\'re many libs(Gson,Jackson...) can do this, can you give me some instructive ideas on how to write this by myself?</p>&#xA;', '2010-04-12 15:12:58'}]

s = 1
for (id, body, creationdate) in myresult:
    #print(id, creationdate)
    #print(body)
    #print('---------------------')
    # parse stackoverflow post body by removing xml tags
    
    sentences = process_raw_text(body)
    sentences_with_keywords = extract_sentence_with_keywords(sentences, keywords)
    sentences_with_adjectives = extract_sentence_with_adjectives(sentences_with_keywords)

    # print each sentence in one line with sentence counter
    for i, sentence in enumerate(sentences_with_adjectives):
        print(i+s, sentence)

    s = s + len(sentences_with_adjectives)
    #print('#####################')

    
if CACHED_DATA == False:
    cursor.close()
    cnx.close()

logging.info('Finished program: '+os.path.basename(__file__))
