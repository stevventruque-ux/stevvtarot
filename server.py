import http.server, os
os.chdir("/Users/stevv/Desktop/stevv tarot web")
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8080, bind="")
