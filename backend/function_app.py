import azure.functions as func
import json
import logging

app = func.FunctionApp()  # no global auth here

@app.function_name(name="http_trigger")
@app.route(route="http_trigger", methods=["GET", "POST"], auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    name = req.params.get("name")
    if not name:
        try:
            body = req.get_json()
            name = body.get("name")
        except ValueError:
            name = None
    return func.HttpResponse(
        json.dumps({"ok": True, "message": f"Hello, {name or 'world'}"}),
        mimetype="application/json",
        status_code=200,
    )
