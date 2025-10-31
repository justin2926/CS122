import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# default steps

df = pd.read_csv('accident_100k.csv')

df_clean = df.copy()

states = ['CA', 'FL', 'TX', 'NY']

df_clean = df_clean[df_clean['State'].isin(states)]

# ---------- task 1 DONE ----------

df_clean['Date'] = pd.to_datetime(df_clean['Weather_Timestamp']).dt.date

state_date_grouping = df_clean.groupby(['State', 'Date']).agg(
    accident_count=('State', 'count')
).reset_index()

# data by state
ca_data = state_date_grouping[state_date_grouping['State'] == 'CA']
fl_data = state_date_grouping[state_date_grouping['State'] == 'FL']
tx_data = state_date_grouping[state_date_grouping['State'] == 'TX']
ny_data = state_date_grouping[state_date_grouping['State'] == 'NY']

# x and y for each state
x_ca = ca_data['Date'].head(10)
y_ca = ca_data['accident_count'].head(10)

x_fl = fl_data['Date'].head(10)
y_fl = fl_data['accident_count'].head(10)

x_tx = tx_data['Date'].head(10)
y_tx = tx_data['accident_count'].head(10)

x_ny = ny_data['Date'].head(10)
y_ny = ny_data['accident_count'].head(10)

# plot for each state's statistics
plt.figure(figsize=(10,5))

plt.plot(x_ca,y_ca, label="CA",marker="o")
plt.plot(x_fl,y_fl, label="FL",marker="o")
plt.plot(x_tx,y_tx, label="TX",marker="o")
plt.plot(x_ny,y_ny, label="NY",marker="o")

plt.xlabel("Date")
plt.ylabel("Number of Accidents")

plt.title("Daily Accident Counts per State")

plt.legend()
plt.show()

# ---------- task 2 DONE ----------

df_clean['Date'] = pd.to_datetime(df_clean['Weather_Timestamp']).dt.date

df_clean['DayOfWeek'] = pd.to_datetime(df_clean['Date']).dt.day_of_week
normalized_freq_per_state = df_clean.groupby('State')['DayOfWeek'].value_counts(normalize=True).reset_index()

pivoted_data = normalized_freq_per_state.pivot_table(
    index='State',
    columns='DayOfWeek',
    values='proportion'
)

sns.heatmap(pivoted_data)
plt.title("Heatmap of Accident Density by DayOfWeek and State")

plt.show()

# ---------- task 3 DONE ----------

conditions = ['Fair', 'Mostly Cloudy', 'Cloudy', 'Clear']

filtered_df = df_clean[['Severity', 'State', 'Weather_Condition']]

filtered_df = filtered_df[filtered_df['Weather_Condition'].isin(conditions)]

ca_data = filtered_df[filtered_df['State'] == 'CA']
fl_data = filtered_df[filtered_df['State'] == 'FL']
tx_data = filtered_df[filtered_df['State'] == 'TX']
ny_data = filtered_df[filtered_df['State'] == 'NY']

ca_data=ca_data[['Severity', 'Weather_Condition']]
fl_data=fl_data[['Severity', 'Weather_Condition']]
tx_data=tx_data[['Severity', 'Weather_Condition']]
ny_data=ny_data[['Severity', 'Weather_Condition']]

fig, axes = plt.subplots(2,2, figsize=(10,10))

sns.boxplot(x="Severity",y="Weather_Condition",data=ca_data, ax=axes[0,1])
plt.xticks(np.arange(2,5,1))
plt.subplot(221)
plt.title('Accident Severity in CA')

sns.boxplot(x="Severity",y="Weather_Condition",data=fl_data, ax=axes[1,1])
plt.xticks(np.arange(2,5,1))
plt.subplot(222)
plt.title('Accident Severity in FL')

sns.boxplot(x="Severity",y="Weather_Condition",data=tx_data, ax=axes[1,0])
plt.xticks(np.arange(2,5,1))
plt.subplot(223)
plt.title('Accident Severity in TX')

sns.boxplot(x="Severity",y="Weather_Condition",data=ny_data, ax=axes[0,0])
plt.xticks(np.arange(2,5,1))
plt.subplot(224)
plt.title('Accident Severity in NY')

plt.tight_layout()
plt.show()

# ---------- task 4 DONE ----------

filtered_df = df_clean[['Severity', 'State']]

ca_data = filtered_df[filtered_df['State'] == 'CA']
fl_data = filtered_df[filtered_df['State'] == 'FL']
tx_data = filtered_df[filtered_df['State'] == 'TX']
ny_data = filtered_df[filtered_df['State'] == 'NY']

x_ca = ca_data['Severity']
y_ca = ca_data['State']

x_fl = fl_data['Severity']
y_fl = fl_data['State']

x_tx = tx_data['Severity']
y_tx = tx_data['State']

x_ny = ny_data['Severity']
y_ny = ny_data['State']

plt.figure()

fig, axes = plt.subplots(2,2, figsize=(10,10))

sns.histplot(ca_data, ax=axes[0,0], discrete=True)
plt.xticks(np.arange(2,5,1))
plt.subplot(221)
plt.title('CA')
plt.xlabel("Severity")

sns.histplot(fl_data, ax=axes[0,1], discrete=True)
plt.xticks(np.arange(2,5,1))
plt.subplot(222)
plt.title('FL')
plt.xlabel("Severity")

sns.histplot(tx_data, ax=axes[1,0], discrete=True)
plt.xticks(np.arange(2,5,1))
plt.subplot(223)
plt.title('TX')
plt.xlabel("Severity")

sns.histplot(ny_data, ax=axes[1,1], discrete=True)
plt.xticks(np.arange(2,5,1))
plt.subplot(224)
plt.title('NY')
plt.xlabel("Severity")

plt.show()

# ---------- task 5 DONEEE ----------

# Does higher wind speed lead to higher severity?

filtered_df = df_clean[['State', 'Severity', 'Wind_Speed(mph)']]

ca_data = filtered_df[filtered_df['State'] == 'CA']
fl_data = filtered_df[filtered_df['State'] == 'FL']
tx_data = filtered_df[filtered_df['State'] == 'TX']
ny_data = filtered_df[filtered_df['State'] == 'NY']

ca_data = ca_data[['Severity', 'Wind_Speed(mph)']]
fl_data = fl_data[['Severity', 'Wind_Speed(mph)']]
tx_data = tx_data[['Severity', 'Wind_Speed(mph)']]
ny_data = ny_data[['Severity', 'Wind_Speed(mph)']]

fig, axes = plt.subplots(2,2, figsize=(10,10))

sns.boxplot(y='Wind_Speed(mph)', x='Severity', data=ca_data, ax=axes[0,0])
axes[0,0].set_title('Wind Speed x Severity in CA')

sns.boxplot(y='Wind_Speed(mph)', x='Severity', data=fl_data, ax=axes[0,1])
axes[0,1].set_title('Wind Speed x Severity in FL')

sns.boxplot(y='Wind_Speed(mph)', x='Severity', data=tx_data, ax=axes[1,0])
axes[1,0].set_title('Wind Speed x Severity in TX')

sns.boxplot(y='Wind_Speed(mph)', x='Severity', data=ny_data, ax=axes[1,1])
axes[1,1].set_title('Wind Speed x Severity in NY')

plt.tight_layout()
plt.show()