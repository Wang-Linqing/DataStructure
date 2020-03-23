import trsfile
import numpy
with trsfile.open('./0_255_align.trs', 'r') as traces:
	data=numpy.array(traces)
	# Show all headers
	# for header, value in traces.get_headers().items():
	# 	print(header, '=', value)
	# print()

	# Iterate over the first 25 traces
	# for i, trace in enumerate(traces[0:25]):
	# 	print('Trace {0:d} contains {1:d} samples'.format(i, len(trace)))
	# 	print('  - minimum value in trace: {0:f}'.format(min(trace)))
	# 	print('  - maximum value in trace: {0:f}'.format(max(trace)))
print(data.shape)