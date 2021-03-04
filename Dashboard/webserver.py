from http.server import HTTPServer, BaseHTTPRequestHandler

root = "./web/"

# this splits everything don't delete or move itay thx


def split(word):
    return [char for char in word]

# this gets the web vars dont delete or move itay thx


def getVar(var, path):
    path = split(path)
    returnStr = ""
    addFromHere = False
    varText = ""
    for i in range(len(path)):
        if(path[i] == "="):
            for j in range(len(split(var))):
                varText += path[i-j+1]
            if(varText == var):
                addFromHere = True
        elif(path[i] == "&"):
            addFromHere = False

        if(addFromHere == True):
            returnStr += path[i]
    return returnStr

# this removes the vars from the path dont delete or remove thx


def RemoveVars(string):
    string = split(string)
    stop = False
    finalStr = ""
    for i in range(len(string)):
        if(string[i] == "?"):
            stop = True
        if(stop == False):
            finalStr += string[i]
    return finalStr


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if(self.path == "/"):
            self.path = "/index.html"
        try:
            try:
                code = open(root + self.path[1:]).read()
            except:
                code = open(root + self.path[1:] + ".html").read()
            self.send_response(200)
        except:
            if("?" in self.path):
                try:
                    code = open(root + RemoveVars(self.path)[1:]).read()
                except:
                    code = open(root + RemoveVars(self.path)[1:] + ".html").read()
                self.send_response(200)

                print(getVar("vodka", self.path))

            else:
                code = open(root + "404.html").read()
                self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(code, 'utf-8'))


httpd = HTTPServer(('localhost', 9028), Serv)
httpd.serve_forever()
