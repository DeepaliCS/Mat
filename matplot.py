


class BarCharts:   
  
    def __init__(self, title, x_label, y_labels):   
        self.title = title
        self.x_label = x_label
        self.y_labels = y_labels  
      
    # Sample Method    
    def bar_subplot(self):

        import matplotlib.pyplot as plt
        import numpy as np

        np.random.seed(19680801)
    
        plt.rcdefaults()
        fig, ax = plt.subplots()

        # Example data
        y_pos = np.arange(len(y_labels))

        performance = 3 + 10 * np.random.rand(len(y_labels))
        error = np.random.rand(len(y_labels))

        ax.barh(y_pos, performance, xerr=error, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(y_labels)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel(x_label)
        ax.set_title(title)
        plt.show() 
      
title = 'How fast do you want to go today?'
x_label = 'Performance'
y_labels = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
p = BarCharts(title, x_label, y_labels)   
p.bar_subplot()   

