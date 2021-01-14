#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib


# In[2]:


import matplotlib
matplotlib.__version__


# In[5]:


import matplotlib.pyplot as plt


# In[8]:


import numpy as np


# In[9]:


X = np.array([1, 2, 5, 8, 12])
Y = np.array([3, 6, 7, 12, 9])


# In[10]:


import matplotlib.pyplot as plt


# In[11]:


plt.plot(X, Y)


# In[12]:


plt.show()


# In[18]:


import numpy as np

X = np.array([1, 2, 5, 8, 12])
Y = np.array([3, 6, 7, 12, 9])

import matplotlib.pyplot as plt
plt.plot(X, Y)
plt.title("This is the title")


# In[19]:


plt.xlabel("X label")
plt.ylabel("Y label")


# In[20]:


plt.show()


# In[29]:


import matplotlib.pyplot as plt


# In[30]:


subjects = ["Maths", "Biology", "Chemistry", "Physics", "English", "Computers"]
marks = [97, 68, 59, 81, 77, 92]


# In[31]:


plt.bar(subjects, marks, color='blue')


# In[32]:


plt.title("Bar Graph Example")
plt.xlabel("Subjects")
plt.ylabel("Marks")


# In[33]:


plt.show()


# In[4]:


import matplotlib.pyplot as plt
import numpy as np


# In[5]:


subjects = ["Maths", "Biology", "Chemistry", "Physics", "English", "Computers"]
student1 = [97, 68, 59, 81, 77, 92]
student2 = [88, 61, 80, 40, 62, 52]
student3 = [54, 62, 77, 54, 71, 98]


# In[6]:


index = np.arange(6)
width = 0.03


# In[8]:


plt.barh(index, student1, width, color="aqua", label="Student 1")
plt.barh(index + width, student2, width, color="green", label="Student 2")
plt.barh(index + (width*2), student3, width, color="blue", label="Student 3")
plt.title(index, student1, width, color="aqua", label="Student 1")
plt.xlabel(index + width, student2, width, color="green", label="Student 2")
plt.ylabel(index + (width*2), student3, width, color="blue", label="Student 3")
plt.xticks(index + width/2, subjects)
plt.legend()
plt.show()


# In[13]:


import matplotlib.pyplot as plt


# In[14]:


firms = ["Firm A", "Firm B", "Firm C", "Firm D", "Firm E"]
market_shares = [10, 40, 30, 5, 15]


# In[15]:


Explode = [0, 0, 0, 0.5, 0]


# In[16]:


plt.pie(market_shares, explode=Explode, labels=firms, shadow=True, startangle=45)
plt.axis('equal')
plt.legend(title = "List of Firms")
plt.show()


# In[55]:


import matplotlib.pyplot as plt


# In[56]:


import numpy as np
x = np.random.randn(10000)


# In[57]:


plt.title("Histogram Example")
plt.xlabel ("Random Data")
plt.ylabel("Frequency")


# In[58]:


plt.hist(x, 10)


# In[59]:


plt.show()


# In[60]:


import matplotlib.pyplot as plt


# In[64]:


from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
figure = plt.figure(1, figsize = (12, 4))
subplot3d = plt.subplot(111, projection='3d')
surface = subplot3d.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0.1)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




