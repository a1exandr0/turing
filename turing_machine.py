from collections import Counter


class Cond:
    """
    Class used to define conditions of turing machine(basically its algorithm)
    """
    def __init__(self):
        """
        Creates object of class.
        Fields:
            actions_mod: Sets command on character (Stop or Left or Right)
            number: Number of condition
        """
        self.actions_mod = {1: [None], 0: [None]}
        self.number = -1

    def set_actions_mod(self, act0=None, act1=None):
        """
        Defines actions of Turing machine on current condition.
        :param act0:
        :param act1:
        :return:
        """
        self.actions_mod[0] = act0
        self.actions_mod[1] = act1

    def commit(self, action_on):
        """
        Converts action character to int, in order to move pointer on tape of machine.
        :param action_on: character
        :return:
        """
        if self.actions_mod[action_on][2] == "L":
            return -1
        elif self.actions_mod[action_on][2] == "R":
            return 1
        else:
            return 0

    def get_action(self, action_on):
        """
        Gets a action character from cell value.
        :param action_on:
        :return:
        """
        return self.actions_mod[action_on]


def fill_tape(tape):
    """
    Parses tape initial condition into tape array.
    :param tape: array to be filled
    :return: filled array
    """
    file = open('tape.txt', 'r')
    g = file.readline()
    h = g.split('0')
    print(" a == {}".format(len(h[1].replace(' ', ''))-1))
    print(" b == {}".format(len(h[2].replace(' ', ''))-1))
    g = g.split()

    for i in range(len(g)):
        try:
            tape[i+5] = int(g[i])#add here
        except:
            tape[i+5] = g[i]#and here

    print(tape)

    return tape


def commit_action(cond_num, operator_pos, conditions, count):
    """
    Commits single iteration of turing machine
    :param cond_num: int() number of condition
    :param operator_pos: int() position of pointer on machine tape
    :param conditions: list() list of all conditions
    :param count: int() iteration counter
    :return:
    """
    # print(tape)
    cell_value = tape[operator_pos+1]
    # print("condition   {}".format(cond_num))
    # print("operator on   {}".format(tape[operator_pos+1]))
    # print(tape)
    next_operator_pos = operator_pos + conditions[cond_num].commit(cell_value)
    tape[operator_pos+1] = conditions[cond_num].get_action(cell_value)[1]
    next_cond_num = conditions[cond_num].get_action(cell_value)[0]
    buff = tape[next_operator_pos]
    tape[next_operator_pos] = '*'
    tape[operator_pos] = buff
    count += 1

    return [next_cond_num, next_operator_pos, conditions, count]


if __name__ == '__main__':
    stop_cond = 0
    tape = [0 for _ in range(10**5 + 10000)]
    tape = fill_tape(tape)
    start = tape.index('*')

    conditions = []
    f = open("conditions.txt", 'r')
    buff = f.readlines()  # parse

    for i in range(len(buff)):
        buff[i] = buff[i][:-1].split('*')
        for j in range(len(buff[i])):               # Parse conditions from file
            buff[i][j] = buff[i][j].split(' ')

    # print(buff)

    c = Cond()
    conditions.append(c)

    for i in range(1, len(buff)):
        for j in range(len(buff[i])):               # Create conditions list using Cond() class
            for m in range(len(buff[i][j])):
                try:
                    buff[i][j][m] = int(buff[i][j][m])
                except:
                    pass

        c = Cond()
        c.number = i
        c.set_actions_mod(buff[i][0], buff[i][1])
        conditions.append(c)

    res = commit_action(38, start, conditions, 0)  # start turing machine with start condition 38(depends on coditions table)

    while res[0] != stop_cond:
        try:
            res = commit_action(res[0], res[1], res[2], res[3])
        except:
            raise Exception("bugged, wrong(bad) condition table or tape values, results are invalid")

    c = Counter(tape)
    print('res == {}'.format(c[1]-1))
    print(tape)  #
    print("Number of iterations was {}".format(res[4]))