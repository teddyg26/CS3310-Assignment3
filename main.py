# geeksforgeeks.org Was referenced in developing this project
# to better understand implementation of data structures.

import sys

# Hoffman tree is traversed recursively.
# As such, list of final nodes must be a global variable
nodes = []

def main():
	chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
		  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
		  'U', 'V', 'W', 'X', 'Y', 'Z']
	frequencies = [77, 17, 32, 42, 120, 24, 17, 50, 76, 4, 7,
				42, 24, 67, 67, 20, 5, 59, 67, 85, 37, 12, 22,
				4, 22, 2]
	heap = minHeap(51)
	for i in range(26):
		nextNode = node(frequencies[i], chars[i], True)
		heap.insert(nextNode)
	
	heap.heapify(0)

	# Establish the heap as a huffman tree
	while(heap.size > 1):
		left = heap.remove()
		right = heap.remove()
		left.huff = 0
		right.huff = 1
		parentNode = node(left.freq + right.freq, left.char + right.char, False, left, right)
		heap.insert(parentNode)
	
	# Recursively parse edges of huffman tree into list
	# and sort alphabetically
	parseNodes(heap.Heap[1])
	nodes.sort(key = lambda node: node.char)

	wmpl = 0
	print("Letter Frequency   Code Length Freq X Len")
	print("------ --------- ------ ------ ----------")
	for i in range(26):
		print(f"{nodes[i].char}      {nodes[i].freq}          {nodes[i].huff}     {len(nodes[i].huff)}      {nodes[i].freq * len(nodes[i].huff)}")
		wmpl += nodes[i].freq * len(nodes[i].huff)
	print("The weighted minimum path length is: " + str(wmpl))
	
	return True

# HUFFMAN TREE IMPLEMENTATION
# Note: nodes will be placed into a heap, which will have additional
# nodes added to form a huffman tree
class node:
	def __init__(self, freq, char, isLeaf : bool, left = None, right = None):
		self.freq = freq
		self.char = char
		self.left = left
		self.right = right
		# huff = Direction of edge (0 or 1)
		# If edge node, huff = finished huffman code after parsing
		self.huff = ''
		self.isLeaf = isLeaf
	
	def __gt__(self, other):
		return self.freq > other.freq
	
	def __lt__(self, other):
		return self.freq < other.freq
	
# Recursively find huffman code of all nodes (as well as
# other values) and add them to global list.
def parseNodes(node, val=''): 

	# Huffman code for current node 
	newVal = val + str(node.huff) 

	# Bring nodes array into scope to add
	# edges to
	global nodes

	# Traverse the heap
	if(node.left): 
		parseNodes(node.left, newVal) 
	if(node.right): 
		parseNodes(node.right, newVal) 

	# Node is an edge, so add to list of worked out nodes
	# and write huffman code to node
	if(not node.left and not node.right):
		node.huff = newVal 
		nodes.append(node)

# MIN HEAP IMPLEMENTATION

class minHeap:
	# Initialize all of the variables needed for minHeap
	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.size = 0

		# Initialize heap of 0s and set first value to
		# smallest possible value
		self.Heap = [node(0, '', False)] * (self.maxsize + 1)
		self.Heap[0] = node(-1 * sys.maxsize, '', False)

		self.front = 1

	# Get size of heap
	def heapSize(self):
		return self.size
	
	# Returns boolean for if current node is a leaf
	def isLeaf(self, pos):
		return pos * 2 > self.size

	# Get position of left child of current node
	def leftChild(self, pos):
		return 2 * pos

	# Get position of right child of current node
	def rightChild(self, pos):
		return (2 * pos) + 1
	
	# Get position of parent of current node
	def parent(self, pos):
		return pos // 2
	
	# If node isn't full, insert a new node and then sift
	# all nodes moving up the tree
	def insert(self, newNode:node):
		# If heap is full, can't insert
		if self.size >= self.maxsize:
			return
		self.size += 1
		self.Heap[self.size] = newNode

		current = self.size

		# Sift down from added node
		if(self.Heap[self.parent(current)]):
			while self.Heap[current].freq < self.Heap[self.parent(current)].freq:
				self.swap(current, self.parent(current))
				current = self.parent(current)

	# Swap the two nodes given
	def swap(self, first, second):
		self.Heap[first], self.Heap[second] = self.Heap[second], self.Heap[first]
	
	# Heapify from node at pos
	# (Will check to see if a node needs to be moved
	# based on the definition of a min heap, recursively)
	def heapify(self, pos:int):
		# If node isn't a leaf & is greater than
		# any of its children
		if not self.isLeaf(pos):
			if(self.Heap[pos] > self.Heap[self.leftChild(pos)] or
	  		self.Heap[pos] > self.Heap[self.rightChild(pos)]):
				# Swap & heapify left child
				if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
					self.swap(pos, self.leftChild(pos))
					self.heapify(self.leftChild(pos))
				# Swap & heapify right child
				else:
					self.swap(pos, self.rightChild(pos))
					self.heapify(self.rightChild(pos))
	
	# Build heap using heapify / Heapify contents of heap
	def minHeap(self):
		for pos in range(self.size // 2, 0, -1):
			self.heapify(pos)
    
	# Pop minimum element from heap
	def remove(self):
		popped = self.Heap[self.front]
		self.Heap[self.front] = self.Heap[self.size]
		self.size -= 1
		self.heapify(self.front)
		return popped

if __name__ == '__main__':
	main()