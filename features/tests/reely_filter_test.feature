Feature: Test reelly filter options
    Scenario: User can filter the Secondary deals by “want to buy” option
        Given Open reelly main page
        When Log in to the page
        When Click on “Secondary” option at the left side menu
        Then Verify the right page opens
        When Click on Filters
        And Filter the products by “want to buy”
        And Click on Apply Filter
        Then Verify all cards have “Want to buy” tag