Feature: default feature some extra conditions etc.

  @what
  Scenario: first default Scenario
    Given bunch of different words
      """
      Ala ma kota Sasza szedł szosą Jola nielojalna Jola lojalna Magikus gigantus benc
      """
    When divide text by words
    And count them up
    Then result is 13

  @what
  Scenario: second default Scenario
    Given bunch of different words
    """
    Ala ma kota
    """
    When we remove spaces
    And count letters
    Then result is 9

  @what
  Scenario: third default Scenario
    Given bunch of different numbers
    """
    1 2 3 4 5 6 7 8 9
    """
    When we split them
    And sum up by changing to ints
    Then result is 45

  @what
  Scenario: fourth default Scenario
    Given one string like "drzewo"
    And another one like "liscie"
    When we compare them
    Then we can see they are not the same

  @what
  Scenario: fifth default Scenario
    Given one string like "drzewo"
    And another one like "drzewo"
    When we compare them
    Then we can see they are the same

  @what
  Scenario: sixth default Scenario
    Given one string like "drzewo"
    And another one like "liscie"
    When we compare the length of them
    Then we can see length is the same

  @what
  Scenario: seventh default Scenario
    Given one string like "drzewo"
    And another one like "igly"
    When we compare the length of them
    Then we can see length is different

  @what
  Scenario: last one default Scenario
    Given one string consists of three numbers
    """
    123
    """
    When we change the type of it to int
    And divide by 3
    Then get result 41