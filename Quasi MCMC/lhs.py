import numpy as np
import matplotlib.pyplot as plt

itr = 100
mc = []
lhs = []

mc_var = []
lhs_var = []

mc_mean_err = []
lhs_mean_err = []
mc_err = []
lhs_err = []

num_samples = 1

def gen_lhs_samples(num_strat):
    strat_size = 1/num_strat
    init = 0
    lhs_samples = []
    while init<1:
        sample = np.random.uniform(init, init+strat_size)
        lhs_samples.append(sample)
        init = init+strat_size
    return np.array(lhs_samples)

def calc_int(samples):
    sq = np.square(samples)
    area = np.sum(sq)/len(samples)
    return area

while num_samples < 50:
    mc = []
    lhs = []
    mc_err = []
    lhs_err = []
    for i in range(100):
        mc_samples = np.random.uniform(0,1,(num_samples,1))
        num_strat = num_samples
        lhs_samples = gen_lhs_samples(num_strat)

        mc_ar = calc_int(mc_samples)
        mc.append(mc_ar)
        lhs_ar = calc_int(lhs_samples)
        lhs.append(lhs_ar)

        mc_err.append(np.abs(mc_ar - 1/3))
        lhs_err.append(np.abs(lhs_ar - 1/3))

    mc_mean_err.append(np.mean(mc_err))
    lhs_mean_err.append(np.mean(lhs_err))
    mc_var.append(np.var(mc))
    lhs_var.append(np.var(lhs))
    num_samples = num_samples+1
plot_lines = []

l1, = plt.plot(mc_var, label = "Monte Carlo")
l2, = plt.plot(lhs_var , label = "LHS")
plt.title('Variance plots')
plt.xlabel('number of samples')
plt.ylabel('Variance')
plot_lines.append([l1,l2])
legend1 = plt.legend(plot_lines[0], ["Monte Carlo", "LHS"], loc=1)
plt.gca().add_artist(legend1)

plt.show()
