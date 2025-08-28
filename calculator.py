def add(n1,n2):
    return n1+n2


def sub(n1,n2):
    return n1-n2


def mul(n1,n2):
    return n1*n2


def div(n1,n2):
    return n1/n2


my_dict = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}
def calculator():
    should_continue = True
    n1 = int(input())
    while(should_continue):


        for symbol in my_dict:
            print (symbol)
        user_input = input()
        n2 = int(input())
        result = my_dict[user_input](n1,n2)
        print(result)

        repeat = input("Type yes to continue and no to Restart").lower()
        if repeat == "yes":
            n1 = result
        else:
            should_continue = False
            print("\n"*20)
            calculator()
calculator()