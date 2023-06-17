from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
# import sqlite3
from kivymd.uix.card import MDCard

# для класса ImageRectangle для определения закругления, цвета, размера и позиции
Builder.load_string("""
<ImageRectangle>:
    canvas.before:
        Color:
            rgba: 0.8, 0.8, 0.8, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15]
""")


class LoginContent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None

        # определяет поле для логина при входе
        self.login_field = MDTextField(
            hint_text="Login",
            helper_text_mode="on_focus",
            pos_hint={"center_x": 0.5},
        )
        # добавляет виджет с полем для логина
        self.add_widget(self.login_field)

        # определяет поле для пароля при входе
        self.password_field = MDTextField(
            hint_text="Password",
            helper_text_mode="on_focus",
            pos_hint={"center_x": 0.5},
        )
        # добавляет виджет с полем для пароля
        self.add_widget(self.password_field)


class RegistrationContent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None

        # определяет поле для имени при регистрации
        self.name_field = MDTextField(
            hint_text="Name",
            helper_text_mode="on_focus",
            pos_hint={"center_x": 0.5},
        )
        # добавляет виджет с полем для имени
        self.add_widget(self.name_field)

        # определяет поле для почты при регистрации
        self.email_field = MDTextField(
            hint_text="Email",
            helper_text_mode="on_focus",
            pos_hint={"center_x": 0.5},
        )
        # добавляет виджет с полем для почты
        self.add_widget(self.email_field)

        # определяет поле для логина при регистрации
        self.login_field = MDTextField(
            hint_text="Login",
            helper_text_mode="on_focus",
            pos_hint={"center_x": 0.5},
        )
        # добавляет виджет с полем для логина
        self.add_widget(self.login_field)

        # определяет поле для пароля при регистрации
        self.password_field = MDTextField(
            hint_text="Password",
            helper_text_mode="on_focus",
            pos_hint={"center_x": 0.5},
        )
        # добавляет виджет с полем для пароля
        self.add_widget(self.password_field)


class MenuContent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # добавляет скролинг в окне с меню
        scroll_view = ScrollView(do_scroll_x=False, do_scroll_y=True, effect_cls="ScrollEffect")
        # добавляет в виджет скролинга виджет с карктикой, обращается к классу
        # ImageRectangle для создания поля в виде прямоугольника с скргуленными унлами
        scroll_view.add_widget(ImageRectangle(image_source=r'C:\Users\ajiga\PycharmProjects\coffeApp\foto'
                                                           r'\изображение_viber_2023-06-15_16-05-49-076.jpg', ))
        self.add_widget(scroll_view)


class ImageRectangle(BoxLayout):
    def __init__(self, image_source, **kwargs):
        super().__init__(**kwargs)
        # определяет ориентацию
        self.orientation = 'vertical'
        # определяет промежуток между окнами прямоугольников
        self.spacing = '15dp'
        # определяет обводку окон прямоугольников
        self.padding = '8dp'
        self.size_hint_y = None
        # определяет высоту прямоугольников
        self.height = '900dp'
        # позволяет картике растягиваться
        self.image = AsyncImage(source=image_source, allow_stretch=True, keep_ratio=False)
        self.add_widget(self.image)
        self.bind(size=self.update_size)

    def update_size(self, *args):
        self.image.size = self.size


class ActionsContent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # определяет положение по центру и вертикальную ориентацию
        self.orientation = 'vertical'
        self.anchor_x = 'center'
        self.anchor_y = 'center'

        # пути к картинкам, строго в пронумерованом порядке по строкам
        image_sources = [
            'path_to_image',
            'path_to_image',
            "path_to_image",
        ]

        scroll_view = ScrollView(do_scroll_x=False, do_scroll_y=True, effect_cls="ScrollEffect")
        grid_layout = GridLayout(cols=1, spacing='20dp', size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))
        for source in image_sources:
            grid_layout.add_widget(ImageRectangle(image_source=source))
        scroll_view.add_widget(grid_layout)

        self.add_widget(scroll_view)


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None

    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.theme_style = "Dark"
        self.dialog = None
        # определяет переменную screen как экран приложения
        screen = MDScreen()

        screen.md_bg_color = [0, 0, 0, 1]

        bottom_navigation = MDBottomNavigation()

        # иконка нижнего управления для вкладки "акции"
        tab1 = MDBottomNavigationItem(
            name='screen 1',
            text='акции',
            badge_icon="numeric-10"
        )
        # добавляет в вкладку "акции" класс содержащий акции
        tab1.add_widget(ActionsContent())

        # иконка нижнего управления для вкладки "меню"
        tab2 = MDBottomNavigationItem(
            name='screen 2',
            text='меню',
            badge_icon="numeric-10",
        )

        # добавляет в вкладку "меню" класс содержащий меню
        tab2.add_widget(MenuContent())

        # иконка нижнего управления для вкладки "о нас"
        tab3 = MDBottomNavigationItem(
            name='screen 3',
            text='о нас',
            badge_icon="numeric-10"
        )
        # иконка нижнего управления для вкладки "главная"
        tab4 = MDBottomNavigationItem(
            name='screen 4',
            text='главная',
            badge_icon="numeric-10"
        )

        center_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        button_layout = BoxLayout(orientation='vertical', spacing='10dp', size=(500, 350), )

        button_layout.size_hint = (None, None)
        button_layout.height = "200dp"
        # устанавливает размеры кнопки и цвет фона
        card_login = MDCard(
            size_hint=(None, None),
            size=(65, 35),
            pos_hint={"center_x": 0.5},
            radius=[15, 15, 15, 15],
            md_bg_color=self.theme_cls.primary_color
        )
        # устанавливвет текст кнопки и функцию при ее нажатии
        button_login = MDFlatButton(
            text="Вход",
            on_release=self.show_login_dialog
        )
        # добавляет виджет с текстом и функцией на поле для кнопки
        card_login.add_widget(button_login)
        # добавляет ранее сохранненый виджет на место для кнопки
        button_layout.add_widget(card_login)

        # устанавливает размеры кнопки и цвет фона
        card_register = MDCard(
            size_hint=(None, None),
            size=(100, 38),
            pos_hint={"center_x": 0.5},
            radius=[15, 15, 15, 15],
            md_bg_color=self.theme_cls.primary_color
        )
        # устанавливвет текст кнопки и функцию при ее нажатии
        button_register = MDFlatButton(
            text="Регистрация",
            on_release=self.show_registration_dialog
        )
        card_register.add_widget(button_register)
        button_layout.add_widget(card_register)

        center_layout.add_widget(button_layout)

        tab4.add_widget(center_layout)
        # добавляет в нижнюю панель управления элементы
        bottom_navigation.add_widget(tab1)
        bottom_navigation.add_widget(tab2)
        bottom_navigation.add_widget(tab3)
        bottom_navigation.add_widget(tab4)
        # добавляет на экран нижнюю панель управления
        screen.add_widget(bottom_navigation)

        return screen

    def show_login_dialog(self, obj):
        # показывает диалог входа с кнопками
        self.dialog = MDDialog(
            title="Вход",
            type="custom",
            content_cls=LoginContent(),
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                ),
                MDRaisedButton(
                    text="LOGIN",
                    on_release=self.login_button_pressed
                ),
            ],
            # устанавливает размеры и цвет фона
            size=(400, 200),
            size_hint=(None, None),
            md_bg_color=self.theme_cls.bg_dark
        )
        self.dialog.open()

    def show_registration_dialog(self, obj):
        # показывает диалог регистрации с кнопками
        self.dialog = MDDialog(
            title="Регистрация",
            type="custom",
            content_cls=RegistrationContent(),
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                ),
                MDRaisedButton(
                    text="REGISTER",
                    on_release=self.register_button_pressed
                ),
            ],
            # устанавливает размер окна диалога и цвет фона
            size=(500, 350),
            size_hint=(None, None),
            md_bg_color=self.theme_cls.bg_dark
        )
        self.dialog.open()

    def close_dialog(self, obj):
        # закрывает диалог
        self.dialog.dismiss()

    def close_success_dialog(self, obj):
        # закрывает диалог успешной регистрации
        self.success_dialog.dismiss()

    def login_button_pressed(self, obj):
        # сохраняет введенные данные входа и выводит их в консоль
        login_text = self.dialog.content_cls.login_field.text
        password_text = self.dialog.content_cls.password_field.text
        print(f"login:{login_text},password:{password_text}")

    def register_button_pressed(self, obj):
        # сохраняет все введённые данные в переменные
        name_text = self.dialog.content_cls.name_field.text
        email_text = self.dialog.content_cls.email_field.text
        login_text = self.dialog.content_cls.login_field.text
        password_text = self.dialog.content_cls.password_field.text

        # указание файла для базы данных
        # self.conn = sqlite3.connect("registration.db")
        # # создание курсора
        # self.cursor = self.conn.cursor()
        #
        # # проверка почты для проверки регистрации
        # self.cursor.execute("SELECT * FROM registration_data WHERE email = ?", (email_text,))
        # existing_user = self.cursor.fetchone()
        #
        # if existing_user:
        #     self.show_error_dialog("Пользователь с такой почтой уже зарегистрирован!")
        # else:
        #     # если пользователя с такой почтой нет, то записывает его в таблицу
        #     self.cursor.execute("INSERT INTO registration_data (name, email, login, password) VALUES (?, ?, ?, ?)",
        #                         (name_text, email_text, login_text, password_text))
        #     self.conn.commit()
        #     self.show_success_dialog("Регистрация прошла успешно!")
        #     self.dialog.dismiss()  # Close the registration dialog
        #
        # # закрытие базы данных и курсора
        # self.cursor.close()
        # self.conn.close()

    def show_error_dialog(self, message):
        # показывает диалог ошибки
        self.error_dialog = MDDialog(
            title="Ошибка",
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color, on_release=self.close_error_dialog
                ),
            ],
        )
        self.error_dialog.open()

    def close_error_dialog(self, obj):
        # закрывает диалог ошибки
        self.error_dialog.dismiss()

    def show_success_dialog(self, message):
        # показывает диалог успешного выполнения
        self.success_dialog = MDDialog(
            title="Успех",
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color, on_release=self.close_success_dialog
                ),
            ],
        )
        self.success_dialog.open()


# запускает главный класс test
Test().run()
