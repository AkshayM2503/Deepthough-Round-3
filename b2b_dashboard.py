import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# Set Streamlit page layout
st.set_page_config(layout="wide", page_title="B2B Outreach Dashboard")
st.title("📊 B2B Outreach Dashboard")

# Create figure and grid layout
fig = plt.figure(figsize=(24, 14), dpi=100)
gs = gridspec.GridSpec(3, 4, figure=fig, hspace=0.85, wspace=0.5)
fig.patch.set_facecolor('#FAFAFA')
fig.suptitle("📊 B2B Outreach Dashboard", fontsize=30, weight='bold', color="#0D47A1", y=1.02)

# Campaign-wise AIDCA Table
ax0 = fig.add_subplot(gs[0, :])
ax0.axis('off')
headers = ['Attention', 'Interest', 'Desire', 'Conviction']
campaigns = [['68%', '58%', '55%', '50%'],
             ['67%', '62%', '63%', '30%'],
             ['45%', '45%', '45%', '10%'],
             ['20%', '35%', '38%', '8%']]
row_labels = ['Campaign 1', 'Campaign 2', 'Campaign 3', 'Campaign 4']
table = ax0.table(cellText=campaigns, colLabels=headers, rowLabels=row_labels,
                  cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(20)
table.scale(1.8, 2.3)
for key, cell in table.get_celld().items():
    if key[0] == 0 or key[1] == -1:
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#1976D2')
    else:
        cell.set_facecolor('#E3F2FD')
ax0.set_title("📋 Campaign-wise AIDCA Diagnosis", fontsize=24, weight='bold', pad=30)

# Funnel Conversion Metrics
ax1 = fig.add_subplot(gs[1, 0])
ax1.axis('off')
conversion_values = [100, 76.5, 44.1, 19.6]
stage_labels = ['Lead', 'MQL', 'SQL', 'Client']
percent_labels = [f"{v}%" for v in conversion_values]
bar_colors = ['#90CAF9', '#64B5F6', '#42A5F5', '#1E88E5']
bg_color = '#E3F2FD'
bar_height = 0.7
y_positions = np.arange(len(conversion_values))[::-1]  # [3, 2, 1, 0]

for y, percent, percent_label, stage, color in zip(
        y_positions, conversion_values, percent_labels, stage_labels, bar_colors):
    
    ax1.barh(y, 1.0, left=0, height=bar_height, color=bg_color, edgecolor='black')
    ax1.barh(y, percent / 100, left=0, height=bar_height, color=color, edgecolor='black')
    ax1.text(-0.02, y, stage, ha='right', va='center', fontsize=16, weight='bold')
    ax1.text(0.5, y, percent_label, ha='center', va='center',
             color='black', fontsize=16, weight='bold')

ax1.set_ylim(-0.5, len(conversion_values) - 0.5)
ax1.set_xlim(-0.1, 1.05)
ax1.set_title("🔁 Funnel Conversion Metrics (Lead → Client)", fontsize=20, weight='bold')

box = ax1.get_position()
ax1.set_position([box.x0 - 0.03, box.y0, box.width, box.height])

box = ax1.get_position()
ax1.set_position([box.x0 - 0.03, box.y0, box.width, box.height])

# Persona Analysis
ax2 = fig.add_subplot(gs[1, 1])
personas = ['Persona A', 'Persona B', 'Persona C']
c1, c2, c3 = [60, 50, 65], [55, 70, 60], [70, 55, 75]
x = np.arange(len(personas))
bw = 0.2
ax2.bar(x - bw, c1, width=bw, label='C1', color='#64B5F6', edgecolor='black')
ax2.bar(x, c2, width=bw, label='C2', color='#FFD54F', edgecolor='black')
ax2.bar(x + bw, c3, width=bw, label='C3', color='#4DB6AC', edgecolor='black')
ax2.set_xticks(x)
ax2.set_xticklabels(personas, fontsize=16)
ax2.set_yticks(np.arange(0, 101, 20))
ax2.set_ylim(0, 100)
ax2.set_title("🧍 Persona Analysis", fontsize=20, weight='bold')
ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
           ncol=3, fontsize=14, frameon=True, edgecolor='black')

# Engagement
ax3 = fig.add_subplot(gs[1, 2])
channels = ['Email', 'LinkedIn', 'Webinar', 'Ad']
values = [80, 60, 50, 55]
colors = ['#42A5F5', '#81C784', '#FFB74D', '#FFB74D']
ax3.bar(channels, values, color=colors, edgecolor='black')
ax3.set_ylim(0, 100)
ax3.set_title("📬 Engagement", fontsize=20, weight='bold')
ax3.tick_params(axis='x', labelsize=14)
ax3.tick_params(axis='y', labelsize=12)

# Message Effectiveness
ax4 = fig.add_subplot(gs[1, 3])
stages = ['Attention', 'Interest', 'Desire', 'Conviction']
scores = [55, 65, 60, 55]
ax4.bar(stages, scores, color='#42A5F5', edgecolor='black')
ax4.set_ylim(0, 100)
ax4.set_title("📣 Message Effectiveness", fontsize=20, weight='bold')
ax4.tick_params(axis='x', labelsize=14)
ax4.tick_params(axis='y', labelsize=12)

# Persona Split
ax5 = fig.add_subplot(gs[2, 0])
ax5.pie([33, 34, 33], labels=['Persona A', 'Persona B', 'Persona C'],
        colors=['#64B5F6', '#FFD54F', '#4DB6AC'], startangle=90,
        autopct='%1.1f%%', textprops={'fontsize': 14},
        wedgeprops={'edgecolor': 'black'})
ax5.set_title("🔍 Persona Split", fontsize=20, weight='bold')

# Message Split
ax6 = fig.add_subplot(gs[2, 1])
ax6.pie([25, 75], labels=['Cold', 'Warm'], colors=['#64B5F6', '#4DB6AC'],
        startangle=90, autopct='%1.1f%%', textprops={'fontsize': 14},
        wedgeprops={'edgecolor': 'black'})
ax6.set_title("📧 Message Split", fontsize=20, weight='bold')

# Strategic Recommendations
ax7 = fig.add_subplot(gs[2, 2:])
ax7.axis('off')
recommendations = [
    "• Improve Conviction stage in Campaign 2",
    "• Target Persona B in new campaigns",
    "• Refine messaging for Desire stage"
]
ax7.text(0.01, 0.6, "\n".join(recommendations), fontsize=18, verticalalignment='center',
         bbox=dict(facecolor='#E0F7FA', edgecolor='gray', boxstyle='round,pad=1'))
ax7.set_title("📌 Strategic Recommendations", fontsize=22, weight='bold')

# Show in Streamlit
st.pyplot(fig)