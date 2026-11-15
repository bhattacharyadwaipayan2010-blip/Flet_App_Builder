import flet as ft

def main(page: ft.Page):
    page.title = "My First App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    name_input = ft.TextField(label="Enter your name", width=250)
    greeting = ft.Text(size=20, weight=ft.FontWeight.BOLD)

    def say_hello(e):
        greeting.value = f"Hello, {name_input.value or 'Friend'}! Your app works!"
        page.update()

    page.add(
        name_input,
        ft.ElevatedButton("Click Me", on_click=say_hello),
        greeting
    )

ft.app(target=main)
  
