from sqlite3 import Cursor

from src.app.services.mongo import mongo_connection


def verification_sales_channel(type, sales_channel_id):
    try:
        sales_channel = mongo_connection().channel.find_one(
            {"sales_channel_id": sales_channel_id}
        )
        if sales_channel["type_sales_channel"] == type:
            return True
        else:
            return False
    except Exception as e:
        return e


def verification_wallet_listing(wallet_listing_id):
    try:
        item = []
        for wallet_item in wallet_listing_id:
            query = mongo_connection().wallet.find_one(
                {"wallet_listing_id": wallet_item}
            )
            item.append(query["type"])
            print(item)
        direct_sale = item.count("Venda Direta")
        auction = item.count("Leilão")
        none = item.count(None)
        if direct_sale > 1:
            return False
        if auction > 1:
            return False
        if none >= 1:
            return False
        else:
            return True
    except Exception as e:
        return e


def list_portal():
    try:
        cursor = mongo_connection().property.find({})
        for document in cursor:
            return document
    except Exception as e:
        return e
