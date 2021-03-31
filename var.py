"""
  DASH TOOLS
  Author: Author: DR4G0N5, JARED, Bomb SQU4D
  Version: 0.0.4
"""


import datetime
import getpass
import os
import socket
import subprocess
import textwrap
import time


class PyColors:
    reset = "\033[00m"
    bold = "\033[01m"
    underline = "\033[04m"
    slow_blink = "\033[05m"
    dim = "\033[2m"
    reverse = "\033[7m"
    hidden = "\033[8m"

    class Fg:
        black = "\033[30m"
        dark_red = "\033[31m"
        dark_green = "\033[32m"
        dark_yellow = "\033[33m"
        dark_blue = "\033[34m"
        dark_purple = "\033[35m"
        dark_cyan = "\033[36m"
        dark_grey = "\033[90m"
        light_grey = "\033[37m"
        light_red = "\033[91m"
        light_green = "\033[92m"
        light_yellow = "\033[93m"
        light_blue = "\033[94m"
        light_purple = "\033[95m"
        light_cyan = "\033[96m"
        light_white = "\033[97m"
        # orange = "\033[48:2:255:165:0m%s"

    class Bg:
        black = "\033[40m"
        dark_red = "\033[41m"
        dark_green = "\033[42m"
        dark_yellow = "\033[43m"
        dark_blue = "\033[44m"
        dark_purple = "\033[45m"
        dark_cyan = "\033[46m"
        dark_grey = "\033[100m"
        light_grey = "\033[47m"
        light_red = "\033[101m"
        light_green = "\033[102m"
        light_yellow = "\033[103m"
        light_blue = "\033[104m"
        light_purple = "\033[105m"
        light_cyan = "\033[106m"
        light_white = "\033[107m"


def hostname_resolves(hostname):
    try:
        socket.gethostbyname(hostname)
        return 1
    except socket.error:
        return 0


def resolve_ip(host):
    result = os.popen("dig 0.0.0.0 axfr | grep -F " + host).readlines()
    print(result)
    if len(result) > 0:
        partitioned_result = result.rpartition(" ")[0]
        print(partitioned_result)
        return partitioned_result
    else:
        second_result = os.popen("dig @0.0.0.0 axfr | grep -F " + host).readlines()
    if len(second_result) > 0:
        partitioned_result = second_result.rpartition(" ")[0]
        return partitioned_result
    else:
        return "UNKNOWN"


def get_ip(node):
    try:
        address_one = socket.gethostbyname_ex(node)
        address_two = str(address_one[2]).replace("['", "").replace("']", "")
        return address_two
    except socket.gaierror:
        print("\n" + node + " - does not exist in DNS\n\n")


def get_hostname(node):
    try:
        address_one = socket.gethostbyaddr(node)
        address_two = address_one[0]
        return address_two
    except socket.gaierror:
        return "UNKNOWN"
    except socket.herror:
        return "UNKNOWN"


def can_ping_ip(hostname):
    pingable = subprocess.call(["ping", "-q", "-c", "3", hostname], stdout=subprocess.DEVNULL)
    return pingable


def get_ip_and_ping(hostname):
    hostname_ip = get_ip(hostname)
    hostname_pingable = can_ping_ip(hostname_ip)
    if hostname_pingable == 0:
        return 0
    else:
        return 1


def resolve_and_get_ip(hostname):
    host_resolves = hostname_resolves(hostname)
    if host_resolves == 1:
        hostname_ip = get_ip(hostname)
        return hostname_ip
    if host_resolves == 0:
        return False


def resolve_and_ping(hostname):
    host_resolves = hostname_resolves(hostname)
    if host_resolves == 1:
        hostname_ip = get_ip(hostname)
        hostname_pingable = can_ping_ip(hostname_ip)
        if hostname_pingable == 0:
            return 0
        else:
            return 1
    else:
        return 2


def get_username():
    username = input(" Username: ").strip()
    return username


def get_password():
    password = getpass.getpass(" Password: ").strip()
    return password


def get_today():
    today = time.strftime("%b %d", time.localtime())
    return today


def get_now():
    now = time.strftime("Time: %H:%M:%S Date: %m-%d-%Y", time.localtime())
    print(
        "\n\n",
        PyColors.Bg.dark_cyan,
        now,
        PyColors.reset,
        "\n"
    )


def get_yesterday():
    yesterday = datetime.datetime.strftime(
        datetime.datetime.now() - datetime.timedelta(1),
        "%b %d"
    )
    return yesterday


def get_two_days_ago():
    yesterday = datetime.datetime.strftime(
        datetime.datetime.now() - datetime.timedelta(2),
        "%b %d"
    )
    return yesterday


def print_lines():
    pass
    """
    print(
        "\n",
        PyColors.bold,
        PyColors.Fg.dark_red,
        "=" * 20,
        PyColors.reset,
        "\n\n"
    )"""


def print_arrows():
    pass
    """
    print(
        "\n\n\t",
        PyColors.bold,
        PyColors.Fg.light_green,
        "="*20,
        PyColors.reset,
        "\n\n"
    )"""


def text_wrapper(string, initial, subsequent):
    new_string = "\n".join([line.strip() for line in string.splitlines()])
    wrapper = textwrap.TextWrapper(
        width=82,
        initial_indent=initial,
        subsequent_indent=subsequent,
        drop_whitespace=True
    )
    new_wrapper = wrapper.fill(new_string.strip("\n"))
    print(new_wrapper)
