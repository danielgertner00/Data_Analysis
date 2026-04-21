import os
from go_nogo_data import gng
from taskswitching_data import tsc

# Go / No Go
gng1_path = r"/media/daniel/7E56-3F49/Studia/trening_uwaz/tasks/#TASK_DATA/TEST1/go_nogo"
gng1_list = os.listdir(gng1_path)
gng2_path = r"/media/daniel/7E56-3F49/Studia/trening_uwaz/tasks/#TASK_DATA/TEST2/go_nogo"
gng2_list = os.listdir(gng2_path)

gng1_results = gng(gng1_list,gng1_path)
gng2_results = gng(gng2_list,gng2_path)

# Taskswitching
tsc1_path = r"/media/daniel/7E56-3F491/Studia/trening_uwaz/tasks/TASK_DATA/TEST1/taskswitching_cued"
tsc1_list = os.listdir(tsc1_path)
tsc2_path = r"/media/daniel/7E56-3F491/Studia/trening_uwaz/tasks/TASK_DATA/TEST2/taskswitching_cued"
tsc2_list = os.listdir(tsc2_path)

tsc1_results = tsc(tsc1_list,tsc1_path)
tsc2_results = tsc(tsc2_list,tsc2_path)

# d2-R
d2R_1 = []
d2R_2 = []

# Questionnaires
quest_1 = []
quest_2 = []

##########################################################################





