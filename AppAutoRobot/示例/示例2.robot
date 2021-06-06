*** Setting ***
Library   AppiumLibrary



*** Test Cases ***
测试小米商城1
    Open Application    http://localhost:4723/wd/hub
    ...                 platformName=Android    appPackage=com.xiaomi.shop
    ...                 appActivity=.activity.MainTabActivity
    Click Element       xpath=//*[@text='同意']
    sleep               5
#    Click Element       xpath=//*[@text='允许']

测试小米商城2
    open application   http://localhost:4723/wd/hub
    ...                platformName=Android  appPackage=com.xiaomi.shop  appActivity=.activity.MainTabActivity
#    ...     90   50    10   50           noReset=True
    click element      xpath=//*[@text="同意"]
    sleep              1
#    click element      xpath=//*[@text="允许"]
    sleep              5
    swipe by percent   90   50    10   50
    sleep              1
    swipe by percent   90   50    10   50
    sleep              6
    click element      class=android.widget.ImageView
    sleep              3
    click element      xpath=//*[@text="分类"]
    click element      xpath=//*[@text="小米手机"]
