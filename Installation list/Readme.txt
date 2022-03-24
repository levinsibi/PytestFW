1.allure zip shall be expanded and placed in a folder and the path of bat file shall be provided in env. variable
2.To generate allure reports run command allure serve "reports and log path"-shall be done with cmd admin


### mandatory installations required ####
#1.pip install pytest
#2.pip install pytest-xdist  -->for parallel execution
#3.pip install pytest-html   -->for html reports
#4.pip install pytest-failed-screenshot   -->for failure will attach screenshot in allure report
#5.pip install allure-pytest  -->for allure reports

execution commands
----------------------

HTML report
#pytest test_Home.py -v -s --capture sys --html="FirstReport.html"
allure report with screenshot
## pytest  --screenshot=on --screenshot_path=on D:\PytestDemo\Tests\screenshot -v -s --capture sys --alluredir="../Reports" test_HomeAllure.py

Generic execution commands
-------------------------
#start with test or end with test.class name also shall be starting with test
# py.test will execute all test_ methods from the suite
# py.test classname will execute tests from the mentioned class
# py.test -k login will execute all test methods having login in its test name.this is similar to groups in testng
# py.test -k login -v .-v--->giving more info on console -s--->shows print stmts
# py.test -n 5  -->will execute tests in parallel with 5 threads


### deleted folders
1.scripts
2.Lib
3.allure zip()