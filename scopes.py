



# x = 10
# def test():
#     x = 20
#     print(x)
    
# test()
# print(x)





# x = "global"

# def outer():
#     x = "outer"

#     def inner():
#         print(x)                                

#     inner()

# outer()

# def outer():
#     x = 10

#     def inner():
#         nonlocal x
#         x = 20

#     inner()
#     print(x)

# outer()




# x = 10

# def test():
#     print(x)
#     x = 20

# test()



# x = 10

# def outer():
#     x = 20

#     def inner():
#         print(x)

#     inner()

# outer()
# print(x)









x = 10

def outer():
    x = 20

    def inner():
        global x
        x = 30

    inner()
    print(x)

outer()
print(x)



x = 5

def outer():
    x = 10

    def inner():
        print(x)
        x = 20

    inner()

outer()