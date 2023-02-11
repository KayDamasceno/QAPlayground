class tagsPage:


    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://qaplayground.dev/apps/tags-input-box/")

    def clean_tags(self):

        while self.page.locator("[class='uit uit-multiply']").count() > 0:

            tags = self.page.locator("[class='uit uit-multiply']")
            
            
            tags.nth(0).click()
    
    def add_tag(self, text):

        self.page.locator("[type='text']").type(text)
        self.page.keyboard.press("Enter")
