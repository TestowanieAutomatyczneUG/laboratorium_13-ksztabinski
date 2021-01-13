Feature: dec to roman converter

  Scenario: first test
    Given test converter
    When given value is 1
    Then output should be I

  Scenario: second test
    Given test converter
    When given value is 2
    Then output should be II

  Scenario: third test
    Given test converter
    When given value is 4
    Then output should be IV

  Scenario: fourth test
    Given test converter
    When given value is 6
    Then output should be VI

  Scenario: fifth test
    Given test converter
    When given value is 9
    Then output should be IX

  Scenario: sixth test
    Given test converter
    When given value is 22
    Then output should be XXII

  Scenario: seventh test
    Given test converter
    When given value is 359
    Then output should be CCCLIX

  Scenario: eighth test
    Given test converter
    When given value is xd
    Then output should be err