# Adapted from:
# https://github.com/yash-dk/TorToolkit-Telegram/blob/master/tortoolkit/core/getCommand.py

from ..utils.commands import Commands
from .get_vars import get_val
import os, logging

torlog = logging.getLogger(__name__)


def get_command(command):
    cmd = None

    # Get the command from the constants supplied
    try:
        cmd = getattr(Commands, command)
        torlog.debug(f"Getting the command {command} from file:- {cmd}")
    except AttributeError:
        pass

    # Get the commands form the env [overlap]
    envcmd = os.environ.get(command)
    torlog.debug(f"Getting the command {command} from file:- {envcmd}")
    cmd = envcmd if envcmd is not None else cmd

    if cmd is None:
        torlog.debug(f"None Command Error occured for command {command}")
        raise Exception(
            "The command was not found in either the constants, environment. Command is :- {}".format(
                command))

    cmd = cmd.strip("/")
    cmd += get_val("BOT_CMD_POSTFIX")

    torlog.debug(f"Final resolver for {command} is {cmd}")
    return f"/{cmd}"

def get_command_p(command):
    cmd = None

    # Get the command from the constants supplied
    try:
        cmd = getattr(Commands, command)
        torlog.debug(f"Getting the command {command} from file:- {cmd}")
    except AttributeError:
        pass

    # Get the commands form the env [overlap]
    # try:
    envcmd = os.environ.get(command)
    torlog.debug(f"Getting the command {command} from file:- {envcmd}")
    cmd = envcmd if envcmd is not None else cmd

    if cmd is None:
        torlog.debug(f"None Command Error occured for command {command}")
        raise Exception(
            "The command was not found in either the constants, environment. Command is :- {}".format(
                command))

    return cmd