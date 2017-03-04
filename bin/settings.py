import sys
import subprocess


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', \
                                                '\33[97m', '\33[93m', \
                                                '\033[1;35m', '\033[1;32m', \
                                                '\033[0m'


def get_py_version(possible=["python", "python2.7"]):
    """
    Return what version of Python is installed
    :param possible: Different python calls for 2.7.x
    :return: 'python' if python 2.7.x is the only installed
             'python27' if more then one version is installed
    """
    items = sys.version
    version = items.split(" ")[0]
    if version.startswith("2.7"):
        return possible[0]
    else:
        return possible[1]


def exec_com(command, py_ver=get_py_version(), sudo=False):
    """
    Execute a command via subprocess call
    :param command: Command to be executed
    :param py_ver: Python version to be called
    :param sudo: Is sudo required?
    :return: Executed command
    """
    command_list = command.split(" ")
    if sudo is True:
        command_list.insert(0, "sudo")
        command_list.insert(1, py_ver)
    else:
        command_list.insert(0, py_ver)
    return subprocess.call(' '.join(command_list), shell=True)
