#!/usr/bin/env python3
# https://github.com/piiyush135/Packet-Sniffer

__author__ = "piiyush135 @ keybase.io/piiyush135"

import PyInstaller.__main__ as pyinstaller


"""Set up the arguments required by PyInstaller to build the Network
Packet Sniffer binary."""
pyinstaller.run(("packet_sniffer/core.py", "--onefile"))
