# v0.2.3 - Connected to Reputation & Token (بدون Redeploy)
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class InteractionHub(gl.Contract):

    interactions: TreeMap[Address, u256]
    
    # آدرس‌های ثابت قراردادهای دیگه 
    REPUTATION_ADDRESS = Address("0x58a73d1dC168B4BAdf5965758656d37d963e4a81")
    TOKEN_ADDRESS = Address("0xeA166C0845904c919A5CD501465976B8d03dBfE6")

    def __init__(self):
        pass

    @gl.public.write
    def record_interaction(self) -> None:
        user = gl.message.sender_address

        # ثبت تعامل
        current = self.interactions.get(user, u256(0))
        self.interactions[user] = current + u256(1)

        # اتصال به Reputation Scoring
        try:
            rep = gl.contract(self.REPUTATION_ADDRESS)
            rep.record_action(u256(10))        # ۱۰ امتیاز reputation
        except:
            pass  # اگر ارور داد، ادامه بده

        # اتصال به Dynamic Token
        try:
            token = gl.contract(self.TOKEN_ADDRESS)
            token.mint(u256(5))                # ۵ توکن پاداش
        except:
            pass  # اگر ارور داد، ادامه بده

    @gl.public.view
    def my_interactions(self) -> u256:
        user = gl.message.sender_address
        return self.interactions.get(user, u256(0))
