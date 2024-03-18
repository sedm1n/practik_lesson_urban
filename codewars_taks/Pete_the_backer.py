def cakes(recipe, available):
    count_list = []
    for item in recipe:
        count_list.append(available.get(item,0)//recipe.get(item,0))

    return min(count_list)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))