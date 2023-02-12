class multilevelDropdownpage:


    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://qaplayground.dev/apps/multi-level-dropdown")

