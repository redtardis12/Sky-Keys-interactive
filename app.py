import os
import json
import shutil
import threading
import flet as ft
from flet import Image, GridView, Container, NavigationRailDestination, Page, Text, IconButton, AppBar, colors, icons
from reactive_menu import ResponsiveMenuLayout
from music.automusic import mstart
import multiprocessing


def main(page: Page, title="Sky: Keys interactive"):

    page.title = title

    menu_button = IconButton(icons.MENU)

    global music_proc
    music_proc = None


    def copy_music(e):
        destination_folder = "music/songs/"

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        if e.files is None:
            return

        for file in e.files:
            new_file_path = os.path.join(destination_folder, file.name)
            try:
                shutil.copy(file.path, new_file_path)
            except Exception as err:
                print(f"Error copying {file.path}: {err}")

            song = ft.Radio(value=new_file_path, label=file.name.replace(".txt", ""))
            page.controls[0].controls[1].controls[1].content.content.controls.append(song)
        page.update()
       

    def music_hotkeys(e):
        global music_proc
        if not music_proc:
            f = "music/songs/" + page.controls[0].controls[1].controls[1].content.value
            music_proc = multiprocessing.Process(target=mstart, args=(f,))
            music_proc.start()
            e.control.icon = icons.PAUSE
            print("Started music")
        else:
            music_proc.terminate()
            music_proc.join()
            music_proc = None
            e.control.icon = icons.PLAY_ARROW
            print("Stopped music")
        page.update()


    def music_page():
        music_view =ft.Column(scroll=True, expand=True)
        fp = ft.FilePicker(on_result=copy_music)
        add_btn = IconButton(icon=icons.ADD, content=Text("Add music"), on_click=lambda e: fp.pick_files(allow_multiple=True, allowed_extensions=['txt', 'json']))
        music_view.controls.append(fp)
        music_view.controls.append(add_btn)
        for midi_file in os.listdir("music/songs/"):
            if midi_file.endswith(".txt"):
                song = ft.Radio(value=midi_file, label=midi_file.replace(".txt", ""))
                music_view.controls.append(song)

        return ft.Container(content=ft.RadioGroup(content=music_view), expand=True)


    def emotes_page():
        grid_view = GridView(
            runs_count=5,
            max_extent=100,
            child_aspect_ratio=1,
            spacing=10,
            expand=True,
        )
        for img_file in os.listdir("emotes/assets/pngs"):
            if img_file.endswith(".png"):
                img = Container(
                    image_src=f"emotes/assets/pngs/{img_file}",
                    width=50,
                    height=50,
                    ink=True,
                    on_click=lambda e, label=img_file: open_dlg_modal(e, label),
                )
                grid_view.controls.append(img)

        return grid_view

    def close_dlg(e, label):
        page.dialog.open = False
        print(label + " saved!")
        page.update()
    
    def open_dlg_modal(e, label):
        dlg_modal = ft.AlertDialog(
            title=ft.Text(label),
            modal=True,
            content=ft.Column([ft.Text("Input rows offset:"),
                            ft.Slider(min=0, max=100, divisions=10, label="{value}%"),
                            ft.Text("Bind a hotkey"),
                            ft.Text("Ctrl+Shift+X")]),
            actions=[
                ft.TextButton("Save", on_click=lambda e, label=label: close_dlg(e, label)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )


        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()


    page.window_width = 800
    page.window_height = 600
    page.appbar = AppBar(
        leading=menu_button,
        leading_width=40,
        title=Text(title),
        bgcolor=colors.DEEP_PURPLE_900,
    )

    pages = [
        (
            NavigationRailDestination(
                icon=icons.FAVORITE_BORDER,
                selected_icon=icons.FAVORITE,
                label="Emotes",
            ),
            emotes_page(),
        ),
        (
            NavigationRailDestination(
                icon=icons.LIBRARY_MUSIC_OUTLINED,
                selected_icon=icons.LIBRARY_MUSIC_ROUNDED,
                label="Music",
            ),
            music_page(),
        ),
    ]

    menu_layout = ResponsiveMenuLayout(page, pages)

    play_btn = IconButton(icon=icons.PLAY_ARROW, on_click=lambda e: music_hotkeys(e))



    page.add(menu_layout)
    page.add(play_btn)

    menu_button.on_click = lambda e: menu_layout.toggle_navigation()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    ft.app(target=main, assets_dir="emotes/assets")