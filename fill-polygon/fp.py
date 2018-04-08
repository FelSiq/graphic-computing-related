#!/usr/bin/python3m
import math
import tkinter as tk
from enum import IntEnum
import re
import sys

class ETindex(IntEnum):
	ymax = 0
	xmin = 1
	angcoefinv = 2

class Polygon:
	def __init__(self, filepath=None, bgcol='#ffffff'):
		self.polygon = self.init(filepath) if filepath else None
		self.window = tk.Tk()
		self.imgWidth = self.window.winfo_screenwidth()
		self.imgHeight = self.window.winfo_screenheight()
		self.canvas = tk.Canvas(self.window, width=self.imgWidth, height=self.imgHeight, bg=bgcol)
		self.canvas.pack()
		self.img = tk.PhotoImage(width=self.imgWidth, height=self.imgHeight)
		self.xOffset = self.imgWidth//2
		self.yOffset = self.imgHeight//2
		self.canvas.create_image((self.xOffset, self.yOffset), image=self.img)

	def init(self, file=None):
		self.polygon = []
		if file:
			with open(file, 'r') as f:
				for line in f:
					x0, y0, x1, y1 = map(int, line.split())
					self.polygon.append((x0, y0, x1, y1))
		else:
			print('Please give a filepath which contains the polygon edges.')
		return self.polygon

	def print(self):
		tk.mainloop()

	def __fillAET__(self, ymin, ymax):
		AET = {i : [] for i in range(ymin, ymax+1)}
		for e in self.polygon:
			yA, yB, xA, xB = (e[1], e[3], e[0], e[2]) if e[1] < e[3] else (e[3], e[1], e[2], e[0])
			if yA != yB:
				m_inv = (xA - xB)/(yA - yB)
				AET[yA].append([yB, xA, m_inv])
		return AET
	
	def fill(self, color="#ff0000", printAET=False):
		if self.polygon:
			minY = min(self.polygon, key=lambda k: min(k[1], k[3]))
			maxY = max(self.polygon, key=lambda k: max(k[1], k[3]))
			minY = min(minY[1], minY[3])
			maxY = max(maxY[1], maxY[3])

			#AET/ET hash item: [Ymax, Xmin, 1/m] ->
			ET = self.__fillAET__(minY, maxY)
			AET = []
			yCur = minY
			counter = 0
			while len(AET) or len(ET):
				newVertices = ET.pop(yCur)
				for v in  newVertices:
					AET.append(v)
				aux = []
				for i in range(len(AET)):
					if AET[i][ETindex.ymax] != yCur:
						aux.append(AET[i])
				AET = aux 		
				n = len(AET)

				if printAET:
					print(counter, ':', end=' ')
					par = 0
					for o in AET:
						print('[', o[0], math.floor(o[1]) if par else math.ceil(o[1]), 
							round(o[2], 2), end= ']')
						par = not par
					print()
					counter += 1

				if n:
					AET.sort(key=lambda k: k[ETindex.xmin])
					# Draw
					i = 0
					while i < n:
						for j in range(math.ceil(AET[i][ETindex.xmin]), math.ceil(AET[i+1][ETindex.xmin])):
							if j + self.xOffset >= 0 and yCur + self.yOffset >= 0:
								self.img.put(color, (j + self.xOffset, yCur + self.yOffset))
						i += 2
					# Update x's
					for i in range(n):
						AET[i][ETindex.xmin] += AET[i][ETindex.angcoefinv]
					# Sort AET
					AET.sort(key=lambda k: k[ETindex.xmin])				
				# Update yCur
				yCur += 1
				
		else:
			print('Error: please load polygon from file first using \'init(filepath)\' method.')
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('usage:', sys.argv[0], '<polygon filepath> <RGB color (HEX #RRGGBB) (optional)>')
		exit(1)

	color = '#ff0000'
	if len(sys.argv) == 3:
		color = sys.argv[2]

	polygon = Polygon(sys.argv[1])
	polygon.fill(color)
	polygon.print()
