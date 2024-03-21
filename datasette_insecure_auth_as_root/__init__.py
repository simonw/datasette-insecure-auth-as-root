from datasette import hookimpl


@hookimpl
def actor_from_request():
    return {"id": "root"}
