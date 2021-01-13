from behave import *
from Roman import *


@given('test converter')
def step_impl(context):
    context.roman = Roman()


@when('given value is 1')
def step_impl(context):
    context.result = context.roman.roman(1)


@then('output should be I')
def step_impl(context):
    assert context.result == 'I'


@when('given value is 2')
def step_impl(context):
    context.result = context.roman.roman(2)


@then('output should be II')
def step_impl(context):
    assert context.result == 'II'


@when('given value is 4')
def step_impl(context):
    context.result = context.roman.roman(4)


@then('output should be IV')
def step_impl(context):
    assert context.result == 'IV'


@when('given value is 6')
def step_impl(context):
    context.result = context.roman.roman(6)


@then('output should be VI')
def step_impl(context):
    assert context.result == 'VI'


@when('given value is 9')
def step_impl(context):
    context.result = context.roman.roman(9)


@then('output should be IX')
def step_impl(context):
    assert context.result == 'IX'


@when('given value is 22')
def step_impl(context):
    context.result = context.roman.roman(22)


@then('output should be XXII')
def step_impl(context):
    assert context.result == 'XXII'


@when('given value is 359')
def step_impl(context):
    context.result = context.roman.roman(359)


@then('output should be CCCLIX')
def step_impl(context):
    assert context.result == 'CCCLIX'


@when('given value is xd')
def step_impl(context):
    context.result = context.roman.roman('xd')


@then('output should be err')
def step_impl(context):
    assert context.result == 'err'
