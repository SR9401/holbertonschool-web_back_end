export default function updateUniqueItems(m) {
	if (m instanceof Map) {
		for (const [item, quantity] of m) {
		if (quantity === 1) {
			m.set(item, 100);
		}
	}
	return m	
	}
	else {
		throw new error('Cannot process');
	}
}
