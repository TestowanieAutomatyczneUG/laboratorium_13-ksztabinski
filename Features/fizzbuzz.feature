Feature: FizzBuzz Game

  Scenario: first game
    Given there is a fizzbuzz game
    When the number is 3
    Then the output should be 'Fizz'

  Scenario: second game
    Given there is a fizzbuzz game
    When the number is 5
    Then the output should be 'Buzz'

  Scenario: third game
    Given there is a fizzbuzz game
    When the number is 15
    Then the output should be 'FizzBuzz'

  Scenario: fourth game
    Given there is a fizzbuzz game
    When the number is 13
    Then the output should be 'ani fizz ani buzz'

  Scenario: fifth game
    Given there is a fizzbuzz game
    When the number is not even a number
    Then the output should be 'TypeError'