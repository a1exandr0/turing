# turing
tape.txt is initial condition of machine tape.
conditions.txt have all the conditions(each line is condition) for different cell values(before and after * sign in conditions.txt)

CURRENT PROBLEM is unary multiplication, as an example "0 0 1 1 1 0 1 1 1 1 0" means 2*4 
and should return "1 1 1 1 1 1 1 1 1"

Each tape element must be separated by space from other elements

each action is defined next way:
1st block tells us next condition
2nd block tells us what value we put in current cell
3rd tells how do we move tape L - left R - right S - stay

p in conditions means unfilled field and program acts normal with it

As an example:

p p p*p p p

1 0 R*0 0 S

Lets say 0 is our stop condition, and 1 is start condition

That means that when machine is in condition 1 and it has cell with value 0 it sets 1 as next condition puts 0 as cell value and goes right.

And when cell value is 1 it puts 0 as cell value sets 0 as next condition and stays on that cell.
