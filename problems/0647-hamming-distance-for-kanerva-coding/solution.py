import numpy as np

def hamming_distance_kanerva(state: list, prototypes: list, threshold: int) -> tuple:
	"""
	Compute Hamming distances and find active prototypes for Kanerva coding.

	Args:
		state: Binary state vector (list of 0s and 1s).
		prototypes: List of binary prototype vectors.
		threshold: Maximum Hamming distance for a prototype to be active.

	Returns:
		Tuple of (distances, active_indices).
	"""
	hamming_distances = []
	active_prototypes = []
	for i in range(len(prototypes)):
		hamming = np.sum(np.abs(np.array(state) - np.array(prototypes[i])))
		hamming_distances.append(hamming)
		if hamming <= threshold:
			active_prototypes.append(i)
	return (hamming_distances, active_prototypes)
	
	