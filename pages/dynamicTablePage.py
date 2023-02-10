class dynamicTablePage:


    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://qaplayground.dev/apps/dynamic-table/")

    def get_superhero_information(self, superhero):
        """
        Return a dictionary with all the informations of the superhero provided
        """
        values = {}

        row = self.page.locator("table.mx-auto tr")
        superhero = row.locator(":scope", has_text = superhero)
        data = superhero.locator("td")
        # Getting all the values
        values["superhero"] = superhero
        values["email"] = (data.nth(0).all_inner_texts())[0].split('\n')[1]
        values["status"] = data.nth(1).inner_text()
        values["real_name"] = data.nth(2).inner_text()

        return values

        