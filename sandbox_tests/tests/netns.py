"""
description: lo is the only interface and is down
script: |
  expect(
    run(exe="/usr/bin/ip", argv=["link"]),
    stdout="1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN mode DEFAULT group default qlen 1000\n    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00\n"
  )
"""

# TODO "empty" tests
