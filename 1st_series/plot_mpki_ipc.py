#!/usr/bin/env python

import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

## For nbit predictors
predictors_to_plot = [ "  Nbit" , "  Static-AlwaysTaken", "  BTFNT", "  Pentium", "  Local", "  Global", "  Alpha21264", "  Tournament", "  SAT", "  T-"]

x_Axis = []
mpki_Axis = []

fp = open(sys.argv[1])
line = fp.readline()
while line:
	tokens = line.split()
	if line.startswith("Total Instructions:"):
		total_ins = int(tokens[2])
	else:
		for pred_prefix in predictors_to_plot:
			if line.startswith(pred_prefix):
				predictor_string = line.split(':')[0]
				correct_predictions = int(np.long(tokens[-2]))				
				incorrect_predictions = int(np.long(tokens[-1]))
				x_Axis.append(predictor_string)
				mpki_Axis.append(incorrect_predictions / (total_ins / 1000.0))

	line = fp.readline()

fig, ax1 = plt.subplots()
ax1.grid(True)

xAx = np.arange(len(x_Axis))
ax1.xaxis.set_ticks(np.arange(0, len(x_Axis), 1))
ax1.set_xticklabels(x_Axis, rotation=45)
ax1.set_xlim(-0.5, len(x_Axis) - 0.5)
ax1.set_ylim(min(mpki_Axis) - 0.05, max(mpki_Axis) + 0.05)
ax1.set_ylabel("$MPKI$")
line1 = ax1.plot(mpki_Axis, label="mpki", color="red",marker='x')

plt.title("MPKI")
plt.savefig((f"{sys.argv[1]}.png"),bbox_inches="tight")
