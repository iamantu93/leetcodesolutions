class BrowserHistory:
# https://leetcode.com/problems/design-browser-history/
    def __init__(self, homepage):
        self.history = []
        self.future = []
        self.history.append(homepage)

    def visit(self, url):
        self.history.append(url)
        self.future = []

    def back(self, steps):
        while steps > 0 and len(self.history) > 1:
            self.future.append(self.history[-1])
            self.history.pop()
            steps -= 1
        return self.history[-1]

    def forward(self, steps):
        while steps > 0 and self.future:
            self.history.append(self.future[-1])
            self.future.pop()
            steps -= 1
        return self.history[-1]
