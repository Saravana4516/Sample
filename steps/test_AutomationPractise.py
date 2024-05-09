import pytest
from pytest_bdd import scenario, then, parsers, given, when
from pages.AutomationPractise import AutomationPractise


@pytest.mark.parametrize(['Username','Password'], [('', '')])
@scenario('../features/AutomationPractise.feature', 'Verify the User is able to add the products in QA environment')
def test_TC01_Automation(Username,Password):
    """"""


@then('click on shop menu item')
def step_impl(init_driver):
    # init_driver.get(GlobalVariables.url)
    AP = AutomationPractise(init_driver)
    AP.HomemenuCLick()

    # init_driver.get("https://www.flipkart.com/")