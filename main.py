from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window

Builder.load_string("""
<ImageRectangle>:
    canvas.before:
        Color:
            rgba: 0.8, 0.8, 0.8, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [28]
""")


class LoginContent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None

        self.login_field = MDTextField(
            hint_text="Login",
            helper_text_mode="on_focus",
            pos_hint={"center_x": 0.5},
        )
        self.add_widget(self.login_field)

        self.password_field = MDTextField(
            hint_text="Password",
            helper_text_mode="on_focus",
            pos_hint={"center_x": 0.5},
        )
        self.add_widget(self.password_field)


class RegistrationContent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None

        self.name_field = MDTextField(
            hint_text="Name",
            helper_text_mode="on_focus",
            pos_hint={"center_x": 0.3},
        )
        self.add_widget(self.name_field)

        self.email_field = MDTextField(
            hint_text="Email",
            helper_text_mode="on_focus",
            pos_hint={"center_x": 0.3},
        )
        self.add_widget(self.email_field)

        self.login_field = MDTextField(
            hint_text="Login",
            helper_text_mode="on_focus",
            pos_hint={"center_x": 0.3},
        )
        self.add_widget(self.login_field)

        self.password_field = MDTextField(
            hint_text="Password",
            helper_text_mode="on_focus",
            pos_hint={"center_x": 0.3},
        )
        self.add_widget(self.password_field)


class MenuContent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        image_source = r'C:\Users\ajiga\PycharmProjects\coffeApp\foto\изображение_viber_2023-06-15_16-05-49-076.jpg'
        image = AsyncImage(source=image_source, allow_stretch=True, keep_ratio=False)
        self.add_widget(image)


class ImageRectangle(BoxLayout):
    def __init__(self, image_source, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = '20dp'
        self.padding = '20dp'
        self.size_hint_y = None

        self.image = AsyncImage(source=image_source, allow_stretch=True, keep_ratio=False)
        self.add_widget(self.image)
        self.bind(size=self.update_size)

    def update_size(self, *args):
        self.image.size = self.size


class ActionsContent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = '20dp'
        self.padding = '20dp'

        # Здесь указывайте шаблон пути для каждого прямоугольника
        image_sources = [
            'path_to_image_1.jpg',
            'path_to_image_2.jpg',
            'path_to_image_3.jpg'
        ]

        # Создаем экземпляры ImageRectangle для каждого пути к изображению
        for source in image_sources:
            self.add_widget(ImageRectangle(image_source=source))

        self.size_hint_y = None
        self.height = Window.height * 0.8  # Adjust the height as needed
        self.pos_hint = {'top': 1}  # Move the content to the top of the screen


def anonymous_button_pressed():
    # Handle anonymous button functionality here
    print("Anonymous button pressed")


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.dialog = None

    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.theme_style = "Dark"
        self.dialog = None

        screen = MDScreen()
        screen.md_bg_color = [1, 1, 1, 1]  # Set the background color to white

        bottom_navigation = MDBottomNavigation()

        tab1 = MDBottomNavigationItem(
            name='screen 1',
            text='акции',
            badge_icon="numeric-10"
        )
        tab1.add_widget(ActionsContent())
        tab2 = MDBottomNavigationItem(
            name='screen 2',
            text='меню',
            badge_icon="numeric-10",
        )
        tab2.add_widget(MenuContent())
        tab3 = MDBottomNavigationItem(
            name='screen 3',
            text='о нас',
            badge_icon="numeric-10"
        )
        tab4 = MDBottomNavigationItem(
            name='screen 4',
            text='главная',
            badge_icon="numeric-10"
        )

        center_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        button_layout = BoxLayout(orientation='horizontal', spacing='10dp')

        button_login = MDRaisedButton(
            text="Вход",
            on_release=self.show_dialog,
        )
        button_login.custom_type = "login"

        button_register = MDRaisedButton(
            text="Регистрация",
            on_release=self.show_dialog,
        )
        button_register.custom_type = "registration"

        button_layout.add_widget(button_login)
        button_layout.add_widget(button_register)

        center_box = BoxLayout(orientation='vertical', size_hint=(None, None), size=(200, 150),
                               pos_hint={'center_x': 0.5, 'center_y': 0.5})
        center_box.add_widget(button_layout)

        button_anonymous = MDRaisedButton(
            text="Анонимное посещение",
            on_release=anonymous_button_pressed
        )

        center_box.add_widget(button_anonymous)

        center_layout.add_widget(center_box)

        tab4.add_widget(center_layout)

        bottom_navigation.add_widget(tab1)
        bottom_navigation.add_widget(tab2)
        bottom_navigation.add_widget(tab3)
        bottom_navigation.add_widget(tab4)

        screen.add_widget(bottom_navigation)
        return screen

    def show_dialog(self, button):
        global buttons, title, content
        if button.custom_type == "login":
            content = LoginContent()
            title = "Login"
            buttons = [
                MDFlatButton(
                    text="CANCEL",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog,
                ),
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.login_button_pressed,
                ),
            ]
        elif button.custom_type == "registration":
            content = RegistrationContent()
            title = "Registration"
            buttons = [
                MDFlatButton(
                    text="CANCEL",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog,
                ),
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.register_button_pressed,
                ),
            ]

        self.dialog = MDDialog(
            title=title,
            type="custom",
            content_cls=content,
            buttons=buttons,
            auto_dismiss=False,
        )
        self.dialog.open()

    def close_dialog(self):
        self.dialog.dismiss()

    def login_button_pressed(self, *args):
        if args and args[0].text == "OK":
            login = self.dialog.content_cls.login_field.text
            password = self.dialog.content_cls.password_field.text
            print(f"Login: {login}, Password: {password}")
        self.close_dialog()

    def register_button_pressed(self, *args):
        if args and args[0].text == "OK":
            name = self.dialog.content_cls.name_field.text
            email = self.dialog.content_cls.email_field.text
            login = self.dialog.content_cls.login_field.text
            password = self.dialog.content_cls.password_field.text
            print(f"Name: {name}, Email: {email}, Login: {login}, Password: {password}")
        self.close_dialog()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.maximize()
        self.theme_cls.material_style = "M2"
        self.theme_cls.theme_style = "Dark"
        self.dialog = None


Test().run()
