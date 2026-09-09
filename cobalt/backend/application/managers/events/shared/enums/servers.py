#  Copyright (C) 2026 Artorias
#  Author: Artorias
#  Repository: https://github.com/artorias-developer/cobalt
#  SPDX-License-Identifier: AGPL-3.0-or-later

from enum import StrEnum


class ServerEventEnum(StrEnum):
    """
    WebSocket servers events enum.
    """
    SUBSCRIBE_STATES = "servers_subscribe_states"
    UNSUBSCRIBE_STATES = "servers_unsubscribe_states"
    SERVER_STATE = "server_state"
