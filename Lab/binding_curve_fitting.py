
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


# sigmoid function
# def sigmoid(x, L ,x0, k, b):
#     y = L / (1 + np.exp(-k*(x-x0))) + b
#     return (y)

# p0 = [max(ydata), np.median(xdata),1,min(ydata)] # this is an mandatory initial guess
#
# popt, pcov = curve_fit(sigmoid, xdata, ydata,p0, method='dogbox')


# Fitting function
# Hill-Langmuir equation
def Hill_Langmuir_equation(x, Ka, n):
    y = x**n/(Ka**n + x**n)
    return y


# experimental data
concentration_of_RRM_836_1162 = np.array([0.33, 0.66, 0.825, 0.99, 1.155, 1.32, 2.64])
concentration_of_RRM_1895_3281 = np.array([0.165, 0.33, 0.66, 1.32, 2.64])
bound_fraction_836 = np.array([0, 0, 0, 0.017857143, 0, 0.690384615, 1.0])
bound_fraction_1162 = np.array([0, 0, 0.058823529, 0.115384615, 0.115384615, 0.753030303, 1.0])
bound_fraction_1895 = np.array([0.027777778, 0.148809524, 0.672727273, 0.846153846, 1.0])
bound_fraction_3281 = np.array([0, 0.14619883, 0.583333333, 1.0, 1.0])
std_of_bound_fraction_836 = np.array([0, 0, 0, 0, 0, 0.410665861, 0])
std_of_bound_fraction_1162 = np.array([0, 0, 0, 0, 0, 0.113565635, 0])
std_of_bound_fraction_1895 = np.array([0.03928371, 0.092597317, 0.179990817, 0.217571317, 0])
std_of_bound_fraction_3281 = np.array([0, 0.170395348, 0.11785113, 0, 0])

# exp data and parameter list
substrate_list = [836, 1162, 1895, 3281]
color_list = ['#342273', '#50B4BF', '#168039', '#F29F05']
format_list = ['o', '^', '*', 'x']
concentration_of_RRM_list = [concentration_of_RRM_836_1162, concentration_of_RRM_836_1162,
                             concentration_of_RRM_1895_3281, concentration_of_RRM_1895_3281]
bound_fraction_list = [bound_fraction_836, bound_fraction_1162,
                       bound_fraction_1895, bound_fraction_3281]
std_of_bound_fraction_list = [std_of_bound_fraction_836, std_of_bound_fraction_1162,
                              std_of_bound_fraction_1895, std_of_bound_fraction_3281]

initial_guess = [1.5, 32.0]

for i in range(4):
    plt.errorbar(concentration_of_RRM_list[i], bound_fraction_list[i], yerr=std_of_bound_fraction_list[i],
                 fmt=format_list[i], capsize=5, capthick=1, ecolor=color_list[i], mfc=color_list[i], mec=color_list[i], label=f'{substrate_list[i]} bp')
    popt, pcov = curve_fit(Hill_Langmuir_equation, concentration_of_RRM_list[i], bound_fraction_list[i], initial_guess, maxfev=60000000)
    print(f'{substrate_list[i]}: \n\tK_a={list(popt)[0]} \n\tn={list(popt)[1]} \n\tK_d={list(popt)[0]**list(popt)[1]}\n')
    x_fit = np.arange(0.0, 2.7, 0.01)
    plt.plot(x_fit, Hill_Langmuir_equation(x_fit, *popt), color=color_list[i])

# plt.errorbar(concentration_of_RRM_list[1], bound_fraction_list[1], yerr=std_of_bound_fraction_list[1],
#              fmt=format_list[1], capsize=5, capthick=1, ecolor=color_list[1], mfc=color_list[1], mec=color_list[1], label=f'{substrate_list[1]} bp')
# popt, pcov = curve_fit(Hill_Langmuir_equation, concentration_of_RRM_list[1], bound_fraction_list[1], initial_guess, maxfev=6000000)
# print(f'{substrate_list[1]}: \n\tK_d={list(popt)[0]} \n\tn={list(popt)[1]}\n')
# x_fit = np.arange(0.0, 2.7, 0.01)
# plt.plot(x_fit, Hill_Langmuir_equation(x_fit, *popt), color=color_list[1])


plt.xlabel('[RRM] (μM)')
plt.ylabel('condensed fraction')
plt.legend()
plt.savefig('binding_curve.png', dpi=300)
