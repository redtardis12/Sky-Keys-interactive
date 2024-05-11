import flet
from flet import AppBar
from flet import Card
from flet import Column
from flet import Container
from flet import Icon
from flet import IconButton
from flet import NavigationRail
from flet import NavigationRailDestination
from flet import Page
from flet import Row
from flet import Stack
from flet import Text
from flet import UserControl
from flet import VerticalDivider
from flet import colors
from flet import icons


class ResponsiveMenuLayout(Row):
    def __init__(self, page, pages, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.expand = True
        self.page = page
        self.pages = pages

        navigation_items = [navigation_item for navigation_item, _ in pages]
        self.navigation_rail = self._build_navigation_rail(navigation_items)

        page_contents = [page_content for _, page_content in pages]

        self.menu_panel = Row(
            controls=[self.navigation_rail, VerticalDivider(width=1)],
            spacing=0,
        )
        self.content_area = Column(page_contents, expand=True)

        self._was_portrait = self.is_portrait()
        self._panel_visible = self.is_landscape()

        self.set_navigation_content()
        self._change_displayed_page()

        self.page.on_resize = self.handle_resize

    def select_page(self, page_number):
        self.navigation_rail.selected_index = page_number
        self._change_displayed_page()

    def _navigation_change(self, e):
        self._change_displayed_page()

    def _change_displayed_page(self):
        selected_index = self.navigation_rail.selected_index
        # page_contents = [page_content for _, page_content in self.pages]
        for i, content_page in enumerate(self.content_area.controls):
            content_page.visible = selected_index == i

        self.check_toggle_on_select()

        self.page.update()

    def _build_navigation_rail(self, navigation_items):
        return NavigationRail(
            selected_index=0,
            label_type="all",
            #extended=True,
            destinations=navigation_items,
            on_change=self._navigation_change,
        )

    def handle_resize(self, e):
        if self._was_portrait != self.is_portrait():
            self._was_portrait = self.is_portrait()
            self._panel_visible = self.is_landscape()
            self.set_navigation_content()
            self.page.update()

    def toggle_navigation(self):
        self._panel_visible = not self._panel_visible
        self.set_navigation_content()
        self.page.update()

    def check_toggle_on_select(self):
        if self.is_portrait() and self._panel_visible:
            self.toggle_navigation()

    def set_navigation_content(self):
        if self.is_landscape():
            self.add_landscape_content()
        else:
            self.add_portrait_content()

    def add_landscape_content(self):
        self.controls = [self.menu_panel, self.content_area]
        self.menu_panel.visible = self._panel_visible

    def add_portrait_content(self):
        self.controls = [Stack(controls=[self.content_area, self.menu_panel], expand=True)]
        self.menu_panel.visible = self._panel_visible

    def is_portrait(self) -> bool:
        # Return true if window/display is narrow
        return self.page.window_height >= self.page.window_width

    def is_landscape(self) -> bool:
        # Return true if window/display is wide
        return self.page.window_width > self.page.window_height