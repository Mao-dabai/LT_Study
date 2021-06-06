*** Variables ***
${appium_server}    http://localhost:4723/wd/hub
&{MuMu}


*** Keywords ***
启动小米商城
    open application    http://localhost:4723/wd/hub
    ...                 platformName=Android    appPackage=com.xiaomi.shop
    ...                 appActivity=.activity.MainTabActivity   noReset=True
    sleep               10


