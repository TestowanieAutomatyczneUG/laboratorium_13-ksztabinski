from behave import *


@Given('bunch of different words')
def step_impl(context):
    context.smth = context.text


@When('divide text by words')
def step_impl(context):
    context.whole = context.smth.split()


@Step('count them up')
def step_impl(context):
    context.result = len(context.whole)


@Then('result is 13')
def step_impl(context):
    assert context.result == 13


@When('we remove spaces')
def step_impl(context):
    context.whole = context.smth.replace(" ", "").strip()


@Step('count letters')
def step_impl(context):
    context.result = len(context.whole)


@Then('result is 9')
def step_impl(context):
    assert context.result == 9


@Given('bunch of different numbers')
def step_impl(context):
    context.smth = context.text


@When('we split them')
def step_impl(context):
    context.whole = context.smth.split()


@Step('sum up by changing to ints')
def step_impl(context):
    context.result = 0
    for num in context.whole:
        context.result += int(num)


@Then('result is 45')
def step_impl(context):
    assert context.result == 45


@Given('one string like {string1}')
def step_impl(context, string1):
    context.str1 = string1


@Step('another one like {string2}')
def step_impl(context, string2):
    context.str2 = string2


@When('we compare them')
def step_impl(context):
    if context.str1 == context.str2:
        context.bool = True
    else:
        context.bool = False


@Then('we can see they are not the same')
def step_impl(context):
    assert context.bool is False


@Then('we can see they are the same')
def step_impl(context):
    assert context.bool is True


@When('we compare the length of them')
def step_impl(context):
    if len(context.str1) == len(context.str2):
        context.bool = True
    else:
        context.bool = False


@Then('we can see length is the same')
def step_impl(context):
    assert context.bool is True


@Then('we can see length is different')
def step_impl(context):
    assert context.bool is False


@Given('one string consists of three numbers')
def step_impl(context):
    context.notIntYet = context.text


@When('we change the type of it to int')
def step_impl(context):
    context.finnalyInt = int(context.notIntYet)


@Step('divide by 3')
def step_impl(context):
    context.result = context.finnalyInt/3


@Then('get result 41')
def step_impl(context):
    assert context.result == 41
