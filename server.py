import json
import falcon
#import pizza

class HelloResource(object):

    #s=pizza.getpizzalist();

    def on_get(self, req, resp):
#        s=pizza.getpizzalist()
        msg = {
#            "test": s[0]["name"]
                "msg":"Hellor World!"
        }

        resp.body = json.dumps(msg,ensure_ascii=False)

app = falcon.API()
app.add_route("/", HelloResource())


if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()
