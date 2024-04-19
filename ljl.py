#!/usr/bin/env python
# coding: utf-8

# # 数据集的读取

# In[1]:


import pandas as pd
data=pd.read_csv(r"E:\BaiduNetdiskDownload\course_chapter.csv")
data


# In[2]:


import pandas as pd
data=pd.read_csv(r"E:\BaiduNetdiskDownload\course_task.csv")
data


# In[3]:


data1=data["title"].value_counts().sort_index()
data1


# In[4]:


import pandas as pd
data=pd.read_csv(r"E:\BaiduNetdiskDownload\course_chapter.csv")
data1=data["title"].value_counts().sort_index()
data1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']='SimHei'
data1.plot(kind="bar")
plt.show()


# In[7]:


data2=data["courseId"].value_counts().sort_index()
data2


# In[5]:


data2=data["courseId"].value_counts().sort_index()
data2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']='SimHei'
data2.plot(kind="bar",title="各个任务数量统计图")
plt.show()


# In[8]:


import pandas as pd
data=pd.read_csv(r"E:\BaiduNetdiskDownload\course_task.csv")
data3=data["type"].value_counts().sort_index()
data3


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']='SimHei'
plt.bar(range(9),data)
data=[31,700,12645,47,10261,115,6330,5706,223403]
plt.xticks(range(9),["discuss","doc","download","exercise","homework","ppt","testpaper","text","video"])
plt.xlabel("type")
plt.ylabel("数量")
plt.title("任务类型统计图")
plt.show()


# In[ ]:


import pandas as pd
data=pd.read_csv(r"E:\BaiduNetdiskDownload\course_task.csv")
data4=data["seq"].value_counts().sort_index()
data4


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']='SimHei'
data4.plot(kind="bar",title="课程安排呈现图")
plt.show()


# # 用户喜好

# In[13]:


#章节编号
import pandas as pd
data=pd.read_csv(r"E:\BaiduNetdiskDownload\course_chapter.csv")
data5=data["number"].value_counts().sort_index()
data5


# In[14]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']='SimHei'
data5.plot(kind="bar",title="章节完成的统计图")
plt.show()
data5.head(30)


# In[15]:


#任务编号
import pandas as pd
data=pd.read_csv(r"E:\BaiduNetdiskDownload\course_task.csv")
data6=data["number"].value_counts().sort_index()
data6
d6=data.sort_values(by="number",ascending=False).head(10)
d6


# In[16]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']='SimHei'
data6.plot(kind="bar",title="任务完成的统计图")
plt.show()


# In[17]:


import pandas as pd
data=pd.read_csv(r"E:\BaiduNetdiskDownload\course_task.csv")
d7=data.sort_values(by="length",ascending=False).head(10)
#t7=d7["length"].head(10).values
d7


# In[ ]:




