def list_tuple_from_args(*args):
    return list(args) , args
result = list_tuple_from_args(10,20,30)
print("list:"+str(result[0]))
print("tuple:"+str(result[1]))
