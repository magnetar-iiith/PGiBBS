import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 18}


legend_properties = {'weight':'bold', 'size':'15'}

l = np.arange(1,100,1)
T = 50.0
c_t = []

eps_q_01 = []
eps_q_05 = []
eps_q_1 = []
eps_q_111 = []
for i in l:
    func1 = lambda k : np.exp(k * 1.5)
    func2 = lambda k : np.exp(k*1)
    func3 = lambda k : np.exp(k*0.5)
    func4 = lambda k : np.exp(k*0.25)
    c_t_01 = np.log(binom.expect(func1,  args=(i+1, 0.1)))
    c_t_05 = np.log(binom.expect(func2,  args=(i+1, 0.1)))
    c_t_1 = np.log(binom.expect(func3,  args=(i+1, 0.1)))
    c_t = np.log(binom.expect(func4,  args=(i+1, 0.1)))
    eps_q_01.append((1.0/float(i) * (T*c_t_01-np.log(1/100.0))))
    eps_q_05.append((1.0/float(i) * (T*c_t_05-np.log(1/100.0))))
    eps_q_1.append((1.0/float(i) * (T*c_t_1-np.log(1/100.0))))
    eps_q_111.append((1.0/float(i) * (T*c_t-np.log(1/100.0))))


f = []
f.append(eps_q_01)
f.append(eps_q_05)
f.append(eps_q_1)
f.append(eps_q_111)


#print(f[2])




val = [1.5,1,0.5,0.25]
c=0


plt.plot(l,f[0], label = r'$\Gamma_\infty=$'+str(val[0]),linewidth="3")
plt.plot(l,f[1], label = r'$\Gamma_\infty=$'+str(val[1]),linewidth="3")
plt.plot(l,f[2], label = r'$\Gamma_\infty=$'+str(val[2]),linewidth="3")
plt.plot(l,f[3], label = r'$\Gamma_\infty=$'+str(val[3]),linewidth="3")
plt.xlabel(r'$\lambda$', fontsize = "25", fontweight="bold")
plt.ylabel(r'$\epsilon_s$', fontsize = "25", fontweight="bold")
plt.title(r'$\lambda$ vs $\epsilon_s$ for different $\Gamma_\infty$, $\delta=0.01,q=0.1,T=50$', fontsize = "25", fontweight="bold")
plt.yticks(weight = 'bold',fontsize="15")
plt.xticks(weight = 'bold',fontsize="15")
plt.legend(prop=legend_properties)
#fig.tight_layout()
plt.show()
