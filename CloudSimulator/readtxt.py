import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_table("./test.txt",header =None,names=["UE","sUE","datarate","latency","Usage","sUsage"],skipfooter=8, engine = "python")
#header=None:没有每列的column name，可以自己设定
#names=[""]: 添加标题
#skipfooter=1: 不读取最后一行
#engine='python': c engine does not support skipfooter
#sep='\t'
#names=["UE","sUE","datarate","latency","jitter","ms","Usage","sUsage"]
#index_col = 0
#skiprows=[8,17,26,35,44,53,62,71]

#data2 = pd.read_csv("./test.csv",sep='\t',header =None,names = user_cols, index_col = 3,skipfooter = 1, engine="python")

dataUELatency = data.head(8)
dataUEDatarate = data.loc[[3,11,19,27,35,43,51,59],:]
#print(data)
print(dataUELatency)
print(dataUEDatarate)
'''
fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(111)
'''
ax1 = dataUELatency.plot(x='latency', y='UE', yerr = 'sUE', color = 'black',fmt='bo:', elinewidth=2,capsize=4,linewidth=0.5,figsize=(20,20))
#ax1 = plt.errorbar(x='latency', y='UE', yerr = 'sUE', fmt='o', ecolor = 'red', color = 'black', figsize=(10,8))
#dataUELatency['UE'].plot(ax=ax1, style = 'bD--', alpha = 0.4, label = 'User Equipment')
plt.xlabel('Latency requirement/miliseconds',fontsize=16)
plt.xticks(fontsize=16)
ax1.set_ylabel('Number of joined User Equipment',fontsize =16)
#ax1.set_ylim(0,1500)
ax1.set_yticks(np.arange(0,1500,step=300)) 
plt.yticks(fontsize=16)
plt.legend(loc=2,fontsize=16)

ax2 = ax1.twinx()
#dataUELatency['Usage'].plot(ax=ax2, style = 'go-.', alpha =0.5, label = 'Cloud Usage')
dataUELatency.plot(x='latency',y='Usage',ax=ax2, yerr = 'sUsage',color = 'red',fmt='rs-',elinewidth=2,capsize=4, linewidth=0.5,grid = True)
#ax2.set_ylim(0,1.5)
ax2.set_yticks(np.arange(0,1.5,step=0.3))  
ax2.set_ylabel('Cloud Usage',fontsize =16)
plt.yticks(fontsize=16)
plt.legend(loc=1,fontsize =16)

plt.title('Cloudperformance: UE and Latency',fontsize =24)
plt.savefig('CloudperformanceUELatency.png', dpi=400, bbox_inches='tight')  


ax3 = dataUEDatarate.plot(x='datarate', y='UE', yerr = 'sUE', color = 'black',fmt='bo:', elinewidth=2,capsize=4,linewidth=0.5,figsize=(20,20))
#ax1 = plt.errorbar(x='latency', y='UE', yerr = 'sUE', fmt='o', ecolor = 'red', color = 'black', figsize=(10,8))
#dataUELatency['UE'].plot(ax=ax1, style = 'bD--', alpha = 0.4, label = 'User Equipment')
plt.xlabel('Datarate requirement/Mbps',fontsize=16)
plt.xticks(fontsize=16)
plt.xscale('log',basex=2)
#ax3.set_xticks([1,2,4,8,16,32,64,128])
ax3.set_ylabel('Number of joined User Equipment',fontsize =16)
#ax1.set_ylim(0,1500)
ax3.set_yticks(np.arange(0,1500,step=300)) 
plt.yticks(fontsize=16)
plt.legend(loc=2,fontsize=16)

ax4 = ax3.twinx()
#dataUELatency['Usage'].plot(ax=ax2, style = 'go-.', alpha =0.5, label = 'Cloud Usage')
dataUEDatarate.plot(x='datarate',y='Usage',ax=ax4, yerr = 'sUsage',color = 'red',fmt='rs-',elinewidth=2,capsize=4, linewidth=0.5,grid = True)
#ax2.set_ylim(0,1.5)
ax4.set_yticks(np.arange(0,1.5,step=0.3))  
ax4.set_ylabel('Cloud Usage',fontsize =16)
plt.yticks(fontsize=16)
plt.legend(loc=1,fontsize =16)

plt.title('Cloudperformance: UE and Datarate',fontsize =24)
plt.savefig('CloudperformanceUEDatarate.png', dpi=400, bbox_inches='tight')


