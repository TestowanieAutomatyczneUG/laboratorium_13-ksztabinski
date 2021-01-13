
def before_scenario(context, scenario):
    print(f'now {scenario}')


def after_scenario(context, scenario):
    print(f'{scenario} has ended')
