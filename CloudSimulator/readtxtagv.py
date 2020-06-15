import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataagvusage = pd.read_table("./testagv.txt",header =None,names=["Expected","Joined","errJoined","datarate","latency","CUsage","errCUsage"], usecols= [0,1,2,5,6,7], skipfooter=1, engine = "python")
#header=None:没有每列的column name，可以自己设定
#names=[""]: 添加标题
#skipfooter=1: 不读取最后一行
#engine='python': c engine does not support skipfooter
#sep='\t'
#names=["UE","sUE","datarate","latency","jitter","ms","Usage","sUsage"]
#index_col = 0
#skiprows=[8,17,26,35,44,53,62,71]

#data2 = pd.read_csv("./test.csv",sep='\t',header =None,names = user_cols, index_col = 3,skipfooter = 1, engine="python")

dataagvusage['Time'] = np.arange(0,24)

#print(dataagvusage)


ax1 = dataagvusage.plot(x='Time',y='Expected',color = 'blue',linewidth=1,figsize=(10,10),alpha=0.7)
plt.xticks(fontsize=20)
ax1.set_xticks(np.arange(0,24,step=2))
ax1.set_ylabel('Number of User Equipment',fontsize =20)
ax1.set_yticks(np.arange(0,1800,step=300)) 
plt.yticks(fontsize=20)
plt.legend(loc=2,fontsize=20)

dataagvusage.plot(x='Time',y='Joined',ax=ax1, yerr = 'errJoined',color = 'red',fmt='rs-',elinewidth=2,capsize=4, linewidth=1,alpha=0.7)
ax1.legend(loc=2,fontsize =20)
plt.title('Expected vs. Real Joined',fontsize =30)
plt.grid(ls= "--",axis="y")
plt.xlabel('Time of a day',fontsize=20)
plt.savefig('Exp_Real.png', dpi=400, bbox_inches='tight')  


ax3 = dataagvusage.plot(x='Time', y='Joined', yerr = 'errJoined', color = 'blue',fmt='bo-', elinewidth=2,capsize=4,linewidth=1,figsize=(10,10),alpha=0.7)
#ax1 = plt.errorbar(x='latency', y='UE', yerr = 'sUE', fmt='o', ecolor = 'red', color = 'black', figsize=(10,8))
#dataUELatency['UE'].plot(ax=ax1, style = 'bD--', alpha = 0.4, label = 'User Equipment')
plt.xlabel('Time of a day',fontsize=20)
plt.xticks(fontsize=20)
#ax3.set_xticks([1,2,4,8,20,32,64,128])
ax3.set_xticks(np.arange(0,24,step=2))
ax3.set_ylabel('Real joined Users',fontsize =20)
#ax1.set_ylim(0,1500)
ax3.set_yticks(np.arange(0,1800,step=300)) 
plt.yticks(fontsize=20)
plt.grid(ls= "--",axis="y")
plt.legend(loc=2,fontsize=20)

ax4 = ax3.twinx()
#dataUELatency['Usage'].plot(ax=ax2, style = 'go-.', alpha =0.5, label = 'Cloud Usage')
dataagvusage.plot(x='Time',y='CUsage',ax=ax4, yerr = 'errCUsage',color = 'red',fmt='rs-',elinewidth=2,capsize=4, linewidth=1,alpha=0.7)
#ax2.set_ylim(0,1.5)
ax4.set_yticks(np.arange(0,1.1,step=0.1))  
ax4.set_ylabel('Cloud Usage',fontsize =20)
plt.yticks(fontsize=20)
ax4.legend(loc=2,fontsize =20, bbox_to_anchor=(0, 0.93))

plt.title('Users vs. Usage',fontsize =30)
plt.savefig('Users_Usages.png', dpi=400, bbox_inches='tight')

ax5 = dataagvusage.plot(x='Time',y='CUsage', yerr = 'errCUsage',color = 'blue',fmt='bs-',markersize = 2, elinewidth=2,capsize=4, linewidth=1, figsize=(10,10),alpha=0.7)
plt.xlabel('Time of a day',fontsize=20)
plt.xticks(fontsize=20)
ax5.set_xticks(np.arange(0,24,step=2))
ax5.set_ylabel('Cloud Usage',fontsize =20)
ax5.set_yticks(np.arange(0,1.1,step=0.1))
plt.yticks(fontsize=20)
plt.title('Usage in a day',fontsize =30)
plt.legend(loc=2,fontsize =20)
plt.grid(ls= "--",axis="y")
plt.savefig('Usages in a day.png', dpi=400, bbox_inches='tight')
