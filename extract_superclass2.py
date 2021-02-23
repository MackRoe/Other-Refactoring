# Starter Code by Kami Bigdely
# Goal: Extract superclass.
# Refactor by Laine (Music)

# Superclass: Shape
#   Attributes: x, y, visible
#   Methods: toggle_visible()
#            display_shape()


class Circle:
    
    def __init__(self, x, y, r, visible = True):
      # Should the value of the visible variable be set in the arguments?
      self.center_x = x
      self.center_y = y
      self.r = r  # Unclear variable naming
      self.visible = visible

      
    def display(self):
        print('drew the circle.')
        
    def set_visible(self,is_visible):
        self.visible = is_visible
        # Seems redundent. Why are we re-assigning this?
        
    def get_center(self):
        return self.center_x, self.center_y
    
    
class Rectangle:
    
    def __init__(self, x, y, width, height, visible = True):
        ''' Returns the coordinates of the left-bottom corner. ''' 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible
        
    def display(self):
        if self.visible:
            print('drew the rectable.')
            
    def hide(self):
        self.visible = False
        
    def make_visible(self):
        self.visible = True
        # redundant
        
    def get_center(self):
        return self.x + self.width/2, \
               self.y + self.height/2 



if __name__ == "__main__":
    circle = Circle(0,0,10, False)
    circle.set_visible(True)
    circle.display()
    print('center point: ', circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.hide()
    rect.display()  # does not display because it's hidden.
    rect.make_visible()
    rect.display()
    print('center point: ', rect.get_center())
