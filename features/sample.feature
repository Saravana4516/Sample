Feature:


   @sample01    @Regression
  Scenario Outline: Verify the login functionality
    Given I Launch the application url
     Then Add products to the cart

    Examples:
      | Username | Password |
      | 123      | 123      |


   @sample02    @Regression
  Scenario Outline: Verify the login functionality for second
    Given I Launch the application url
    #Then  select the product and add to cart

    Examples:
      | Username | Password |
      | 123      | 123      |