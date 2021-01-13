from behave import *
from FizzBuzz import *


@given('there is a fizzbuzz game')
def step_impl(context):
    context.fizzbuzz = FizzBuzz()


@when('the number is 3')
def step_impl(context):
    context.result = context.fizzbuzz.fizzybuzzy(3)


@then('the output should be \'Fizz\'')
def step_impl(context):
    assert context.result == 'Fizz'


@when('the number is 5')
def step_impl(context):
    context.result = context.fizzbuzz.fizzybuzzy(5)


@then('the output should be \'Buzz\'')
def step_impl(context):
    assert context.result == 'Buzz'


@when('the number is 15')
def step_impl(context):
    context.result = context.fizzbuzz.fizzybuzzy(15)


@then('the output should be \'FizzBuzz\'')
def step_impl(context):
    assert context.result == 'FizzBuzz'


@when('the number is 13')
def step_impl(context):
    context.result = context.fizzbuzz.fizzybuzzy(13)


@then('the output should be \'ani fizz ani buzz\'')
def step_impl(context):
    assert context.result == 'ani fizz ani buzz'


@when('the number is not even a number')
def step_impl(context):
    context.result = context.fizzbuzz.fizzybuzzy("xd")


@then('the output should be \'TypeError\'')
def step_impl(context):
    assert context.result == 'err'
