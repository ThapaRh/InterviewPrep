'''
Add behaviors to objects dynamically without modifying the class
Analogy:
Shirt->add sweater->add jacket
Each adds function but doesnot change the base "you"
'''

class Text:
    def render(self):
        return "Test text."

class BoldDecorator(Text):
    def __init__(self,wrapped):
        self.wrapped = wrapped
    
    def render(self):
        return f"<b>{self.wrapped.render()}</b>"

class ItalicDecorator(Text):
    def __init__(self,wrapped):
        self.wrapped = wrapped
    
    def render(self):
        return f"<i>{self.wrapped.render()}</i>"
    
text = Text()
decorated = BoldDecorator(ItalicDecorator(text))
print(decorated.render())