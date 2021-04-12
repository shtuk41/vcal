import numpy as np

def unit(vec):
	mag = magnitude(vec);
	return vec / magnitude(vec);

def dot(vec1, vec2):
	return vec1[0] * vec2[0] + vec1[1] * vec2[1] + vec1[2] * vec2[2]

def cross(vec1, vec2):
	return (vec1[1] * vec2[2] - vec1[2] * vec2[1]) * np.array([1,0,0]) + \
			(vec1[2] * vec2[0] - vec1[0] * vec2[2]) * np.array([0,1,0]) + \
			(vec1[0] * vec2[1] - vec1[1] * vec2[0]) * np.array([0,0,1]);

def magnitude(vec):
	mag = np.sqrt(vec[0] * vec[0] + vec[1] * vec[1] + vec[2] * vec[2]);
	return mag;

def direction_cos(vec, coordinate_vector):
	u = unit(coordinate_vector)
	#print("unit: ", u);
	m = magnitude(vec);
	#print ("mag: ", m);
	return dot(vec, u) / m;

def direction_deg(vec, coordinate_vector):
	dircos =  direction_cos(vec, coordinate_vector);
	return np.arccos(dircos) * 180.0 / np.pi;









		

