from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDRectangleFlatButton
from kivy.metrics import dp


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.hue = "500"
        self.theme_cls.theme_style = "Dark"
        button = MDRectangleFlatButton(text='back',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.1})
        screen = Screen()
        table = MDDataTable(pos_hint={'center_x':0.5, 'center_y':0.5},
                                size_hint=(0.9,0.6),
                                rows_num = 999,
                                    column_data=[
                                        ('Player', dp(15)), #controls space inbetween columns
                                        ('Wins', dp(15)),
                                        ('Losses', dp(15)),
                                        ('Draw', dp(15))
                                    ],
                                    row_data=[
                                        ('Stephen', "8", '6', '2'),
                                        ('Ian', "9", '3', '12'),
                                        ('Jackson', "3", '10', '6'),
                                        ('Austin', "0", '30', '2'),
                                        ('Stephen', "8", '6', '2'),
                                        ('Ian', "9", '3', '12'),
                                        ('Jackson', "3", '10', '6'),
                                        ('Austin', "0", '30', '2'),
                                        ('Stephen', "8", '6', '2'),
                                        ('Ian', "9", '3', '12'),
                                        ('Jackson', "3", '10', '6'),
                                        ('Austin', "0", '30', '2'),
                                        ('Jackson', "3", '10', '6'),
                                        ('Austin', "0", '30', '2'),
                                        ('Stephen', "8", '6', '2'),
                                        ('Ian', "9", '3', '12'),
                                        ('Jackson', "3", '10', '6'),
                                        ('Austin', "0", '30', '2'),
                                        ('Jackson', "3", '10', '6'),
                                        ('Austin', "0", '30', '2'),
                                        ('Stephen', "8", '6', '2'),
                                        ('Ian', "9", '3', '12'),
                                        ('Jackson', "3", '10', '6'),
                                        ('Austin', "0", '30', '2'),
                                    ],
                            )
        table.bind(on_row_press=self.row_press)
        screen.add_widget(table)
        screen.add_widget(button)
        return screen

    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)


DemoApp().run()
