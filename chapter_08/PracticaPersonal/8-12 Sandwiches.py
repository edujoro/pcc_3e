def sandwich_ingredients(*ingredients):
    for ingredient in ingredients:
        print(ingredient)
    print()
    
sandwich_ingredients('queso')
sandwich_ingredients('queso', 'huevo')
sandwich_ingredients('mayonesa','quetchup','mostasa','papas')
