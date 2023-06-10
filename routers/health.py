from fastapi.responses import PlainTextResponse

def api_health(app):
    @app.get("/health", response_class=PlainTextResponse)
    def health_check():
        return "ok"
