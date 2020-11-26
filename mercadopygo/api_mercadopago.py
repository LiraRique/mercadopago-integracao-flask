import mercadopago
import json

CLIENT_ID = '1280735590581038'
CLIENT_SECRET = 'hygp27SZgrXEoNzMM8zJ22LxNL6BnkWe'


def payment(req, **kwargs):
    product = kwargs['product']
    preference = {
      "items": [
        {
          "title": product.name,
          "quantity": product.quantity,
          "currency_id": "BRL",
          "unit_price": product.price
        }
      ]
    }

    mp = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)

    preferenceResult = mp.create_preference(preference)

    url = preferenceResult["response"]["init_point"]
    
    return url
