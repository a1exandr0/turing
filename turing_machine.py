from collections import Counter


class Cond:
    def __init__(self):
        self.actions_mod = {1: [None], 0: [None], '_': [None], 'x': [None], '=': [None]}
        self.actions = [[None], [None], [None]]
        self.number = -1
        self.is_stop = False

    # def set_actions(self, act0=None, act1=None, act2=None):
    #     self.actions[0] = act0
    #     self.actions[1] = act1
    #     self.actions[2] = act2

    def set_actions_mod(self, act0=None, act1=None, act2=None, act3=None, act4=None, act5=None):
        self.actions_mod[0] = act0
        self.actions_mod[1] = act1
        # self.actions_mod['='] = act2
        # self.actions_mod[0] = act3
        # self.actions_mod['^'] = act4
        # self.actions_mod['_'] = act5

    def commit(self, action_on):
        if self.actions_mod[action_on][2] == "L":
            return -1
        elif self.actions_mod[action_on][2] == "R":
            return 1
        else:
            return 0

    def set_number(self, num):
        self.number = num

    def get_action(self, action_on):
        return self.actions_mod[action_on]


def fill_tape(tape):
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


def commit_action(cond_num, operator_pos, conditions, stop_num, count):
    # print(count)
    # if count>30:
    print(tape)
    #     return
    # # if cond_num == stop_num:
    #     c = Counter(tape)
    #     print(tape)
    #     print(c)
    #     return
    cell_value = tape[operator_pos+1]
    # print("condition   {}".format(cond_num))
    # print("operator on   {}".format(tape[operator_pos+1]))
    # print(tape)
    next_operator_pos = operator_pos + conditions[cond_num].commit(cell_value)
    tape[operator_pos+1] = conditions[cond_num].get_action(cell_value)[1]
    next_cond_num = conditions[cond_num].get_action(cell_value)[0]
    # print(conditions[cond_num].commit(cell_value))
    buff = tape[next_operator_pos]
    tape[next_operator_pos] = '*'
    tape[operator_pos] = buff
    count += 1

    return [next_cond_num, next_operator_pos, conditions, stop_num, count]


if __name__ == '__main__':
    stop_cond = 0
    tape = [0 for _ in range(10**5 + 10000)]
    tape = fill_tape(tape)
    start = tape.index('*')

    conditions = []
    f = open("conditions.txt", 'r')
    buff = f.readlines()                            #parse
    for i in range(len(buff)):
        buff[i] = buff[i][:-1].split('*')
        for j in range(len(buff[i])):
            buff[i][j] = buff[i][j].split(' ')
    # print(buff)

    c = Cond()
    conditions.append(c)
    for i in range(1, len(buff)):
        for j in range(len(buff[i])):
            for m in range(len(buff[i][j])):
                try:
                    buff[i][j][m] = int(buff[i][j][m])
                except:
                    pass
        c = Cond()
        c.set_number(i)
        # print(c.number)
        c.set_actions_mod(buff[i][0], buff[i][1])  # buff[i][2], buff[i][3], buff[i][4]....) //add more conditions
        # print(c.get_action(0))
        # print(c.get_action(1))
        # print(c.get_action(2))
        conditions.append(c)
    res = commit_action(38, start, conditions, 0, 0)
    while res[0] != stop_cond:
        # if res[4] == 25:
        #     break
        try:
            res = commit_action(res[0], res[1], res[2], res[3], res[4])
        except:
            raise Exception("bugged, wrong(bad) condition table or tape values, results are invalid")
    c = Counter(tape)
    print('res == {}'.format(c[1]-1))
    print(tape)
    print(res[4])