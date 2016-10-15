import sys


def read_stdin_integers() -> list:
    """

    :rtype: list
    """
    lines = sys.stdin.readlines()
    lines = [int(x.strip()) for x in lines]
    return lines


def write_stdout_anything(list_to_write):
    list_to_write = [str(x) for x in list_to_write]
    sys.stdout.writelines(list_to_write)


def intro_division(integer_list):
    ret = list()
    ret.append(integer_list[0]//integer_list[1])
    ret.append(integer_list[0]/integer_list[1])
    return(ret)


if __name__ == '__main__':
    write_stdout_anything(intro_division(read_stdin_integers()))
