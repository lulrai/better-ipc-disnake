"""
Better IPC
~~~~~~~~~~

High-performance inter-process communication 
library designed to work with the latest version of discord.py

:copyright: (C) 2022 DaPandaOfficial
:license: GNU GENERAL PUBLIC LICENSE
"""
import disnake

if disnake.version_info.major < 2:
    raise RuntimeError("You must have disnake (v2.0 or greater) to use this library.")

__title__ = "better-ipc-disnake"
__author__ = "Raizusekku"
__license__ = "GNU GENERAL PUBLIC LICENSE"
__copyright__ = "Copyright (C) 2022 Raizusekku"
__version__ = "2.0.1"


from .errors import BaseException, NoEndpointFoundError, MulticastFailure, InvalidReturn, ServerAlreadyStarted
from .client import Client
from .server import Server
from .objects import ClientPayload, ServerResponse


