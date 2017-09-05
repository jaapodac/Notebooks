
# coding: utf-8

# # In this, my first notebook, I will explore some of how I can present
# #information. It looks a lot like Mathematica to me. No Spell checking . Hmmm. Let's see..

# In[8]:

## Observations. (Easier to see up here)


# In[ ]:

## Automatic save is a little too often.


# Note on directory navigation: https://stackoverflow.com/questions/4810927/how-to-go-up-a-level-in-the-src-path-of-a-url-in-html
#         "../ "   Does not work!
#         So keep charts and graphics in the same folder as the notebook.

# In[ ]:

Installed nbextensions from https://github.com/ipython-contrib/jupyter_contrib_nbextensions
    Now I control the Automatic Saves (every 15 minutes rather than every 2)
    There are a whole host of other configurable features


# In[22]:

from IPython.core.display import display, HTML
display(HTML('<img src="Jupyter-Menu-Example.png">' ))
print("Available under nbextensions:")


# In[ ]:

Trying out some simple Python


# In[1]:

someList = [9,8,7,6,5,4,3,2,1]


# In[2]:

for i in someList:
    print(i**3)


# In[ ]:

Graphic Inserts. According to https://stackoverflow.com/questions/25698448/how-to-embed-html-into-ipython-output

The trick is to wrap it in "display" as well.


# In[13]:

from IPython.core.display import display, HTML
display(HTML('<h1>Hello, world!</h1><img src="Capture.png">' ))


# In[ ]:

Or, just using Python


# In[3]:

from IPython.display import Image
Image(filename='Capture.png')


# In[23]:

from IPython.display import Image
# From: Jonathan Whitmore https://www.youtube.com/watch?v=JI1HWUAyJHE&index=44&list=WL
Image(filename='Folder-Explanation.png')


# In[24]:

from IPython.display import Image
# From: Jonathan Whitmore https://www.youtube.com/watch?v=JI1HWUAyJHE&index=44&list=WL
Image(filename='Process-Of-Using-Versioning.png')


# In[26]:

from IPython.display import Image
# From: Jonathan Whitmore https://www.youtube.com/watch?v=JI1HWUAyJHE&index=44&list=WL
Image(filename='Use-Post-Save-Hooks.png')


# In[ ]:

##(It was complicated to add this snippet given the change from iPython to Jupyter)
Do Not Execute this Here


# In[ ]:

import os
from subprocess import check_call
# Add this to ipython_notebook_config.py to Save Jupyter Notebooks as .py and .html files automatically. 
def post_save(model, os_path, contents_manager):
    """post-save hook for converting notebooks to .py and .html files."""
    if model['type'] != 'notebook':
        return # only do this for notebooks
    d, fname = os.path.split(os_path)
    check_call(['jupyter', 'nbconvert', '--to', 'script', fname], cwd=d)
    check_call(['jupyter', 'nbconvert', '--to', 'html', fname], cwd=d)

c.FileContentsManager.post_save_hook = post_save


# In[25]:

from IPython.display import Image
# From: Jonathan Whitmore https://www.youtube.com/watch?v=JI1HWUAyJHE&index=44&list=WL
Image(filename='What-This-snippet-does.png')


# In[ ]:

Doing a whole "print" and "display" combo  here.


# In[2]:

from IPython.core.display import display, HTML
display(HTML('<h1>Hello, world!</h1>'))
print("Here's a link:")
display(HTML("<a href='http://www.google.com' target='_blank'>www.google.com</a>"))
print("some more printed text ...")
display(HTML('<p>Paragraph text here ...</p>'))


# In[ ]:

Now to try equations...


# In[ ]:

All from http://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Typesetting%20Equations.ipynb


# In[ ]:

\begin{align}
\dot{x} & = \sigma(y-x) \\dot{y} & = \rho x - y - xz \\dot{z} & = -\beta z + xy
\end{align}


# In[ ]:

\begin{equation*}
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
\end{equation*}


# In[ ]:

\begin{equation*}
\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0
\end{vmatrix}  
\end{equation*}


# MaxWell's Equations'

# In[8]:

from IPython.core.display import display, HTML
display(HTML('{1 \over \lambda}  = R \left({1\over n_1}-{1\over n_2}\right)'))


# Pasted from another notebook, but the takeaway was to setup the inline formulae in Markdown cell

# The differents frequencies emmited by an hydrogen atom is given by the rydberg formulae :
# 
# $$ {1 \over \lambda}  = R \left({1\over n_1}-{1\over n_2}\right) $$
# 
# Which gives a similar relation on the emitted frequencies of the Hydrogen :
# 
# $$ f_{n,m}={c \over \lambda}  = {R_h\over h} \left({1\over n}-{1\over m}\right) $$
# 
# for $n=1$ we've got the Lyman series, and for $n=2$ we have the Balmer series

# In[4]:

\begin{align}
\nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\   \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\nabla \cdot \vec{\mathbf{B}} & = 0 
\end{align}


# In[ ]:

Must wrap inline latex equations in Python, HTML construct!


# In[6]:

from IPython.core.display import display, HTML
display(HTML('This expression $\sqrt{3x-1}+(1+x)^2$ is an example of a TeX inline equation in a [Markdown-formatted](http://daringfireball.net/projects/markdown/) sentence.'))


# In[5]:

This expression $\sqrt{3x-1}+(1+x)^2$ is an example of a TeX inline equation in a [Markdown-formatted](http://daringfireball.net/projects/markdown/) sentence.


# In[ ]:

$$
\begin{array}{c}
y_1 \\y_2 \mathtt{t}_i \\z_{3,4}
\end{array}
$$
$$
\begin{array}{c}
y_1 \cr
y_2 \mathtt{t}_i \cr
y_{3}
\end{array}
$$
$$\begin{eqnarray} 
x' &=& &x \sin\phi &+& z \cos\phi \z' &=& - &x \cos\phi &+& z \sin\phi \\end{eqnarray}$$
$$
x=4
$$


# In[1]:

print("idk")


# In[ ]:



