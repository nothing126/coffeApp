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
import sqlite3

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
        self.size_hint_y = 8

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
        self.spacing = '15dp'
        self.padding = '8dp'
        self.size_hint_y = None
        self.height = '170dp'
        self.image = AsyncImage(source=image_source, allow_stretch=True, keep_ratio=False)
        self.add_widget(self.image)
        self.bind(size=self.update_size)

    def update_size(self, *args):
        self.image.size = self.size


class ActionsContent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.anchor_x = 'center'
        self.anchor_y = 'center'

        image_sources = [
            "path_to_image_1.jpg",
            "path_to_image_2.jpg",
            "path_to_image_3.jpg"
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

        screen = MDScreen()
        screen.md_bg_color = [1, 1, 1, 1]

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

        button_layout = BoxLayout(orientation='vertical', spacing='10dp', size_hint=(None, None), size=(300, 200),
                                  pos_hint={"center_x": 0.5, "center_y": 0.5})

        button_login = MDFlatButton(
            text="Вход",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5},
            on_release=self.show_dialog
        )
        button_register = MDFlatButton(
            text="Регистрация",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5},
            on_release=self.show_dialog
        )

        button_layout.add_widget(button_login)
        button_layout.add_widget(button_register)

        center_layout.add_widget(button_layout)

        tab4.add_widget(center_layout)

        bottom_navigation.add_widget(tab1)
        bottom_navigation.add_widget(tab2)
        bottom_navigation.add_widget(tab3)
        bottom_navigation.add_widget(tab4)

        screen.add_widget(bottom_navigation)

        return screen

    def show_dialog(self, obj):
        self.dialog = MDDialog(
            title="вход",
            type="custom",
            content_cls=LoginContent() if obj.text == "Вход" else RegistrationContent(),
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                ),
                MDRaisedButton(
                    text="REGISTER" if obj.text == "Регистрация" else "LOGIN",
                    on_release=self.login_button_pressed if obj.text == "Вход" else self.register_button_pressed
                ),
            ],
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def login_button_pressed(self, obj):
        login_text = self.dialog.content_cls.login_field.text
        password_text = self.dialog.content_cls.password_field.text

    def register_button_pressed(self, obj):
        # Code for handling register button pressed
        name_text = self.dialog.content_cls.name_field.text
        email_text = self.dialog.content_cls.email_field.text
        login_text = self.dialog.content_cls.login_field.text
        password_text = self.dialog.content_cls.password_field.text

        # Open connection to the database
        self.conn = sqlite3.connect("registration.db")
        self.cursor = self.conn.cursor()

        # Insert registration data into the table
        self.cursor.execute(
            "INSERT INTO registration_data (name, email, login, password) VALUES (?, ?, ?, ?)",
            (name_text, email_text, login_text, password_text)
        )

        # Commit changes and close the connection
        self.conn.commit()
        self.conn.close()

        self.dialog.dismiss()
        self.show_success_dialog()

    def show_success_dialog(self):
        success_dialog = MDDialog(
            title="Success",
            text="Registration successful!",
            buttons=[
                MDFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color, on_release=self.close_success_dialog
                ),
            ],
        )
        success_dialog.open()

    def close_success_dialog(self, obj):
        self.dialog.dismiss()

    def show_error_dialog(self):
        error_dialog = MDDialog(
            title="Error",
            text="неверное имя пользователя или пароль!",
            buttons=[
                MDFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color, on_release=self.close_error_dialog
                ),
            ],
        )
        error_dialog.open()

    def close_error_dialog(self, obj):
        self.dialog.dismiss()


if __name__ == '__main__':
    Test().run()
