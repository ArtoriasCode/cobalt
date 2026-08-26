#  Copyright (C) 2026 Artorias
#  Author: Artorias
#  Repository: https://github.com/artorias-developer/cobalt
#  SPDX-License-Identifier: AGPL-3.0-or-later

from enum import StrEnum


class LogEventEnum(StrEnum):
    """
    WebSocket logs events enum.
    """
    SUBSCRIBE_HOST = "logs_subscribe_host"
    SUBSCRIBE_SERVER = "logs_subscribe_server"
    UNSUBSCRIBE_HOST = "logs_unsubscribe_host"
    UNSUBSCRIBE_SERVER = "logs_unsubscribe_server"
    HOST_LOG = "host_log"
    SERVER_LOG = "server_log"