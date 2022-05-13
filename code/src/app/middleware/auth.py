from functools import wraps

import jwt
from flask import request
from src.app.settings import Configuration


def ResponseError(message):
    return {"message": message, "status": 401}, 401


def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if Configuration.ENV in ["development", "disable_auth"]:
            try:
                return f(*args, **kwargs)
            except Exception as e:
                return ResponseError(e)

        token, audit, user = "", "", {}
        try:
            token = request.headers.get("Authorization").split(" ")[1]
        except Exception as e:
            return ResponseError("Not authorized")

        try:
            if token != Configuration.TOKEN:
                user = jwt.decode(
                    token, Configuration.JWT_SECRET_KEY, algorithms=["HS256"]
                )
        except Exception as e:
            return ResponseError(f"Not authorized")

        try:
            response = f(*args, {**dict(kwargs), **{"user": user.get("sub", None)}})
            return response
        except Exception as e:
            return ResponseError(f"Error Exception detected: {e}")

    return wrapper
