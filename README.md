# test_awresume.py #
author: Aaron Weitekamp
version: 0.1

## Purpose ##
This Python *unittest* script tests several components of [Aaron Weitekamp's resume](http://resume-aaronweitekamp.rhcloud.com/ "Aaron Weitekamp's resume") site using [Selenium WebDriver](http://seleniumhq.org/projects/webdriver/ "Selenium WebDriver"). It may be used as a starting point template for web site testing.

## Files ##
    README.md (this file)
    test_awresume.py

## Run as ##
    python test_awresume.py [optional python options]

## Requirements and Dependencies ##
* [Selenium 2](http://seleniumhq.org/projects/webdriver/ "Selenium 2") server, WebDriver API
* Python *unittest* module

## Known issues ##
* time.sleep() statements are a hack. The site under test is based on toggling jQuery hide/show elements so waitForPageLoad() doesn't apply. Need to find a more elegant solution.

## Enhancement wish list ##
* Test all major browser types
* Verify all links
* Verify external links return http response header 200 ok
