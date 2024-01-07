from buff163_unofficial_api import Buff163API
from buff163_unofficial_api.cs_enums import *

# This specific example does not need a cookie
# This is how the cookie should be formatted
cookie = "Device-Id=_; Locale-Supported=_; game=_; NTES_YD_SESS=_; S_INFO=_; P_INFO=_; remember_me=_; session=_; csrf_token=_"

buff163api = Buff163API(session_cookie=cookie)

market = buff163api.get_item_market(category=Gun.AK47)

for item in market:
    print(f"{item.market_hash_name}")
    print(f"¥ {item.sell_min_price}\n")
