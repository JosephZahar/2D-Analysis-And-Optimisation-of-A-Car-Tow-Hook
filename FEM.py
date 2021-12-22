import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = {'Thickness (mm)': [14.77, 21.27, 26.27, 31.27, 36.27],
      'Inner Radius (mm)': [31.5, 25, 20, 15, 10],
      'Maximum Stress (MPa)': [630, 485.3, 508, 456, 462],
      'Original critical point Stress (MPa)': [630, 285.5, 194, 135, 104],
      'Maximum Displacement (mm)': [1.68, 1.1, 1.09, 0.96, 0.9],
      'Deformation Factor': [20.8,23.82,24.73,25.89,26.49]}

Parameter1 = pd.DataFrame(df, columns=['Thickness (mm)', 'Inner Radius (mm)', 'Maximum Stress (MPa)',
                                       'Original critical point Stress (MPa)', 'Maximum Displacement (mm)','Deformation Factor'])


print('\n', Parameter1.to_markdown())

fonttype = {'fontname': 'Times New Roman'}
ax1 = plt.subplot(212)
plt.plot(Parameter1['Thickness (mm)'], Parameter1['Maximum Stress (MPa)'],color='mediumvioletred', marker='o')
plt.plot(Parameter1['Thickness (mm)'], Parameter1['Original critical point Stress (MPa)'], color='steelblue', marker = 'o')
plt.setp(ax1.get_xticklabels(), fontsize=12, **fonttype)
ax1.set_ylabel('Stress (MPa)', fontsize=12, **fonttype)
ax1.set_xlabel('Thickness (mm)', fontsize=12, **fonttype)
ax1.legend(['New Max Stress', 'Stress at Original Critical Point'],
                loc='upper right', borderaxespad=0., prop={"size": 12,"family": 'Times New Roman'})

ax2 = plt.subplot(211, sharex=ax1)
plt.plot(Parameter1['Thickness (mm)'], Parameter1['Maximum Displacement (mm)'], color='forestgreen', marker='o')
plt.setp(ax2.get_xticklabels(), visible=False, fontsize=12, **fonttype)
ax2.set_ylabel('Maximum Displacement (mm)', fontsize=12, **fonttype)
ax2.set_title('Maximum Stress & Displacement against Thickness', fontsize=14, **fonttype, weight = 'bold')
plt.rcParams['figure.dpi'] = 360

for tick in ax1.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax2.get_yticklabels():
    tick.set_fontname("Times New Roman")

plt.show()

df1 = {'Shape': ['Original','4 Triangles','3 Triangles ','2 Triangles','8 Circles','Elongated Rectangle','No Empty Space'],
      'Maximum Stress (MPa)': [630,660, 651, 683.6, 680, 575,684],
      'Maximum Displacement (mm)': [1.685,1.482, 1.90, 1.498, 1.496, 2.593, 1.395],
       'Deformation Factor': [20.8,18.34,14.01,18.25,18.12,9.981,19.52]}


Parameter2 = pd.DataFrame(df1, columns=['Shape', 'Maximum Stress (MPa)',
                                        'Maximum Displacement (mm)','Deformation Factor'])

Parameter2.sort_values(['Maximum Stress (MPa)'], ascending=True, axis=0, inplace=True)

print('\n', Parameter2.to_markdown())

fonttype = {'fontname': 'Times New Roman'}
fig2 = plt.figure(figsize=(12, 6))
ax1 = plt.subplot(212)
plt.plot(Parameter2['Shape'], Parameter2['Maximum Stress (MPa)'],color='mediumvioletred', marker='o')
plt.setp(ax1.get_xticklabels(), fontsize=12, **fonttype)
ax1.set_ylabel('Maximum Stress (MPa)', fontsize=12, **fonttype)
ax1.set_xlabel('Shape', fontsize=12, **fonttype)


ax2 = plt.subplot(211, sharex=ax1)
plt.plot(Parameter2['Shape'], Parameter2['Maximum Displacement (mm)'], color='forestgreen', marker='o')
plt.setp(ax2.get_xticklabels(), visible=False, fontsize=12, **fonttype)
ax2.set_ylabel('Maximum Displacement (mm)', fontsize=12, **fonttype)
ax2.set_title('Maximum Stress & Displacement against Shape', fontsize=14, **fonttype, weight = 'bold')
plt.rcParams['figure.dpi'] = 360


for tick in ax1.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax2.get_yticklabels():
    tick.set_fontname("Times New Roman")

plt.savefig('S.png')