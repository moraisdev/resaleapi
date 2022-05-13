import jwt
from settings.configuration import JWT_SECRET_KEY


class VerificationJWT:
    def verify_jwt(self, token):
        try:
            header_data = jwt.get_unverified_header(token)
            header = jwt.decode(token, JWT_SECRET_KEY, algorithms=[header_data["alg"]])
            return header
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."
