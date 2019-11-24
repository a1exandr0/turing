# turing
tape.txt is initial condition of machine tape.
conditions.txt have all the conditions(each line is condition) for different cell values(before and after * sign in conditions.txt)

Each tape element must be separated by space from other elements

each action is defined next way:
1st block tells us next condition
2nd block tells us what value we put in current cell
3rd tells how do we move tape L - left R - right S - stay

p in conditions means unfilled field and program acts normal with it

As an example:
p p p*p p p    0cond
1 0 R*0 0 S    1cond

lets say 0 is our stop condition

and 1 is start condition

that means that when machine is in condition 1 and it has cell with value 0 it sets 1 as next condition puts 0 as cell value and goes right.

And when cell value is 1 it puts 0 as cell value sets 0 as next condition and stays on exact cell
