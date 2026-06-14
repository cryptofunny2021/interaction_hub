# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class InteractionHub(gl.Contract):

    interactions: TreeMap[Address, u256]

    def __init__(self):
        pass

    @gl.public.write
    def record_interaction(self) -> None:
        user = gl.message.sender_address

        current = self.interactions.get(user, u256(0))
        self.interactions[user] = current + u256(1)

    @gl.public.view
    def my_interactions(self) -> u256:
        user = gl.message.sender_address
        return self.interactions.get(user, u256(0))
