import pytest
from pytest_bdd import scenario, then , parsers, given, when
import time

from utility import GlobalVariables


#from utility import GlobalVariables


#sample scenario
@pytest.mark.parametrize(['Username','Password'],[('','')])
@scenario('../features/sample.feature','Verify the login functionality')
def test_sample01(Username,Password):
    """"""



#sample scenario
@pytest.mark.parametrize(['Username','Password'],[('','')])
@scenario('../features/sample.feature','Verify the login functionality for second')
def test_sample02(Username,Password):
    """"""

@given(parsers.cfparse('I Launch the application url "{env}"'))
def launch_app(init_driver,env):
    with open('config/envInfo.yaml', 'r') as f:
        info = yaml.safe_load(f)
    if (env == 'QA'):
        GlobalVariables.url = info["REGION"]["QA"]["url"]

    init_driver.get(GlobalVariables.url)
    #init_driver.get("https://www.flipkart.com/")