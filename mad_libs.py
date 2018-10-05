def mad_libs(*args):
    text = """
    It was a {}, cold November day. I woke up to the {} smell
    of {} roasting in the {} downstairs. I {} down the
    stairs to see if I could help {} the dinner. My mom said, 'See if
    {} needs a fresh {}.' So I carried a tray of glasses
    full of {} into the {} room. When I got there , I couldn't
    believe my {}! There were {} {} on the {}.""".format(*args)

    return text

args = []
inputs = ["an adjective: ",
          "another adjective: ",
          "a type of a bird: ",
          "a room in a house: ",
          "a verb(past tense): ",
          "a verb: ",
          "a relative's name: ",
          "a noun: ",
          "a liquid: ",
          "a verb ending in -ing: ",
          "a part of the body (plural): ",
          "a plural noun: ",
          "a verb ending in -ing: ",
          "a noun: "]

for i in range(len(inputs)):
    print("Give me ")
    item = input(inputs[i])
    if item == "":
        break
    args.append(item)

print(mad_libs(*args))
