from selenium.webdriver.common.by import By

locator_url = "com.dejavoosystems.wizarpos:id/"

class CommonLocators(object):
    SEARCH_ELEMENT = (By.ID, locator_url + "ibOption")
    OPTION_SEARCH = (By.ID, locator_url + "etSearch")
    TV_VALUE = (By.ID, locator_url + "tvValue")
    TV_NAME = (By.ID, locator_url + "tvName")
    TV_TEXT = (By.ID, locator_url + "tvText")
    TV_TITLE = (By.ID, locator_url + "tvTitle")
    TV_HINT = (By.ID, locator_url + "tvHint")
    TV_PHONE = (By.ID, locator_url + "tvPhone")
    TV_QUICK = (By.ID, locator_url + "tvQuick")
    TV_ORDER_TYPE = (By.ID, locator_url + "tvOrderType")
    PAYMENT_TOOL = (By.ID, locator_url + "btnPaymentTool")
    ET_FIELD = (By.ID, locator_url + "etField")
    ACTV_TEXT = (By.ID, locator_url + "actvText")

class CartPageLocators(object):
    BUTTON_ADD_ITEM = (By.ID, locator_url + "llNewItem")
    BUTTON_SEARCH_ITEMS = (By.ID, locator_url + "btnSearch")
    BUTTON_RETURN = (By.ID, locator_url + "imgIcon")
    BUTTON_UP = (By.ID, locator_url + "btnUp")
    BUTTON_DOWN = (By.ID, locator_url + "btnDown")
    BUTTON_NEXT = (By.ID, locator_url + "btnNext")
    BUTTON_PREVIOUS = (By.ID, locator_url + "btnPrevious")
    BUTTON_SAVE_ITEM_IN_CART = (By.ID, locator_url + "btnSave")
    BUTTON_SAVE = (By.CSS_SELECTOR, "[content-desc='OperationButtons.Save']")
    BUTTON_OPEN_COLOR_PICKER = (By.ID, locator_url + "ivStart")
    BUTTON_CREATE_CATEGORY = (By.ID, locator_url + "tvAddCategory")
    BUTTON_CREATE_ITEM = (By.ID, locator_url + "llNewPosition")
    BUTTON_CHOOSE_PICTURE = (By.ID, locator_url + "tvPlaceholder")
    BUTTON_OPEN_GALLERY = (By.CSS_SELECTOR, "[content-desc='Gallery']")
    BUTTON_VOID_CURRENT_ORDER = (By.ID, locator_url + "navVoidCurrentOrder")
    BUTTON_OPEN_ORDERS = (By.ID, locator_url + "navOrders")
    BUTTON_POSTIVE = (By.ID, locator_url + "btnPositive")
    BUTTON_ITEM_ADDED_VIEWER = (By.ID, locator_url + "vBottomTotal")
    BUTTON_OPEN_MORE = (By.XPATH, "//android.widget.LinearLayout[@content-desc='Navigation view']/android.view.ViewGroup/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView")
    BUTTON_COLOR = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[5]/android.widget.ImageView")

    BUTTON_KEY_1 = (By.ID, locator_url + "btnKey1")
    BUTTON_KEY_2 = (By.ID, locator_url + "btnKey2")
    BUTTON_KEY_3 = (By.ID, locator_url + "btnKey3")
    BUTTON_KEY_ENTER = (By.ID, locator_url + "btnEnter")
    BUTTON_OPEN_ITEM_MENU = (By.ID, locator_url + "btnAddItem")


    INPUT_Quantity = (By.ID, locator_url + "etQuantity")
    INPUT_MANUAL_ITEM = (By.ID, locator_url + "etAmount")


    TV_QANTITY = (By.ID, locator_url + "tvQuantity")
    TV_AMOUNT = (By.ID, locator_url + "tvAmount")
    TV_TOTAL = (By.ID, locator_url + "tvTotal")

    SWITCH_VARIABLE_PRICE = (By.ID, locator_url + "switchVariablePrice")
    SWITCH_FAVORITE = (By.ID, locator_url + "switchFavorite")


class InventoryPageLocators(object):
    BUTTON_CATEGORIES = (By.CSS_SELECTOR, "[content-desc='Form.Departments.Value']")

class MoreOptionPageLocators(object):
    BUTTON_CONSUMER = (By.ID, locator_url + "navConsumers")
    BUTTON_CLEAR_CONSUMER = (By.CSS_SELECTOR, "[content-desc='OperationButtons.ClearConsumer']")

    INPUT_NOTE = (By.ID, locator_url + "etComment")

