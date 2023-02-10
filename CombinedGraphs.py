import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("respondent_data.csv")

questions = df['Profession'].unique()
options = ['None', '1 to 10', '11 to 25', '26 to 50', 'More than 50', 'No Response']

response_matrix = np.zeros((len(questions), len(options)))
for i, question in enumerate(questions):
    for j, option in enumerate(options):
        row = df[(df['Profession'] == question) & (df['Option'] == option)]['Response']
        if len(row) > 0:
            response_matrix[i, j] = row.values[0]

colors = ['darkblue', 'blue', 'teal', 'lightgreen', 'green', 'grey']
fig, ax = plt.subplots(figsize=(20, 10))
bottom = np.zeros(len(questions))
for i, option in enumerate(options):
    ax.barh(questions, response_matrix[:, i], color=colors[i], height=0.55, left=bottom)
    for j, question in enumerate(questions):
        if response_matrix[j, i] > 0:
            y = j - 0.4 if i in [0, 2, 5] else j + 0.4 if i in [1, 3] else j
            ax.annotate(f"{int(response_matrix[j, i])} ({response_matrix[j, i]/np.sum(response_matrix[j])*100:.1f}%)", 
                        (bottom[j]+response_matrix[j, i]/2, y), 
                        ha='center', va='center')

    bottom += response_matrix[:, i]

ax.set_title('Figure 1. Number of bedside ultrasounds (POCUS) performed in the last 30 days?')
ax.legend(options, loc='center left', bbox_to_anchor=(1.05, 0.5), frameon=False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
plt.text(0,-1,'Survey given to 130 different medical professionals asking number of times they used POCUS in the last 30 days. Attending Pysicans (N=70), Physician Assistant (N=21), Nurse Practitioner (N=12), Registered Nurse (N=27)')
plt.show()

df = pd.read_csv("survey_data.csv")

questions = df['Question'].unique()
options = ['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree', 'No Response']

response_matrix = np.zeros((len(questions), len(options)))
for i, question in enumerate(questions):
    for j, option in enumerate(options):
        row = df[(df['Question'] == question) & (df['Option'] == option)]['Response']
        if len(row) > 0:
            response_matrix[i, j] = row.values[0]

response_matrix = response_matrix / response_matrix.sum(axis=1, keepdims=True)

colors = ['darkgreen', 'green', 'yellow', 'orange', 'red', 'grey']
fig, ax = plt.subplots(figsize=(20, 10))
bottom = np.zeros(len(questions))
for i, option in enumerate(options):
    ax.barh(questions, response_matrix[:, i], color=colors[i], height=0.55, left=bottom)
    for j, question in enumerate(questions):
        if response_matrix[j, i] > 0:
            y = j - 0.4 if i in [0, 4] else j + 0.4 if i in [1, 5] else j
            ax.annotate(f"{int(response_matrix[j, i] * df[df['Question'] == question]['Response'].sum())} "
            f"({response_matrix[j, i]/response_matrix[j].sum()*100:.1f}%)", 
                    (bottom[j]+response_matrix[j, i]/2, y), 
                    ha='center', va='center')

    bottom += response_matrix[:, i]

ax.set_title('Figure 2. POCUS Responses')
ax.legend(options, loc='center left', bbox_to_anchor=(1.05, 0.5), frameon=False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
plt.text(0,-1,'Survey Questions and their reposnes from group of Medcial Professionals (N=130) from Figure 1.')
plt.show()