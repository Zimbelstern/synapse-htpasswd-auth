from typing import Awaitable, Callable, Optional, Tuple

import bcrypt
import synapse
from synapse import module_api

class HtpasswdAuthProvider:
    def __init__(self, config: dict, api: module_api):
        self.api = api
        api.register_password_auth_provider_callbacks(
            auth_checkers = {
                ("m.login.password", ("password",)): self.htpasswd_check,
            }
        )

        self.path = config.get("htpasswd_path")


    async def htpasswd_check(
        self,
        username: str,
        login_type: str,
        login_dict: "synapse.module_api.JsonDict",
    ) -> Optional[
        Tuple[
            str,
            Optional[Callable[["synapse.module_api.LoginResponse"], Awaitable[None]]],
        ]
    ]:

        if login_type != "m.login.password":
            return None
        with open(self.path, "r") as p:
            for line in p:
                line = line.strip("\n")
                if line.split(":", 1)[0] == username.split(":", 1)[0][1:] and bcrypt.checkpw(login_dict.get("password").encode(), line.split(":", 1)[1].encode()):
                    return (self.api.get_qualified_user_id(username), None)

        return None
