Feature: Trains1

  Background: common steps
    Given open the chrome browser
    When  Enter the URL

    Then  click on the Train Icon


    Scenario: Train bokking
      Given click on "From" text field
      When Enter the cityname in Fromserch
      Then it will select that particular city
      Then  click on "To" text field
      And Enter the city name in Tosearch
      And it will select the particular city
      Then click on "Searchbutton"
      Then click on "DateofJourney"
      And select the month
      And select the Date
      Then Click the particular train
      And Enter the Mobile number
      And Enter the given OTP
      And Now click on submit button
      Then Click on checkavailabity
      And select the train
      And Enter the IRCTC user id
      And Click on proceed button