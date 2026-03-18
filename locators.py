from selenium.webdriver.common.by import By

# Главная страница
MAIN_PAGE_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка входа на главной
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Кнопка перехода в личный кабинет
CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка перехода в конструктор
LOGO = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]")  # Логотип Stellar Burgers
PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # Кнопка оформления заказа

# Разделы конструктора
BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']/parent::div")  # Раздел «Булки»
SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']/parent::div")  # Раздел «Соусы»
FILLINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']/parent::div")  # Раздел «Начинки»
ACTIVE_SECTION = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]")  # Активный раздел

# Страница регистрации - ПРАВИЛЬНЫЕ ЛОКАТОРЫ
REGISTER_NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")  # Поле Имя
REGISTER_EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # Поле Email
REGISTER_PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")  # Поле Пароль
REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка регистрации
LOGIN_LINK_FROM_REGISTER = (By.XPATH, ".//a[text()='Войти']")  # Ссылка на вход
ERROR_MESSAGE = (By.XPATH, ".//p[contains(@class, 'input__error')]")  # Сообщение об ошибке

# Страница входа
LOGIN_EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # Поле Email
LOGIN_PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")  # Поле Пароль
LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка «Войти»
REGISTER_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")  # Ссылка на регистрацию
RESTORE_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")  # Ссылка восстановления

# Страница профиля
PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль']")  # Ссылка «Профиль»
LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка «Выход»