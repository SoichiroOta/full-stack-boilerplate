class MainHealthCheckResource:
    def on_get(self, req, resp):
        resp.media = {
            "status": True
        }
