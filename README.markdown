# Human Webserver
... is a Web Server written for presentation purposes that allows handwritten responses.

# Usage
Start the Server (at default it will listen to port 8008)
    $ python Listen.py 
    World's Slowest Web Server HumanWebserver started

If a request comes in, you will see something like
    GET / HTTP/1.1
    Host: local:8008
    Connection: keep-alive
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.102 Safari/535.2
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Encoding: gzip,deflate,sdch
    Accept-Language: en-US,en;q=0.8
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3
    Cookie: asdf=1; StatusNetInstance=%7B%22Nickname%22%3A%22alpha%22%7D; _pk_id.1.6fe1=8ab14a961354ea78.1314833645.57.1319207239.1319112665.; splashShown=1; splashShown1.5=1
    
    
    Respond with? 

Now you can type the status code you want to respond with (try tab for completition). Default is 200.

This will open vim prefilled with e.g.
    HTTP/1.1 200 OK
    Content-Type: text/html

After editing your response just save and quit vim to send it out.

# Templates
If you want some custom predefined responses pu them into the responses directory. If then a request comes in you can provide the file name instead of a status code (try tab completition again).