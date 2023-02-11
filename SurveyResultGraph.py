#import numpy pandas and matplotlib for data science 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read in the survey data
df = pd.read_csv("survey_data.csv")

#set questions and their options into an array for matrix
questions = df['Question'].unique()
options = ['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree', 'No Response']

#fill the questions and options into the matrix
response_matrix = np.zeros((len(questions), len(options)))
for i, question in enumerate(questions):
    for j, option in enumerate(options):
        row = df[(df['Question'] == question) & (df['Option'] == option)]['Response']
        if len(row) > 0:
            response_matrix[i, j] = row.values[0]

#normalize for percentage based results
response_matrix = response_matrix / response_matrix.sum(axis=1, keepdims=True)

#plot the data in the response matrix, set color and labels
colors = ['#0a5d00', '#1fc600', 'yellow', 'orange', 'red', 'grey']
fig, ax = plt.subplots(figsize=(20, 10))
bottom = np.zeros(len(questions))
for i, option in enumerate(options):
    ax.barh(questions, response_matrix[:, i], color=colors[i], height=0.55, left=bottom)
    for j, question in enumerate(questions):
        if response_matrix[j, i] > 0:
            y = j - 0.15 if i == 4 else j + 0.15 if i == 3 else j
            color = 'white' if i in [0, 5] else 'black'
            ax.annotate(f"{int(df[(df['Question'] == question) & (df['Option'] == options[i])]['Response'].sum())} ({response_matrix[j, i]/response_matrix[j].sum()*100:.1f}%)", 
                        (bottom[j]+response_matrix[j, i]/2, y), 
                        ha='center', va='center', color=color)
    bottom += response_matrix[:, i]

#do some finishing touches to make everything look nice and show the graph
question_labels = []
for question in questions:
    words = question.split()
    label = words[0]
    count = 1
    for word in words[1:]:
        if count % 9 == 0:
            label += '\n'
        label += ' ' + word
        count += 1
    question_labels.append(label)
ax.set_yticklabels(question_labels)
ax.legend(options, loc='center', bbox_to_anchor=(0.4, -0.1), frameon=False, ncol = len(options), fontsize = 20)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.xaxis.set_tick_params(labelsize=14)
ax.xaxis.set_ticks(np.arange(0, 1.1, 0.1))
ax.xaxis.set_ticklabels(['{:.0%}'.format(x) for x in np.arange(0, 1.1, 0.1)], fontname="Times New Roman")
plt.yticks(fontsize=20, fontname="Times New Roman")
plt.show()




