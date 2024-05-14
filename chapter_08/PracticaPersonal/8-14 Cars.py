def make_car(manufacturer, model, **kwargs):
    kwargs[manufacturer] =manufacturer
    kwargs[model] =model
    return kwargs

car1 = make_car('subaru', 'outback', color='blue', tow_package=True)
car2 = make_car('kia', 'serato', color='yelow', tow_package=True)

print(car1)
print()
print(car2)


